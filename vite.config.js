import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  // Tells Vite that source files live inside the web directory
  root: resolve(__dirname, 'web'),
  build: {
    // Outputs exactly to web/build so EdgeOne can find it
    outDir: resolve(__dirname, 'web/build'),
    emptyOutDir: true,
  }
});
