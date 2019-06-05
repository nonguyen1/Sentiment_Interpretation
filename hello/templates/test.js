

function generate_config_emotion(weights) {
    vals = Object.values(weights);
    keys = Object.keys(weights);

    let zipped = [];

    // zip the values and keys together.
    for (let i=0; i<vals.length; i++) {
        zipped.push({vals: vals[i], keys: keys[i]});
    }

    // Sort from smallest to largest
    zipped.sort(function (x, y) { return x.vals - y.vals; });

    let nzip = zipped.filter((zip) => zip.vals < 0); // zipped negative values.
    let pzip = zipped.filter((zip) => zip.vals >= 0); // zipped positive values.

    console.log(nzip);
    console.log(pzip);
//
//    let negVals = [];
//    let negKeys = [];
//
//    let posVals = [];
//    let posKeys = [];
//
//    // unzip negative
//    for (i=0; i<nzip.length; i++) {
//        let z = nzip[i];
//        negVals[i] = z.vals;
//        negKeys[i] = z.keys;
//    }
//
//    // unzip positive
//    for (i=0; i<pzip.length; i++) {
//        let z = pzip[i];
//        posVals[i] = z.vals;
//        posKeys[i] = z.keys;
//    }
//
//    console.log(negVals);
//    console.log(negKeys);
//
//    console.log(posVals);
//    console.log(posKeys);
//
//    // Build the series data to be displayed.
//
//    let series = [];
//
//
//    // Add the negative values.
//    series.push({
//        "values": negVals,
//        "decimals":2,
//        "stack":1,
//        "scales":"scale-x,scale-y",
//        'data-custom-token': negKeys,
//        "valueBox":{
//            "text":'%data-custom-token',
//            "placement":'bottom'
//        },
//        "background-color":"#fd625e"
//    })
//    // Add the positive values.
//    series.push({
//        "values": posVals,
//        "decimals":2,
//        "stack":2,
//        "scales":"scale-x-2,scale-y",
//        'data-custom-token': posKeys,
//        "valueBox":{
//            "text":'%data-custom-token',
//            "placement":'bottom'
//        },
//        "background-color":"#68d7c6"
//    })
//
//    return series;
}


a = {
    "test1":[1,2,3,4,5], 
    "test2":[1,2,3,4,5], 
    "test3":[1,2,3,4,5], 
    "test4":[1,2,3,4,5], 
}

console.log(generate_config_emotion(a));


/*
More content about what looks good and comments about what you think about the
progress

Smart defaults.


Always show the value proposition
Auto PDF generated interal documentation.

When at a pitch always need to vocalize and explain to bring value.


Improvements on video

1. The user tour was tool.
1. Behind the scenes thin.
1. Highlight the strong engineering things. like polyfilling.


*/
