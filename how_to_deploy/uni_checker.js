const fs = require('fs')
const fetch = require('node-fetch')
const BN = require('bignumber.js')

async function makeRequest (address) {
//   const url = `https://gentle-frost-9e74.uniswap.workers.dev/1/${address}`
const url = `https://swap.c4ei.net/workers/21004/${address}`
  const res = await fetch(url)
  const json = await res.json()
  return json
}

async function main () {
  const data = fs.readFileSync('addresses.csv', 'utf8')
  const lines = data.split('\n')
  const startIndex = process.argv[2] >>> 0

  for (let i = startIndex; i < lines.length; i++) {
    const address = lines[i]
    if (!address) {
      console.error(`${i} empty line`)
      continue
    }

    try {
      const result = await makeRequest(address)
      const amountHex = result.amount
      if (!amountHex) {
        console.error(`${i} ${address} ${result.message}`)
        continue
      }

      const amount = new BN(amountHex).div(new BN(10e17)).toNumber()
      console.log(`${i} ${address} ${amount}`)
    } catch (err) {
      console.error(`${i} ${address} ${err.message}`)
    }
  }
}

main()

// Usage:
// $ touch addresses.csv
// $ node index.js 