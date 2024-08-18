import { defineAppSetup } from "@slidev/types";
import PrimeVue from "primevue/config";
import Aura from "@primevue/themes/aura";

export default defineAppSetup(({ app, router }) => {
  app.use(PrimeVue, {
    theme: {
      preset: Aura,
    },
  });
});
