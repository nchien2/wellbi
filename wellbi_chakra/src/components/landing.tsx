import {
  Stack,
  Flex,
  Button,
  Text,
  VStack,
  useBreakpointValue,
} from '@chakra-ui/react';

export default function WithBackgroundImage() {
  return (
    <Flex
    rounded={"xl"}
      w={'full'}
      h={'100vh'}
      backgroundImage={
        'url(https://images.unsplash.com/photo-1600267175161-cfaa711b4a81?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80)'
      }
      backgroundSize={'cover'}
      backgroundPosition={'center center'}>
      <VStack
        rounded={"xl"}
        w={'full'}
        justify={'center'}
        px={useBreakpointValue({ base: 4, md: 8 })}
        bgGradient={'linear(to-r, blackAlpha.600, transparent)'}>
        <Stack maxW={'2xl'} align={'flex-start'} spacing={6}>
          <Text
            color={'white'}
            fontWeight={700}
            lineHeight={1.2}
            fontSize={useBreakpointValue({ base: '3xl', md: '4xl' })}>
            We are here to help. Click to diagnose or explore general resources.
          </Text>
          <Stack direction={'row'}>
            <Button
              bg={'#1d3557'}
              rounded={'full'}
              color={'white'}
              _hover={{ bg: '#457b9d' }}>
              Diagnose Me
            </Button>
            <Button
              bg={'#e63946'}
              rounded={'full'}
              color={'white'}
              _hover={{ bg: 'pink.300' }}>
              Explore Resources
            </Button>
          </Stack>
        </Stack>
      </VStack>
    </Flex>
  );
}
