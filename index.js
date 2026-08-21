const { default: makeWASocket, useMultiFileAuthState, DisconnectReason } = require('@whiskeysockets/baileys');
const { exec } = require('child_process');
const readline = require('readline');

// Interfaz para leer el número en la consola
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const question = (text) => new Promise((resolve) => rl.question(text, resolve));

async function conectarWhatsApp() {
    const { state, saveCreds } = await useMultiFileAuthState('Qrcode_Sesion');

    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: false // Desactivamos el QR visual
    });

    sock.ev.on('creds.update', saveCreds);

    // Si la sesión no existe, solicitamos el código de vinculación
    if (!sock.authState.creds.registered) {
        const numeroTelefono = await question('\n Escribe tu número de WhatsApp con código de país (ej. 521234567890): ');
        const numeroLimpio = numeroTelefono.replace(/[^0-9]/g, '');
        
        setTimeout(async () => {
            const code = await sock.requestPairingCode(numeroLimpio);
            console.log(`\n TU CÓDIGO DE VINCULACIÓN ES: ${code}\n`);
        }, 3000);
    }

    sock.ev.on('connection.update', (update) => {
        const { connection, lastDisconnect } = update;

        if (connection === 'close') {
            const shouldReconnect = lastDisconnect?.error?.output?.statusCode !== DisconnectReason.loggedOut;
            console.log(' Conexión cerrada. Reconectando...', shouldReconnect);
            if (shouldReconnect) conectarWhatsApp();
        } else if (connection === 'open') {
            console.log(' ¡Bot de WhatsApp conectado con éxito mediante código!');
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
