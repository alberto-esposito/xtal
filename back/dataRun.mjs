import XLSX from 'xlsx'
import fs from 'fs'

const rawData = XLSX.readFile('./data/XTAL_Challange.xlsx')

const currencyMap = {
  AAPL: 'USD',
  ALV: 'EUR',
  GE: 'USD',
  LLOY: 'GBP',
  BT: 'GBP',
  DPW: 'EUR',
  JNJ: 'USD'
}

const Mt = []
// const DMC = []

// console.log(rawData.Sheets.values['V1307'])

let i

const vals = rawData.Sheets.values

const xrate = rawData.Sheets.xrate

const days = 1300

for (i = 2; i < days; i++) {
  Mt[i - 2] = vals[`B${i}`].v * vals[`C${i}`].v * vals[`D${i}`].v +
        vals[`E${i}`].v * vals[`F${i}`].v * vals[`G${i}`].v / xrate[`C${i}`].v +
        vals[`H${i}`].v * vals[`I${i}`].v * vals[`J${i}`].v +
        vals[`K${i}`].v * vals[`L${i}`].v * vals[`M${i}`].v / xrate[`B${i}`].v +
        vals[`N${i}`].v * vals[`O${i}`].v * vals[`P${i}`].v / xrate[`B${i}`].v +
        vals[`Q${i}`].v * vals[`R${i}`].v * vals[`S${i}`].v / xrate[`C${i}`].v +
        vals[`T${i}`].v * vals[`U${i}`].v * vals[`V${i}`].v
}

fs.writeFile('./front/src/indexValues.mjs', `export const indexValues = [${Mt.toString()}]`, err => console.log({ err }))

// console.log({Mt})
