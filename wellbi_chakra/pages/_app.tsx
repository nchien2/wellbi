import { ChakraProvider, Link, Text, HStack } from '@chakra-ui/react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import theme from '../src/theme/index'
import NavBar from '../src/components/navbar'
import Forum from '../src/components/Forum/forum'
import Resources from '../src/components/Resources/resources'
import Home from '../src/components/Home/home'

// import { ChakraProvider } from "@chakra-ui/react";

// import '@fontsource/josefin-sans/700.css';
// import theme from '../src/theme';

// type NavLinkProps = { text: string };
// const NavLink = ({ text }: NavLinkProps) => (
//   <Link>
//     <Text fontSize="xl">{text}</Text>
//   </Link>
// );

import { AppProps } from 'next/app';

export default function App({ Component, pageProps }: AppProps) {
    return (
        <ChakraProvider theme={theme}>
            <Component {...pageProps}/>
        </ChakraProvider>
    )
}



// export default function App() {
//     return (
//         <>
//             <ChakraProvider theme={theme}>
//                 <Router>
//                     <NavBar />
//                     <Routes>
//                         <Route path="/test">
//                             <Forum />
//                         </Route>
//                         <Route path="/about">
//                             <Resources />
//                         </Route>
//                         <Route path="/">
//                             <Home />
//                         </Route>
//                     </Routes>
//                 </Router>
//             </ChakraProvider>

//         </>
//     );
// }