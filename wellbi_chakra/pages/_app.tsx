import { ChakraProvider, Link, Text, HStack } from '@chakra-ui/react';
//import { BrowserRouter, Routes, Route } from 'react-router-dom'

import '@fontsource/josefin-sans/700.css';
import theme from '../src/theme';

type NavLinkProps = { text: string };
const NavLink = ({ text }: NavLinkProps) => (
  <Link>
    <Text fontSize="xl">{text}</Text>
  </Link>
);

export default function App({ Component, pageProps }) {
    return (
        <ChakraProvider theme={theme}>
            <Component {...pageProps}/>
        </ChakraProvider>
    

        
       
    )
}