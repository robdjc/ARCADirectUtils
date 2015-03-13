#!/usr/bin/env python
import sys, struct

def cleanString(inString):
  if str(inString).find('\0') >= 0:
     return str(inString)[:str(inString).find('\0')]
  else:
     return str(inString)

def formatLogonMessage(messageTuple):
  print "Logon Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "Last Seq Num........: " + cleanString(messageTuple[4])
  print "AppName.............: " + cleanString(messageTuple[5])
  print "Symbology...........: " + cleanString(messageTuple[6])
  print "MVPPair1a...........: " + cleanString(messageTuple[7])
  print "MVPPair1b...........: " + cleanString(messageTuple[8])
  print "MVPPair2a...........: " + cleanString(messageTuple[9])
  print "MVPPair2b...........: " + cleanString(messageTuple[10])
  print "MVPPair3a...........: " + cleanString(messageTuple[11])
  print "MVPPair3b...........: " + cleanString(messageTuple[12])
  print "MVPPair4a...........: " + cleanString(messageTuple[13])
  print "MVPPair4b...........: " + cleanString(messageTuple[14])
  print "MVPPair5a...........: " + cleanString(messageTuple[15])
  print "MVPPair5b...........: " + cleanString(messageTuple[16])
  print "MVPPair6a...........: " + cleanString(messageTuple[17])
  print "MVPPair6b...........: " + cleanString(messageTuple[18])
  print "MVPPair7a...........: " + cleanString(messageTuple[19])
  print "MVPPair7b...........: " + cleanString(messageTuple[20])
  print "MVPPair8a...........: " + cleanString(messageTuple[21])
  print "MVPPair8b...........: " + cleanString(messageTuple[22])
  print "MVPPair9a...........: " + cleanString(messageTuple[23])
  print "MVPPair9b...........: " + cleanString(messageTuple[24])
  print "MVPPair10a..........: " + cleanString(messageTuple[25])
  print "MVPPair10b..........: " + cleanString(messageTuple[26])
  print "MVPPair11a..........: " + cleanString(messageTuple[27])
  print "MVPPair11b..........: " + cleanString(messageTuple[28])
  print "MVPPair12a..........: " + cleanString(messageTuple[29])
  print "MVPPair12b..........: " + cleanString(messageTuple[30])
  print "MVPPair13a..........: " + cleanString(messageTuple[31])
  print "MVPPair13b..........: " + cleanString(messageTuple[32])
  print "MVPPair14a..........: " + cleanString(messageTuple[33])
  print "MVPPair14b..........: " + cleanString(messageTuple[34])
  print "CancelOnDisconnect..: " + cleanString(messageTuple[35])
  print

def formatLogonRejectMessage(messageTuple):
  print "Logon Reject Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "Last Seq Num Srv Rec: " + cleanString(messageTuple[4])
  print "Last Seq Num Srv Snt: " + cleanString(messageTuple[5])
  print "Reject Type.........: " + cleanString(messageTuple[6])
  print "Text................: " + cleanString(messageTuple[7])
  print

def formatRejectMessage(messageTuple):
  print "Reject Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "Sending Time........: " + cleanString(messageTuple[4])
  print "Transaction Time....: " + cleanString(messageTuple[5])
  print "ClOrdId.............: " + cleanString(messageTuple[6])
  print "OrigClOrdId.........: " + cleanString(messageTuple[7])
  print "Rejected Msg Type...: " + cleanString(messageTuple[8])
  print "Text................: " + cleanString(messageTuple[9])
  print "Reject Reason.......: " + cleanString(messageTuple[10])
  print

def formatNewOrderMessage(messageTuple):
  print "New Order Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "ClientOrderId.......: " + cleanString(messageTuple[4])
  print "PcsLinkId...........: " + cleanString(messageTuple[5])
  print "OrderQuantity.......: " + cleanString(messageTuple[6])
  print "Price...............: " + cleanString(messageTuple[7])
  print "ExDestination.......: " + cleanString(messageTuple[8])
  print "PriceScale..........: " + cleanString(messageTuple[9])
  print "Symbol..............: " + cleanString(messageTuple[10])
  print "CompanyGroupId......: " + cleanString(messageTuple[11])
  print "DeliverToCompId.....: " + cleanString(messageTuple[12])
  print "SenderSubId.........: " + cleanString(messageTuple[13])
  print "ExecInst............: " + cleanString(messageTuple[14])
  print "Side................: " + cleanString(messageTuple[15])
  print "OrderType...........: " + cleanString(messageTuple[16])
  print "TimeInForce.........: " + cleanString(messageTuple[17])
  print "Rule80A.............: " + cleanString(messageTuple[18])
  print "TradingSessionId....: " + cleanString(messageTuple[19])
  print "Account.............: " + cleanString(messageTuple[20])
  print "ISO.................: " + cleanString(messageTuple[21])
  print "ExtExecInst.........: " + cleanString(messageTuple[22])
  print "ExtendedPNP.........: " + cleanString(messageTuple[23])
  print "NoSelfTrade.........: " + cleanString(messageTuple[24])
  print

def formatNewOrderVerboseMessage(messageTuple):
  print "New Order Verbose Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "ClientOrderId.......: " + cleanString(messageTuple[4])
  print "PcsLinkId...........: " + cleanString(messageTuple[5])
  print "OrderQuantity.......: " + cleanString(messageTuple[6])
  print "StrikePrice.........: " + cleanString(messageTuple[7])
  print "MinQty..............: " + cleanString(messageTuple[8])
  print "MaxFloor............: " + cleanString(messageTuple[9])
  print "DisplayRange........: " + cleanString(messageTuple[10])
  print "DiscretionOffset....: " + cleanString(messageTuple[11])
  print "PegDifference.......: " + cleanString(messageTuple[12])
  print "StopPx..............: " + cleanString(messageTuple[13])
  print "Price...............: " + cleanString(messageTuple[14])
  print "ExDestination.......: " + cleanString(messageTuple[15])
  print "UnderlyingQuantity..: " + cleanString(messageTuple[16])
  print "PutCall.............: " + cleanString(messageTuple[17])
  print "LocalOrAway.........: " + cleanString(messageTuple[18])
  print "PriceScale..........: " + cleanString(messageTuple[19])
  print "CorporateAction.....: " + cleanString(messageTuple[20])
  print "OpenClose...........: " + cleanString(messageTuple[21])
  print "Symbol..............: " + cleanString(messageTuple[22])
  print "StrikeDate..........: " + cleanString(messageTuple[23])
  print "CompanyGroupId......: " + cleanString(messageTuple[24])
  print "DeliverToCompId.....: " + cleanString(messageTuple[25])
  print "SenderSubId.........: " + cleanString(messageTuple[26])
  print "ExecInst............: " + cleanString(messageTuple[27])
  print "Side................: " + cleanString(messageTuple[28])
  print "OrderType...........: " + cleanString(messageTuple[29])
  print "TimeInForce.........: " + cleanString(messageTuple[30])
  print "Rule80A.............: " + cleanString(messageTuple[31])
  print "CustomerOrFirm......: " + cleanString(messageTuple[32])
  print "TradingSessionId....: " + cleanString(messageTuple[33])
  print "Account.............: " + cleanString(messageTuple[34])
  print "OptionalData........: " + cleanString(messageTuple[35])
  print "ClearingFirm........: " + cleanString(messageTuple[36])
  print "ClearingAccount.....: " + cleanString(messageTuple[37])
  print "ExpireTimeFlag......: " + cleanString(messageTuple[38])
  print "ExpireTime..........: " + cleanString(messageTuple[39])
  print "EffectiveTime.......: " + cleanString(messageTuple[40])
  print "DiscretionInst......: " + cleanString(messageTuple[41])
  print "ProactiveDiscInd....: " + cleanString(messageTuple[42])
  print "ProactiveIfLocked...: " + cleanString(messageTuple[43])
  print "ExecBroker..........: " + cleanString(messageTuple[44])
  print "ISO.................: " + cleanString(messageTuple[45])
  print "SymbolType..........: " + cleanString(messageTuple[46])
  print "ExtExecInst.........: " + cleanString(messageTuple[47])
  print "ExtendedPNP.........: " + cleanString(messageTuple[48])
  print "NoSelfTrade.........: " + cleanString(messageTuple[49])
  print

def formatAckMessage(messageTuple):
  print "Ack Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "Sending Time........: " + cleanString(messageTuple[4])
  print "Transaction Time....: " + cleanString(messageTuple[5])
  print "ClientOrderId.......: " + cleanString(messageTuple[6])
  print "OrderId.............: " + cleanString(messageTuple[7])
  print "Price...............: " + cleanString(messageTuple[8])
  print "PriceScale..........: " + cleanString(messageTuple[9])
  print "Liquidity Indicator.: " + cleanString(messageTuple[10])
  print

def formatOrderCancelMessage(messageTuple):
  print "Order Cancel Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "OrderId.............: " + cleanString(messageTuple[4])
  print "ClientOrderId.......: " + cleanString(messageTuple[5])
  print "StrikePrice.........: " + cleanString(messageTuple[6])
  print "UnderQty............: " + cleanString(messageTuple[7])
  print "ExDestination.......: " + cleanString(messageTuple[8])
  print "CorporateAction.....: " + cleanString(messageTuple[9])
  print "PutOrCall...........: " + cleanString(messageTuple[10])
  print "BulkCancel..........: " + cleanString(messageTuple[11])
  print "OpenOrClose.........: " + cleanString(messageTuple[12])
  print "Symbol..............: " + cleanString(messageTuple[13])
  print "StrikeDate..........: " + cleanString(messageTuple[14])
  print "Side................: " + cleanString(messageTuple[15])
  print "DeliverToCompId.....: " + cleanString(messageTuple[16])
  print "Account.............: " + cleanString(messageTuple[17])
  print

def formatCancelRequestAck(messageTuple):
  print "Cancel Request Ack Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "Sending Time........: " + cleanString(messageTuple[4])
  print "Transaction Time....: " + cleanString(messageTuple[5])
  print "ClientOrderId.......: " + cleanString(messageTuple[6])
  print "OrderId.............: " + cleanString(messageTuple[7])
  print

def formatOrderKilled(messageTuple):
  print "Order Killed Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "Sending Time........: " + cleanString(messageTuple[4])
  print "Transaction Time....: " + cleanString(messageTuple[5])
  print "ClientOrderId.......: " + cleanString(messageTuple[6])
  print "OrderId.............: " + cleanString(messageTuple[7])
  print "Information Text....: " + cleanString(messageTuple[8])
  print

def formatOrderFill(messageTuple):
  print "Order Fill Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "Sending Time........: " + cleanString(messageTuple[4])
  print "Transaction Time....: " + cleanString(messageTuple[5])
  print "ClientOrderId.......: " + cleanString(messageTuple[6])
  print "OrderId.............: " + cleanString(messageTuple[7])
  print "ExecutionId.........: " + cleanString(messageTuple[8])
  print "ArcaExId............: " + cleanString(messageTuple[9])
  print "LastShares..........: " + cleanString(messageTuple[10])
  print "LastPrice...........: " + cleanString(messageTuple[11])
  print "PriceScale..........: " + cleanString(messageTuple[12])
  print "LiquidityIndicator..: " + cleanString(messageTuple[13])
  print "Side................: " + cleanString(messageTuple[14])
  print "Last Market.........: " + cleanString(messageTuple[15])
  print

def formatorderCancelReplace(messageTuple):
  print "Order Cancel Replace Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "OrderId.............: " + cleanString(messageTuple[4])
  print "ClientOrderId.......: " + cleanString(messageTuple[5])
  print "OrigClientOrderId...: " + cleanString(messageTuple[6])
  print "OrderQuantity.......: " + cleanString(messageTuple[7])
  print "StrikePrice.........: " + cleanString(messageTuple[8])
  print "Price...............: " + cleanString(messageTuple[9])
  print "ExDestination.......: " + cleanString(messageTuple[10])
  print "UnderQty............: " + cleanString(messageTuple[11])
  print "PriceScale..........: " + cleanString(messageTuple[12])
  print "PutOrCall...........: " + cleanString(messageTuple[13])
  print "CorporateAction.....: " + cleanString(messageTuple[14])
  print "OpenOrClose.........: " + cleanString(messageTuple[15])
  print "Symbol..............: " + cleanString(messageTuple[16])
  print "StrikeDate..........: " + cleanString(messageTuple[17])
  print "ExecInst............: " + cleanString(messageTuple[18])
  print "Side................: " + cleanString(messageTuple[19])
  print "OrderType...........: " + cleanString(messageTuple[20])
  print "TimeInForce.........: " + cleanString(messageTuple[21])
  print "Rule80A.............: " + cleanString(messageTuple[22])
  print "TradingSessionId....: " + cleanString(messageTuple[23])
  print "DeliverToCompId.....: " + cleanString(messageTuple[24])
  print "Account.............: " + cleanString(messageTuple[25])
  print

def formatorderCancelReplaceVerbose(messageTuple):
  print "Order Cancel Replace Verbose Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "OrderId.............: " + cleanString(messageTuple[4])
  print "ClientOrderId.......: " + cleanString(messageTuple[5])
  print "OrigClientOrderId...: " + cleanString(messageTuple[6])
  print "OrderQuantity.......: " + cleanString(messageTuple[7])
  print "StrikePrice.........: " + cleanString(messageTuple[8])
  print "MinQty..............: " + cleanString(messageTuple[9])
  print "MaxFloor............: " + cleanString(messageTuple[10])
  print "DisplayRange........: " + cleanString(messageTuple[11])
  print "DiscretionOffset....: " + cleanString(messageTuple[12])
  print "PegDifference.......: " + cleanString(messageTuple[13])
  print "StopPx..............: " + cleanString(messageTuple[14])
  print "Price...............: " + cleanString(messageTuple[15])
  print "UnderlyingQuantity..: " + cleanString(messageTuple[16])
  print "ExDestination.......: " + cleanString(messageTuple[17])
  print "PutCall.............: " + cleanString(messageTuple[18])
  print "PriceScale..........: " + cleanString(messageTuple[19])
  print "CorporateAction.....: " + cleanString(messageTuple[20])
  print "OpenOrClose.........: " + cleanString(messageTuple[21])
  print "Symbol..............: " + cleanString(messageTuple[22])
  print "StrikeDate..........: " + cleanString(messageTuple[23])
  print "ExecInst............: " + cleanString(messageTuple[24])
  print "Side................: " + cleanString(messageTuple[25])
  print "OrderType...........: " + cleanString(messageTuple[26])
  print "TimeInForce.........: " + cleanString(messageTuple[27])
  print "Rule80A.............: " + cleanString(messageTuple[28])
  print "CustomerOrFirm......: " + cleanString(messageTuple[29])
  print "TradingSessionId....: " + cleanString(messageTuple[30])
  print "ExpireTimeFlag......: " + cleanString(messageTuple[31])
  print "ExpireTime..........: " + cleanString(messageTuple[32])
  print "EffectiveTime.......: " + cleanString(messageTuple[33])
  print "DiscretionInst......: " + cleanString(messageTuple[34])
  print "ProactiveDiscInd....: " + cleanString(messageTuple[35])
  print "DeliverToCompId.....: " + cleanString(messageTuple[36])
  print "ClearingAccount.....: " + cleanString(messageTuple[37])
  print "Account.............: " + cleanString(messageTuple[38])
  print

def formatCancelReplaceAck(messageTuple):
  print "Cancel Replace Ack Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "Sending Time........: " + cleanString(messageTuple[4])
  print "Transaction Time....: " + cleanString(messageTuple[5])
  print "ClientOrderId.......: " + cleanString(messageTuple[6])
  print "OrderId.............: " + cleanString(messageTuple[7])
  print

def formatOrderReplacedMessage(messageTuple):
  print "Order Replaced Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "Sending Time........: " + cleanString(messageTuple[4])
  print "Transaction Time....: " + cleanString(messageTuple[5])
  print "ClientOrderId.......: " + cleanString(messageTuple[6])
  print "OrderId.............: " + cleanString(messageTuple[7])
  print

def formatBustCorrectMessage(messageTuple):
  print "Bust/Correct Message"
  print "Message Type........: " + cleanString(messageTuple[0])
  print "Variant.............: " + cleanString(messageTuple[1])
  print "Length..............: " + cleanString(messageTuple[2])
  print "Seq Number..........: " + cleanString(messageTuple[3])
  print "Sending Time........: " + cleanString(messageTuple[4])
  print "Transaction Time....: " + cleanString(messageTuple[5])
  print "ClientOrderId.......: " + cleanString(messageTuple[6])
  print "ExecutionId.........: " + cleanString(messageTuple[7])
  print "OrderQuantity.......: " + cleanString(messageTuple[8])
  print "Price...............: " + cleanString(messageTuple[9])
  print "PriceScale..........: " + cleanString(messageTuple[10])
  print "Type................: " + cleanString(messageTuple[11])
  print


def main(argv):

  adMessageTypes = ['A', 'L', '1', '0', 'B', 'C', 'D', 'E', 'F', 'G', 'J', 'P', 'a', '2', '4', '5', '6', '8']
  adVariants = [1, 2, 3, 4]

  if len(argv) == 2:

    print argv[1]

    inFile = open(argv[1], "rb")
    try:

        binaryData = inFile.read(4)

        while binaryData != "":
          msgType = struct.unpack("!c", binaryData[0])[0]
          # print "DEBUG: [" + str(msgType) + "]"
          # print type(msgType)
          
          if msgType in adMessageTypes:
            msgVariant = struct.unpack("!B", binaryData[1])[0]
            # print "DEBUG: [" + str(msgVariant) + "]"
            # print type(msgVariant)
            
            if msgVariant in adVariants:
              msgLength = struct.unpack("!H", binaryData[2:4])[0]

              # print "DEBUG: [" + str(msgLength) + "]"
              # print type(msgLength)
              # print "DEBUG: Next message is " + str(msgLength) + " bytes"

              # read the rest of the message (we already read 4 bytes)
              ouchMessage = binaryData + inFile.read(msgLength - 4)
              # print len(ouchMessage)

              if msgType == 'A':
                someData = struct.unpack("!cBHLL5sBcBcBcBcBcBcBcBcBcBcBcBcBcBcBBc", ouchMessage)
                formatLogonMessage(someData)

              elif msgType == 'L':
                someData = struct.unpack("!cBHLLLH40sBc", ouchMessage)
                formatLogonRejectMessage(someData)

              elif msgType == '8': # CancelReplaceRejectAckMessage
                someData = struct.unpack("!cBHLQQLLc40scBBBBBc", ouchMessage)
                formatRejectMessage(someData)

              elif msgType == 'D' and msgVariant == 1:
                someData = struct.unpack("!cBHLLLLLHc8s5s5s5sccccc4s10sccccBBc", ouchMessage)
                formatNewOrderMessage(someData)

              elif msgType == 'D' and msgVariant == 3:
                someData = struct.unpack("!cBHLLLLLLLLLlLLHHBBccc8s8s5s5s5scccccc4s10s16s5s5sc4s4sccc5scccccBBBc", ouchMessage)
                formatNewOrderVerboseMessage(someData)

              elif msgType == 'F':
                someData = struct.unpack("!cBHLQLLHHBBBc8s8sc5s10sBBBBBBBc", ouchMessage)
                formatOrderCancelMessage(someData)

              elif msgType == 'a': # OrderAckMessage
                someData = struct.unpack("!cBHLQQLQLccBBBBBc", ouchMessage)
                formatAckMessage(someData)

              elif msgType == '6': # CancelRequestAckMessage
                someData = struct.unpack("!cBHLQQLQBBBc", ouchMessage)
                formatCancelRequestAck(someData)

              elif msgType == '4': # OrderKilledMessage
                someData = struct.unpack("!cBHLQQLQBBBc", ouchMessage)
                formatOrderKilled(someData)

              elif msgType == '2': # OrderFillMessage
                someData = struct.unpack("!cBHLQQLQQ20sLLccc2sBBBBBBBBBBc", ouchMessage)
                formatOrderFill(someData)

              elif msgType == 'G' and msgVariant == 1:
                someData = struct.unpack("!cBHLQLLLLLHHcBBc8s8sccccc4s5s10sBBBc", ouchMessage)
                formatorderCancelReplace(someData)

              elif msgType == 'G' and msgVariant == 2:
                someData = struct.unpack("!cBHLQLLLLLLLLLLLHHBcBc8s8scccccc4sc4s4scc5s5s10sBBc", ouchMessage)
                formatorderCancelReplaceVerbose(someData)

              elif msgType == 'E': # CancelReplaceAckMessage
                someData = struct.unpack("!cBHLQQLQBBBc", ouchMessage)
                formatCancelReplaceAck(someData)

              elif msgType == '5': # OrderReplacedMessage
                someData = struct.unpack("!cBHLQQLQBBBc", ouchMessage)
                formatOrderReplacedMessage(someData)

              elif msgType == 'C': # BustCorrectMessage
                someData = struct.unpack("!cBHLQQLQLLccBc", ouchMessage)
                formatBustCorrectMessage(someData)

              elif msgType == '1':
                # print "TEST REQUEST"
                pass

              elif msgType == '0':
                # print "HEARTBEAT"
                pass

              else:
                print "Unknown Message - needs to be added to the script"

          # read the next byte to see if it's arca data or 
          binaryData = inFile.read(1)
          if binaryData != "":
            msgType = struct.unpack("!c", binaryData[0])[0]
            # print "DEBUG: [" + str(msgType) + "]"
            # print type(msgType)
            
            if msgType in adMessageTypes:
               binaryData = binaryData + inFile.read(3)
            else:
               # print "junk data"
               pass
          

    finally:
        inFile.close()

    
  else:
    print "Please enter a filename on the cmd line"

if (__name__ == "__main__"):
  main(sys.argv)
