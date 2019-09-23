var unzip = require('unzipper');
const request = require('request');
const fs = require('fs');

const getData = url => {
    try {
        console.log("Downloading --->", url)
        return new Promise(async(resolve)=>{
            const req = request({url});
            var writer = req.pipe(unzip.Parse())
            writer.on('entry',(entry)=>{
                    var fileName = entry.path;
                    if (fileName.includes("-Regular.ttf")) {
                        entry.pipe(fs.createWriteStream('download/'+fileName))
                        .on('error',(err)=>{console.log(err)})
                        .on('finish',()=>{
                            resolve(fileName); //local file path
                        });
                    } else {
                        entry.autodrain();
                    }
                })
            })
    } catch (error) {
        console.log(error);
    }
};
async function main(){ 
    await getData(url);
}

main();