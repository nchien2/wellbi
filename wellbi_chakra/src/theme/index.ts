import { extendTheme, theme as base } from '@chakra-ui/react';
import { mode } from "@chakra-ui/theme-tools";

const theme = extendTheme({
  styles: {
    global: {
      'html, body': {
        bg: mode("#a8dadc", "#797d77"),
        color: 'gray.700',
      },
    },
  },
  colors: {
    brand: {
      pink: '#e63946',
      primary: '#f1faee',
      light_blue: '#a8dadc',
      med_blue: '#457b9d',
      dark_blue: '#1d3557',
    },
  },
  fonts: {
    heading: `Josefin Sans, ${base.fonts.heading}`,
  },
  components: {
    Button: {
      variants: {
        pill: (props) => ({
          ...base.components.Button.variants.outline(props),
          rounded: 'full',
          color: 'gray.500',
        }),
      },
    },
  },
});

export default theme;