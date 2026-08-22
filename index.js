if (texto.startsWith('.')) {
            const partes = texto.trim().split(' ');
            const comando = partes[0].toLowerCase();
            const parametro = partes.slice(1).join(' ') || '';
            
            // 📌 OBTENER EL ID REAL DEL USUARIO (Funciona tanto en grupos como en chats privados)
            const usuarioId = msg.key.participant || remitente;

            // COMANDOS DE ADMINISTRACIÓN REAL DE GRUPOS EN WHATSAPP
            if (remitente.endsWith('@g.us')) {
                try {
                    if (comando === '.close') {
                        await sock.groupSettingUpdate(remitente, 'announcement');
                        await sock.sendMessage(remitente, { text: '🔒 El grupo ha sido cerrado. Solo administradores pueden enviar mensajes.' }, { quoted: msg });
                        return;
                    } 
                    if (comando === '.open') {
                        await sock.groupSettingUpdate(remitente, 'not_announcement');
                        await sock.sendMessage(remitente, { text: '🔓 El grupo ha sido abierto. Todos pueden enviar mensajes.' }, { quoted: msg });
                        return;
                    }
                } catch (err) {
                    await sock.sendMessage(remitente, { text: '⚠️ Error: Asegúrate de que el bot sea Administrador del grupo.' }, { quoted: msg });
                    return;
                }
            }

            // COMANDOS PROCESADOS DESDE PYTHON (Le pasamos el comando, el parámetro y el ID del usuario)
            const comandoPython = `python3 bot.py "${comando}" "${parametro}" "${usuarioId}"`;
            
            exec(comandoPython, { encoding: 'utf-8' }, async (error, stdout) => {
                if (error) {
                    console.error(`Error ejecutando Python: ${error.message}`);
                    return;
                }
                
                const respuesta = stdout.trim();
                
                if (respuesta) {
                    // Si Python responde con formato de GIF
                    if (respuesta.startsWith("GIF|")) {
                        const partesGif = respuesta.split("|");
                        const urlGif = partesGif[1];
                        const mensajeTexto = partesGif[2] || "";

                        await sock.sendMessage(remitente, {
                            video: { url: urlGif },
                            caption: mensajeTexto,
                            gifPlayback: true
                        }, { quoted: msg });
                    } else {
                        // Respuesta en texto normal
                        await sock.sendMessage(remitente, { text: respuesta }, { quoted: msg });
                    }
                }
            });
        }
