const { default: makeWASocket, useMultiFileAuthState, DisconnectReason } = require('@whiskeysockets/baileys');
const qrcode = require('qrcode-terminal');
const { exec } = require('child_process');

async function conectarWhatsApp() {
    // Guarda los datos de la sesión para no escanear el QR cada vez
    const { state, saveCreds } = await useMultiFileAuthState('Qrcode_Sesion');

    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: false
    });

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', (update) => {
        const { connection, lastDisconnect, qr } = update;

        // Muestra el código QR en la consola de Termux
        if (qr) {
            console.log('\n Escanea este código QR con tu WhatsApp:\n');
            qrcode.generate(qr, { small: true });
        }

        if (connection === 'close') {
            const shouldReconnect = lastDisconnect?.error?.output?.statusCode !== DisconnectReason.loggedOut;
            console.log(' Conexión cerrada. Reconectando...', shouldReconnect);
            if (shouldReconnect) conectarWhatsApp();
        } else if (connection === 'open') {
            console.log(' ¡Bot de WhatsApp conectado con éxito en Termux!');
        }
    });

    // Escucha los mensajes entrantes
    sock.ev.on('messages.upsert', async (m) => {
        const msg = m.messages[0];
        if (!msg.message || msg.key.fromMe) return;

        const texto = msg.message.conversation || msg.message.extendedTextMessage?.text || '';
        const remitente = msg.key.remoteJid;

        // Si el mensaje inicia con punto (.)
        if (texto.startsWith('.')) {
            const partes = texto.split(' ');
            const comando = partes[0];
            const parametro = partes.slice(1).join(' ') || '';

            // Comando optimizado para Termux (Linux)
            const comandoPython = `python bot.py "${comando}" "${parametro}"`;
            
            exec(comandoPython, async (error, stdout, stderr) => {
                if (error) {
                    console.error(`Error en Python: ${error.message}`);
                    return;
                }
                if (stdout.trim()) {
                    await sock.sendMessage(remitente, { text: stdout.trim() });
                }
            });
        }
    });
}

conectarWhatsApp();