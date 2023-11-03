from SDP_offer_answer import SDPOfferAnswerGenerator, setup
import asyncio

async def main():
    sdp_gen = SDPOfferAnswerGenerator()
    
    # Create SDP offer
    await sdp_gen.create_offer()
    
    # Access SDP offer
    offer = sdp_gen.offer
    
    print("---------->offer -----==",offer)
    # Generate SDP answer (provide the offer as an argument)
    # answer = await sdp_gen.create_answer(offer).answer
    # print(answer)
if __name__ == '__main__':
    a=setup()
    import asyncio
    asyncio.run(main())
