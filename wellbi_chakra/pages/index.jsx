// import {useColorModeValue } from "@chakra-ui/react";
// import { Container, VStack } from '@chakra-ui/react';
// import Home from '../src/components/Home/home';
// import Forum from '../src/components/Forum/forum';
// import Resources from '../src/components/Resources/resources';
// import Diagnose from '../src/components/Diagnose/diagnose';
// import Navbar from '../src/components/navbar';
// import Landing from '../src/components/landing'
// import ThreeCol from '../src/components/three_col'
// import ContactForm from '../src/components/contact_form'
// import Carousel from '../src/components/carousel'
// import App from "./_app"
//
//
// const Index = () => (
//   <Container maxW="container.xl" py={10} bg={useColorModeValue('#f1faee', 'gray.800')}>
//       <VStack spacing={8} alignItems="stretch" >
//           <Navbar />
//           <Landing />
//           <Carousel />
//           <ThreeCol />
//           <ContactForm />
//         {/* <Gallery />
//         </*ListingDetails />
//         <WhatsIncluded />
//         <Divider />
//           <ThingsToKnow />*/}
//       </VStack>
//   </Container>
// )
  
// export default Index

// import { app } from "firebase-admin";
// import React from "react";
// import ReactDOM from "react-dom"
// import App from "./_app"


// if (typeof window !== 'undefined') {  
//   ReactDOM.render(<App />, document.getElementByID("root"));
// }

import React from 'react';
import ReactDOM from 'react-dom';
import Head from 'next/head';
import render from 'react-dom'
import Navbar from '../src/components/navbar'
import Home from '../src/components/Home/home'
import Diagnose from "../src/components/Diagnose/diagnose"
import { Link, BrowserRouter, Routes, Route } from 'react-router-dom';
import { Component } from 'react';


class Index extends React.Component {
  //const rootElement = document.getElementById("root");
  // render() {
  //   return(
    ReactDOM.render(
      <div className='Header'>
        <BrowserRouter>
        {/* <Navbar /> */}
        <div className='Content'>
          <Routes>
            <Route path='/' element={Home} />
            {/* <Route path='/diagnose' element={Diagnose} /> */}
          </Routes>
        </div>
        </BrowserRouter>
      </div>, document.getElementById('root')
      );
//   }
      // <div>
      //   <Head>
      //     <title>QuizApp</title>
      //     <link rel="icon" href="/favicon.ico" />
      //   </Head>
      //   <main>
      //     <Home />
      //   </main>
      //   <footer></footer>
      // </div>
}

export default Index;





// import {
//   BrowserRouter as Router,
//   Routes,
//   Route,
// } from 'react-router-dom';
// import { generateKeyPair } from "crypto";
// import traceback from "traceback";

// function App() {
//   if (typeof window !== 'undefined') {
//     console.log("You're on the browser")
//     return (
//         <div className="App">
//           <Navbar />
//           <div className="Content">
//             <Routes>
//               <Route exact path="/"
//             </Routes>
//           </div>
//         </div>

//       // <Router>
//       //   <div className="App">
//       //     {/* <Container maxW="container.xl" py={10} bg={useColorModeValue('#f1faee', 'gray.800')}> */}
//       //     <Navbar />
//       //     <div className="Content">
//       //       <Routes>
//       //         <Route path="/">
//       //           <Home />
//       //         </Route>
//       //         {/* <Route path="/diagnose/">
//       //           <Diagnose />
//       //         </Route>
//       //         <Route path="/forum/">
//       //           <Forum />
//       //         </Route>
//       //         <Route path="/resources/">
//       //           <Resources />
//       //         </Route> */}
//       //       </Routes>
//       //     </div>
//       //   </div>
//       // </Router>
//     );
//   } else {
//     console.log("You're not on the browser")
//   }
  
  
// //  <Flex height="100vh" alignItems="center" justifyContent="center">
// //    <Flex direction="column" background="gray.100" p={12} rounded={6} >
// //     <Heading mb={6}>Log in</Heading>
// //     <input placeholder="lazar@chakra-ui.com" variant='filled' mb={3} type="email"/>
// //     <input placeholder="********" variant="filled" mb={6} type="password"/>
// //     <Button colorScheme = "teal">Log in</Button>   
// //    </Flex>
// //  </Flex>
// }

// export default App




// // import { ReactNode } from 'react';
// // import Head from 'next/head';
// // import {
// //   Box,
// //   Heading,
// //   Container,
// //   Text,
// //   Button,
// //   Stack,
// //   Icon,
// //   useColorModeValue,
// //   createIcon,
// //   Flex,
// //   Avatar,
// //   HStack,
// //   Link,
// //   IconButton,
// //   Menu,
// //   MenuButton,
// //   MenuList,
// //   MenuItem,
// //   MenuDivider,
// //   useDisclosure,
// // } from '@chakra-ui/react';

// // import { WellbiLogo } from ''
// // import { HamburgerIcon, CloseIcon, AddIcon } from '@chakra-ui/icons';

// // const Links = ['Dashboard', 'Projects', 'Team'];

// // const NavLink = ({ children }: { children: ReactNode }) => (
// //   <Link
// //     px={2}
// //     py={1}
// //     rounded={'md'}
// //     _hover={{
// //       textDecoration: 'none',
// //       bg: useColorModeValue('gray.200', 'gray.700'),
// //     }}
// //     href={'#'}>
// //     {children}
// //   </Link>
// // );

// import {useColorModeValue } from "@chakra-ui/react"
// import { Container, VStack } from '@chakra-ui/react';
// import Navbar from '../navbar'
// import Landing from '../landing'
// import ThreeCol from '../three_col'
// import ContactForm from '../contact_form'
// import Carousel from '../carousel'

