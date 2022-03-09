import { ReactElement } from 'react';
import { Box, SimpleGrid, Icon, Text, Stack, Flex } from '@chakra-ui/react';
import { FcConferenceCall, FcCustomerSupport, FcLibrary } from 'react-icons/fc';

interface FeatureProps {
  title: string;
  text: string;
  icon: ReactElement;
}

const Feature = ({ title, text, icon }: FeatureProps) => {
  return (
    <Stack>
      <Flex
        w={16}
        h={16}
        align={'center'}
        justify={'center'}
        color={'white'}
        rounded={'full'}
        bg={'#457b9d'}
        mb={1}>
        {icon}
      </Flex>
      <Text fontWeight={600}>{title}</Text>
      <Text color={'gray.600'}>{text}</Text>
    </Stack>
  );
};

export default function SimpleThreeColumns() {
  return (
    <Box p={4}>
      <SimpleGrid columns={{ base: 1, md: 3 }} spacing={10}>
        <Feature
          icon={<Icon as={FcConferenceCall} w={10} h={10} />}
          title={'Establish Community'}
          text={
            "Take control of your education with our community forum. Share experiences or inquire about any ailments you're facing."
          }
        />
        <Feature
          icon={<Icon as={FcLibrary} w={10} h={10} />}
          title={'Obtain Resources and Information'}
          text={
            "Knowledge is power: Empower yourself and others through discovering free and low-cost clinics near you."
          }
        />
        <Feature
          icon={<Icon as={FcCustomerSupport } w={10} h={10} />}
          title={'Contact Support'}
          text={
            "Reach out with any questions or concerns, we eagerly await feedback."
          }
        />
      </SimpleGrid>
    </Box>
  );
}