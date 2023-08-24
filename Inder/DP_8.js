console.log("Welcome to TextInsight Character Frequency Analysis!");

const str = prompt("Please enter the text you would like to analyze:");


if(str){
    console.log("Thank you for providing the text for analysis.");
    console.log("Here is the character frequency analysis: ");

    const frequency = new Map();

    function stringFrequency(str) {
        
        for(var i=0; i<str.length; i++){
            var char = str[i];
            if(frequency.has(char)){
                frequency.set(char, frequency.get(char)+1);
            }
            else {
                frequency.set(char, 1);
            }
        }
        return frequency;
    }   
    stringFrequency(str);

    for(const [key,value] of frequency){
        console.log(`${key} occurs ${value} time`);
    }
}

