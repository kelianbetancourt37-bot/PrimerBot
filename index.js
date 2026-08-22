sock.ev.on('messages.upsert', async (m) => {
    const msg = m.messages[0];
    if (!msg.message) return;

    const texto = msg.message.conversation || msg.message.extendedTextMessage?.text || '';
    const remitente = msg.key.remoteJid;

    if (texto.startsWith('.')) {
        const partes = texto.trim().split(' ');
        const comando = partes[0].toLowerCase();
        const parametro = partes.slice(1).join(' ') || '';
        
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

        // COMANDOS PROCESADOS DESDE PYTHON
        const comandoPython = `python3 bot.py "${comando}" "${parametro}" "${usuarioId}"`;
        
        exec(comandoPython, { encoding: 'utf-8' }, async (error, stdout) => {
            if (error) {
                console.error(`Error ejecutando Python: ${error.message}`);
                return;
            }
            
            const respuesta = stdout.trim();
            
            if (respuesta) {
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
                    await sock.sendMessage(remitente, { text: respuesta }, { quoted: msg });
                }
            }
        });
    }
});
