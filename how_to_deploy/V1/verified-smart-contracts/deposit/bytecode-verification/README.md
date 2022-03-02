_**[DEPRECATED: The result in this directory is outdated. The deposit contract has been reimplemented in Solidity and reverified. The latest result can be found at https://github.com/runtimeverification/deposit-contract-verification.]**_

# Bytecode Verification of Deposit Contract _(Vyper Implementation)_

This directory presents the formal verification artifacts of the [deposit contract] bytecode, compiled by the Vyper compiler version [`1761-HOTFIX-v0.1.0-beta.13`].

Verified bytecode:
 * Contract creation bytecode:
   ```
   0x740100000000000000000000000000000000000000006020526f7fffffffffffffffffffffffffffffff6040527fffffffffffffffffffffffffffffffff8000000000000000000000000000000060605274012a05f1fffffffffffffffffffffffffdabf41c006080527ffffffffffffffffffffffffed5fa0e000000000000000000000000000000000060a052341561009857600080fd5b6101406000601f818352015b600061014051602081106100b757600080fd5b600260c052602060c020015460208261016001015260208101905061014051602081106100e357600080fd5b600260c052602060c020015460208261016001015260208101905080610160526101609050602060c0825160208401600060025af161012157600080fd5b60c0519050606051600161014051018060405190131561014057600080fd5b809190121561014e57600080fd5b6020811061015b57600080fd5b600260c052602060c02001555b81516001018083528114156100a4575b505061123556600436101561000d576110b0565b600035601c52740100000000000000000000000000000000000000006020526f7fffffffffffffffffffffffffffffff6040527fffffffffffffffffffffffffffffffff8000000000000000000000000000000060605274012a05f1fffffffffffffffffffffffffdabf41c006080527ffffffffffffffffffffffffed5fa0e000000000000000000000000000000000060a05260001561027f575b6101605261014052600061018052610140516101a0526101c060006008818352015b61018051600860008112156100e8578060000360020a82046100ef565b8060020a82025b905090506101805260ff6101a051166101e052610180516101e0516101805101101561011a57600080fd5b6101e0516101805101610180526101a0517ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff86000811215610163578060000360020a820461016a565b8060020a82025b905090506101a0525b81516001018083528114156100cb575b5050601860086020820661020001602082840111156101a157600080fd5b60208061022082610180600060045af15050818152809050905090508051602001806102c08284600060045af16101d757600080fd5b50506102c05160206001820306601f82010390506103206102c0516020818352015b826103205110151561020a57610226565b6000610320516102e001535b81516001018083528114156101f9575b50505060206102a05260406102c0510160206001820306601f8201039050610280525b60006102805111151561025b57610277565b602061028051036102a001516020610280510361028052610249565b610160515650005b63c5f2892f600051141561050e57341561029857600080fd5b6000610140526101405161016052600154610180526101a060006020818352015b600160016101805116141561033a5760006101a051602081106102db57600080fd5b600060c052602060c02001546020826102400101526020810190506101605160208261024001015260208101905080610240526102409050602060c0825160208401600060025af161032c57600080fd5b60c0519050610160526103a8565b6000610160516020826101c00101526020810190506101a0516020811061036057600080fd5b600260c052602060c02001546020826101c0010152602081019050806101c0526101c09050602060c0825160208401600060025af161039e57600080fd5b60c0519050610160525b61018060026103b657600080fd5b60028151048152505b81516001018083528114156102b9575b505060006101605160208261046001015260208101905061014051610160516101805163806732896102e0526001546103005261030051600658016100a9565b506103605260006103c0525b6103605160206001820306601f82010390506103c05110151561043d57610456565b6103c05161038001526103c0516020016103c05261041b565b61018052610160526101405261036060088060208461046001018260208501600060045af150508051820191505060006018602082066103e001602082840111156104a057600080fd5b60208061040082610140600060045af150508181528090509050905060188060208461046001018260208501600060045af150508051820191505080610460526104609050602060c0825160208401600060025af16104fe57600080fd5b60c051905060005260206000f350005b63621fd130600051141561061c57341561052757600080fd5b6380673289610140526001546101605261016051600658016100a9565b506101c0526000610220525b6101c05160206001820306601f8201039050610220511015156105725761058b565b610220516101e001526102205160200161022052610550565b6101c08051602001806102808284600060045af16105a857600080fd5b50506102805160206001820306601f82010390506102e0610280516020818352015b826102e0511015156105db576105f7565b60006102e0516102a001535b81516001018083528114156105ca575b5050506020610260526040610280510160206001820306601f8201039050610260f350005b632289511860005114156110af57605060043560040161014037603060043560040135111561064a57600080fd5b60406024356004016101c037602060243560040135111561066a57600080fd5b608060443560040161022037606060443560040135111561068a57600080fd5b63ffffffff6001541061069c57600080fd5b633b9aca006102e0526102e0516106b257600080fd5b6102e05134046102c052633b9aca006102c05110156106d057600080fd5b603061014051146106e057600080fd5b60206101c051146106f057600080fd5b6060610220511461070057600080fd5b610140610360525b6103605151602061036051016103605261036061036051101561072a57610708565b6380673289610380526102c0516103a0526103a051600658016100a9565b50610400526000610460525b6104005160206001820306601f8201039050610460511015156107765761078f565b6104605161042001526104605160200161046052610754565b610340610360525b61036051526020610360510361036052610140610360511015156107ba57610797565b6104008051602001806103008284600060045af16107d757600080fd5b5050610140610480525b61048051516020610480510161048052610480610480511015610803576107e1565b63806732896104a0526001546104c0526104c051600658016100a9565b50610520526000610580525b6105205160206001820306601f82010390506105805110151561084e57610867565b610580516105400152610580516020016105805261082c565b610460610480525b61048051526020610480510361048052610140610480511015156108925761086f565b6105208051602001806105a08284600060045af16108af57600080fd5b505060a061062052610620516106605261014080516020018061062051610660018284600060045af16108e157600080fd5b505061062051610660015160206001820306601f82010390506106006106205161066001516040818352015b826106005110151561091e5761093f565b600061060051610620516106800101535b815160010180835281141561090d575b505050602061062051610660015160206001820306601f82010390506106205101016106205261062051610680526101c080516020018061062051610660018284600060045af161098f57600080fd5b505061062051610660015160206001820306601f82010390506106006106205161066001516020818352015b82610600511015156109cc576109ed565b600061060051610620516106800101535b81516001018083528114156109bb575b505050602061062051610660015160206001820306601f820103905061062051010161062052610620516106a05261030080516020018061062051610660018284600060045af1610a3d57600080fd5b505061062051610660015160206001820306601f82010390506106006106205161066001516020818352015b8261060051101515610a7a57610a9b565b600061060051610620516106800101535b8151600101808352811415610a69575b505050602061062051610660015160206001820306601f820103905061062051010161062052610620516106c05261022080516020018061062051610660018284600060045af1610aeb57600080fd5b505061062051610660015160206001820306601f82010390506106006106205161066001516060818352015b8261060051101515610b2857610b49565b600061060051610620516106800101535b8151600101808352811415610b17575b505050602061062051610660015160206001820306601f820103905061062051010161062052610620516106e0526105a080516020018061062051610660018284600060045af1610b9957600080fd5b505061062051610660015160206001820306601f82010390506106006106205161066001516020818352015b8261060051101515610bd657610bf7565b600061060051610620516106800101535b8151600101808352811415610bc5575b505050602061062051610660015160206001820306601f8201039050610620510101610620527f649bbc62d0e31342afea4e5cd82d4049e7e1ee912fc0889aa790803be39038c561062051610660a160006107005260006101406030806020846107c001018260208501600060045af150508051820191505060006010602082066107400160208284011115610c8c57600080fd5b60208061076082610700600060045af15050818152809050905090506010806020846107c001018260208501600060045af1505080518201915050806107c0526107c09050602060c0825160208401600060025af1610cea57600080fd5b60c0519050610720526000600060406020820661086001610220518284011115610d1357600080fd5b6060806108808260206020880688030161022001600060045af1505081815280905090509050602060c0825160208401600060025af1610d5257600080fd5b60c0519050602082610a600101526020810190506000604060206020820661092001610220518284011115610d8657600080fd5b6060806109408260206020880688030161022001600060045af15050818152809050905090506020806020846109e001018260208501600060045af1505080518201915050610700516020826109e0010152602081019050806109e0526109e09050602060c0825160208401600060025af1610e0157600080fd5b60c0519050602082610a6001015260208101905080610a6052610a609050602060c0825160208401600060025af1610e3857600080fd5b60c0519050610840526000600061072051602082610b000101526020810190506101c0602080602084610b0001018260208501600060045af150508051820191505080610b0052610b009050602060c0825160208401600060025af1610e9d57600080fd5b60c0519050602082610c800101526020810190506000610300600880602084610c0001018260208501600060045af15050805182019150506000601860208206610b800160208284011115610ef157600080fd5b602080610ba082610700600060045af1505081815280905090509050601880602084610c0001018260208501600060045af150508051820191505061084051602082610c0001015260208101905080610c0052610c009050602060c0825160208401600060025af1610f6257600080fd5b60c0519050602082610c8001015260208101905080610c8052610c809050602060c0825160208401600060025af1610f9957600080fd5b60c0519050610ae052606435610ae05114610fb357600080fd5b6001805460018254011015610fc757600080fd5b6001815401815550600154610d0052610d2060006020818352015b60016001610d005116141561101757610ae051610d20516020811061100657600080fd5b600060c052602060c02001556110ab565b6000610d20516020811061102a57600080fd5b600060c052602060c0200154602082610d40010152602081019050610ae051602082610d4001015260208101905080610d4052610d409050602060c0825160208401600060025af161107b57600080fd5b60c0519050610ae052610d00600261109257600080fd5b60028151048152505b8151600101808352811415610fe2575b5050005b5b60006000fd5b61017f6112350361017f60003961017f611235036000f3
   ```
 * Runtime bytecode:
   ```
   0x600436101561000d576110b0565b600035601c52740100000000000000000000000000000000000000006020526f7fffffffffffffffffffffffffffffff6040527fffffffffffffffffffffffffffffffff8000000000000000000000000000000060605274012a05f1fffffffffffffffffffffffffdabf41c006080527ffffffffffffffffffffffffed5fa0e000000000000000000000000000000000060a05260001561027f575b6101605261014052600061018052610140516101a0526101c060006008818352015b61018051600860008112156100e8578060000360020a82046100ef565b8060020a82025b905090506101805260ff6101a051166101e052610180516101e0516101805101101561011a57600080fd5b6101e0516101805101610180526101a0517ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff86000811215610163578060000360020a820461016a565b8060020a82025b905090506101a0525b81516001018083528114156100cb575b5050601860086020820661020001602082840111156101a157600080fd5b60208061022082610180600060045af15050818152809050905090508051602001806102c08284600060045af16101d757600080fd5b50506102c05160206001820306601f82010390506103206102c0516020818352015b826103205110151561020a57610226565b6000610320516102e001535b81516001018083528114156101f9575b50505060206102a05260406102c0510160206001820306601f8201039050610280525b60006102805111151561025b57610277565b602061028051036102a001516020610280510361028052610249565b610160515650005b63c5f2892f600051141561050e57341561029857600080fd5b6000610140526101405161016052600154610180526101a060006020818352015b600160016101805116141561033a5760006101a051602081106102db57600080fd5b600060c052602060c02001546020826102400101526020810190506101605160208261024001015260208101905080610240526102409050602060c0825160208401600060025af161032c57600080fd5b60c0519050610160526103a8565b6000610160516020826101c00101526020810190506101a0516020811061036057600080fd5b600260c052602060c02001546020826101c0010152602081019050806101c0526101c09050602060c0825160208401600060025af161039e57600080fd5b60c0519050610160525b61018060026103b657600080fd5b60028151048152505b81516001018083528114156102b9575b505060006101605160208261046001015260208101905061014051610160516101805163806732896102e0526001546103005261030051600658016100a9565b506103605260006103c0525b6103605160206001820306601f82010390506103c05110151561043d57610456565b6103c05161038001526103c0516020016103c05261041b565b61018052610160526101405261036060088060208461046001018260208501600060045af150508051820191505060006018602082066103e001602082840111156104a057600080fd5b60208061040082610140600060045af150508181528090509050905060188060208461046001018260208501600060045af150508051820191505080610460526104609050602060c0825160208401600060025af16104fe57600080fd5b60c051905060005260206000f350005b63621fd130600051141561061c57341561052757600080fd5b6380673289610140526001546101605261016051600658016100a9565b506101c0526000610220525b6101c05160206001820306601f8201039050610220511015156105725761058b565b610220516101e001526102205160200161022052610550565b6101c08051602001806102808284600060045af16105a857600080fd5b50506102805160206001820306601f82010390506102e0610280516020818352015b826102e0511015156105db576105f7565b60006102e0516102a001535b81516001018083528114156105ca575b5050506020610260526040610280510160206001820306601f8201039050610260f350005b632289511860005114156110af57605060043560040161014037603060043560040135111561064a57600080fd5b60406024356004016101c037602060243560040135111561066a57600080fd5b608060443560040161022037606060443560040135111561068a57600080fd5b63ffffffff6001541061069c57600080fd5b633b9aca006102e0526102e0516106b257600080fd5b6102e05134046102c052633b9aca006102c05110156106d057600080fd5b603061014051146106e057600080fd5b60206101c051146106f057600080fd5b6060610220511461070057600080fd5b610140610360525b6103605151602061036051016103605261036061036051101561072a57610708565b6380673289610380526102c0516103a0526103a051600658016100a9565b50610400526000610460525b6104005160206001820306601f8201039050610460511015156107765761078f565b6104605161042001526104605160200161046052610754565b610340610360525b61036051526020610360510361036052610140610360511015156107ba57610797565b6104008051602001806103008284600060045af16107d757600080fd5b5050610140610480525b61048051516020610480510161048052610480610480511015610803576107e1565b63806732896104a0526001546104c0526104c051600658016100a9565b50610520526000610580525b6105205160206001820306601f82010390506105805110151561084e57610867565b610580516105400152610580516020016105805261082c565b610460610480525b61048051526020610480510361048052610140610480511015156108925761086f565b6105208051602001806105a08284600060045af16108af57600080fd5b505060a061062052610620516106605261014080516020018061062051610660018284600060045af16108e157600080fd5b505061062051610660015160206001820306601f82010390506106006106205161066001516040818352015b826106005110151561091e5761093f565b600061060051610620516106800101535b815160010180835281141561090d575b505050602061062051610660015160206001820306601f82010390506106205101016106205261062051610680526101c080516020018061062051610660018284600060045af161098f57600080fd5b505061062051610660015160206001820306601f82010390506106006106205161066001516020818352015b82610600511015156109cc576109ed565b600061060051610620516106800101535b81516001018083528114156109bb575b505050602061062051610660015160206001820306601f820103905061062051010161062052610620516106a05261030080516020018061062051610660018284600060045af1610a3d57600080fd5b505061062051610660015160206001820306601f82010390506106006106205161066001516020818352015b8261060051101515610a7a57610a9b565b600061060051610620516106800101535b8151600101808352811415610a69575b505050602061062051610660015160206001820306601f820103905061062051010161062052610620516106c05261022080516020018061062051610660018284600060045af1610aeb57600080fd5b505061062051610660015160206001820306601f82010390506106006106205161066001516060818352015b8261060051101515610b2857610b49565b600061060051610620516106800101535b8151600101808352811415610b17575b505050602061062051610660015160206001820306601f820103905061062051010161062052610620516106e0526105a080516020018061062051610660018284600060045af1610b9957600080fd5b505061062051610660015160206001820306601f82010390506106006106205161066001516020818352015b8261060051101515610bd657610bf7565b600061060051610620516106800101535b8151600101808352811415610bc5575b505050602061062051610660015160206001820306601f8201039050610620510101610620527f649bbc62d0e31342afea4e5cd82d4049e7e1ee912fc0889aa790803be39038c561062051610660a160006107005260006101406030806020846107c001018260208501600060045af150508051820191505060006010602082066107400160208284011115610c8c57600080fd5b60208061076082610700600060045af15050818152809050905090506010806020846107c001018260208501600060045af1505080518201915050806107c0526107c09050602060c0825160208401600060025af1610cea57600080fd5b60c0519050610720526000600060406020820661086001610220518284011115610d1357600080fd5b6060806108808260206020880688030161022001600060045af1505081815280905090509050602060c0825160208401600060025af1610d5257600080fd5b60c0519050602082610a600101526020810190506000604060206020820661092001610220518284011115610d8657600080fd5b6060806109408260206020880688030161022001600060045af15050818152809050905090506020806020846109e001018260208501600060045af1505080518201915050610700516020826109e0010152602081019050806109e0526109e09050602060c0825160208401600060025af1610e0157600080fd5b60c0519050602082610a6001015260208101905080610a6052610a609050602060c0825160208401600060025af1610e3857600080fd5b60c0519050610840526000600061072051602082610b000101526020810190506101c0602080602084610b0001018260208501600060045af150508051820191505080610b0052610b009050602060c0825160208401600060025af1610e9d57600080fd5b60c0519050602082610c800101526020810190506000610300600880602084610c0001018260208501600060045af15050805182019150506000601860208206610b800160208284011115610ef157600080fd5b602080610ba082610700600060045af1505081815280905090509050601880602084610c0001018260208501600060045af150508051820191505061084051602082610c0001015260208101905080610c0052610c009050602060c0825160208401600060025af1610f6257600080fd5b60c0519050602082610c8001015260208101905080610c8052610c809050602060c0825160208401600060025af1610f9957600080fd5b60c0519050610ae052606435610ae05114610fb357600080fd5b6001805460018254011015610fc757600080fd5b6001815401815550600154610d0052610d2060006020818352015b60016001610d005116141561101757610ae051610d20516020811061100657600080fd5b600060c052602060c02001556110ab565b6000610d20516020811061102a57600080fd5b600060c052602060c0200154602082610d40010152602081019050610ae051602082610d4001015260208101905080610d4052610d409050602060c0825160208401600060025af161107b57600080fd5b60c0519050610ae052610d00600261109257600080fd5b60028151048152505b8151600101808352811415610fe2575b5050005b5b60006000fd
   ```

***NOTE**: The contract creation bytecode must match the `"bytecode"` element of [`validator_registration.json`].*

Formal specification:
 * [`deposit-spec.ini.md`](deposit-spec.ini.md): high-level summary
 * [`deposit-spec.ini`](deposit-spec.ini): full formal specification

To prove the specifications:
```
$ make deps
$ make split-proof-tests
$ make test
```
Prerequisites:
 * Install Z3 (4.6.0): https://github.com/Z3Prover/z3/releases/tag/z3-4.6.0
 * System dependencies: https://github.com/kframework/evm-semantics#system-dependencies

## [Resources](/README.md#resources)

## [Disclaimer](/README.md#disclaimer)

[deposit contract]: <https://github.com/ethereum/eth2.0-specs/blob/v0.10.0/deposit_contract/contracts/validator_registration.vy>
[`1761-HOTFIX-v0.1.0-beta.13`]: <https://github.com/vyperlang/vyper/commits/1761-HOTFIX-v0.1.0-beta.13>
[`validator_registration.json`]: <https://github.com/ethereum/eth2.0-specs/blob/v0.10.0/deposit_contract/contracts/validator_registration.json>