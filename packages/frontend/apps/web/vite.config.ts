import { defineConfig, mergeConfig } from 'vite';

import Config from '../../../../vite.config';

// https://vite.dev/config/
export default mergeConfig(Config, defineConfig({}));
