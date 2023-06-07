import React, { useState } from "react";
import { StyleSheet, Text, View, ImageBackground, Circle } from "react-native";
import MultiSlider from "@ptomasroos/react-native-multi-slider";
import SliderCustomLabel from "./SliderCustomLabel";


const img = {uri: 'https://img.freepik.com/free-photo/abstract-luxury-plain-blur-grey-black-gradient-used-as-background-studio-wall-display-your-products_1258-63644.jpg'};
const textTransformerTimes = (value) => {
  return value+" mi"
};
const TIME = {  min: 1,  max: 20 }
const SliderPad = 2;


export default function Radius({route, navigation}) {
  const { min, max } = TIME;
  const [width, setWidth] = useState(280);
  const [selected, setSelected] = useState(null);

  if (!selected) {
    setSelected([max-4]);
  }

  // Callbacks
  const onLayout = (event) => {
    setWidth(event.nativeEvent.layout.width - SliderPad * 2);
  };
  const onValuesChangeFinish = (values) => {
    setSelected(values);
  };

  return (
    <View onLayout={onLayout} style={styles.wrapper}>
        <ImageBackground source={require('./assets/border.png')} resizeMode="cover" style={styles.image}>
        <Text style={styles.header}> Select your Safety Radius</Text>
        <MultiSlider
          min={min}
          max={max}
          allowOverlap
          values={selected}
          sliderLength={width}
          onValuesChangeFinish={onValuesChangeFinish}
          enableLabel={true}
          customLabel={SliderCustomLabel(textTransformerTimes)}
          trackStyle={{
            height: 20,
            borderRadius: 8,
          }}
          markerOffsetY={3}
          selectedStyle={{
            backgroundColor: "#895CDF",
          }}
          unselectedStyle={{
            backgroundColor: "#EEF3F7",
          }}
        />
        </ImageBackground>
    </View>
  );
}




const styles = StyleSheet.create({
  wrapper: {
    flex: 1,
    margin: SliderPad * 2,
    
    justifyContent: "center",
    alignItems: "center",
  },
  image: {
    resizeMode: "stretch",
            height: 200,
            width: '100%',
    flex: 1,
    justifyContent: 'center',
  },
  header: {
    fontSize: 28,
    fontWeight: 'bold',
    paddingLeft: 8,
    paddingRight: 5
  },
  logo: { 
    width: 200, 
    height: 200, 
  },
  circleContainer: {
    alignItems: 'center',
  }
});






