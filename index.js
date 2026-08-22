async function iniciarBot() {
    const { state, saveCreds } = await useMultiFileAuthState('Qrcode_Sesion');

    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: false
    });

    sock.ev.on('creds.update', saveCreds);

    if (!sock.authState.creds.registered) {
        const numeroLimpio = "5595981068631";
        
        console.log('Generando código de vinculación...');
        setTimeout(async () => {
            try {
                const code = await sock.requestPairingCode(numeroLimpio);
                console.log(`\n TU CÓDIGO DE VINCULACIÓN ES: ${code}\n`);
            } catch (err) {
                console.error('Error al generar el código:', err.message);
            }
        }, 3000);
    }

    sock.ev.on('connection.update', (update) => {
        const { connection, lastDisconnect } = update;
        if (connection === 'close') {
            const shouldReconnect = lastDisconnect?.error?.output?.statusCode !== DisconnectReason.loggedOut;
            if (shouldReconnect) iniciarBot();
        } else if (connection === 'open') {
            console.log(' ¡Bot conectado con éxito!');
        }
    });

    // 📌 EL EVENTO DE MENSAJES DEBE IR AQUÍ DENTRO, DONDE "sock" YA EXISTE
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

            if (remitente.endsWith('@g.us')) {
                try {
                    if (comando === '.close') {
                        await sock.groupSettingUpdate(remitente, 'announcement');
                        await sock.sendMessage(remitente, { text: '🔒 El grupo ha sido cerrado.' }, { quoted: msg });
                        return;
                    } 
                    if (comando === '.open') {
                        await sock.groupSettingUpdate(remitente, 'not_announcement');
                        await sock.sendMessage(remitente, { text: '🔓 El grupo ha sido abierto.' }, { quoted: msg });
                        return;
                    }
                } catch (err) {
                    await sock.sendMessage(remitente, { text: '⚠️ Error: Asegúrate de que el bot sea Administrador.' }, { quoted: msg });
                    return;
                }
            }

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
                        await sock.sendMessage(remitente, {
                            video: { url: partesGif[1] },
                            caption: partesGif[2] || "",
                            gifPlayback: true
                        }, { quoted: msg });
                    } else {
                        await sock.sendMessage(remitente, { text: respuesta }, { quoted: msg });
                    }
                }
            });
        }
    });
}

iniciarBot();
