const { default: makeWASocket, useMultiFileAuthState, DisconnectReason } = require('@whiskeysockets/baileys');
const { exec } = require('child_process');

async function iniciarBot() {
    const { state, saveCreds } = await useMultiFileAuthState('Qrcode_Sesion');

    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: false
    });

    sock.ev.on('creds.update', saveCreds);

    // Si aún no estás registrado, solicita el código automáticamente
    if (!sock.authState.creds.registered) {
        const numeroLimpio = "5595981068631"; // Tu número de Brasil asignado directamente
        
        console.log('Generando código de vinculación para +55 95 98106-8631...');
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

    sock.ev.on('messages.upsert', async (m) => {
        const msg = m.messages[0];
        if (!msg.message || msg.key.fromMe) return;

        const texto = msg.message.conversation || msg.message.extendedTextMessage?.text || '';
        const remitente = msg.key.remoteJid;

        if (texto.startsWith('.')) {
            const partes = texto.split(' ');
            const comando = partes[0];
            const parametro = partes.slice(1).join(' ') || '';

            const comandoPython = `python bot.py "${comando}" "${parametro}"`;
            
            exec(comandoPython, async (error, stdout) => {
                if (error) return console.error(`Error: ${error.message}`);
                if (stdout.trim()) {
                    await sock.sendMessage(remitente, { text: stdout.trim() });
                }
            });
        }
    });
}

iniciarBot();
