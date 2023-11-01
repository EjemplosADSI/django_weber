import { defineConfig } from 'vite';

const { resolve } = require('path');
export default {
    build: {
        manifest: true, // agrega un manifest.json
        rollupOptions: {
            input: [ resolve(__dirname, './main.js'), ] // el punto de entrada de tu app frontend
        },
        outDir: 'static', // el directorio de salida para los archivos generados por vite
        assetsDir: 'theme', // el subdirectorio para los archivos estáticos
    },
    plugins: [], // aquí puedes agregar plugins de vite si necesitas
    server: {
        port: 3001, // el puerto del servidor de desarrollo
        open: false, // si quieres que se abra el navegador al iniciar el servidor
    }
};