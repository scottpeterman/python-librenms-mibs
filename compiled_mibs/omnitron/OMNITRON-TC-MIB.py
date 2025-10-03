# SNMP MIB module (OMNITRON-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\omnitron\OMNITRON-TC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:10 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ostOmnitronTcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 11)
)
if mibBuilder.loadTexts:
    ostOmnitronTcMib.setRevisions(
        ("2015-05-13 12:00",
         "2015-01-21 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OstAccessibiltyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )



class OstClassOfService(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



class OstClockFreq(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"


class OstCosL2cpDstAddr(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )



class OstCosNameString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class OstCosNameStringOrNone(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )



class OstCosTrustType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cosTrust", 1),
          ("cosUsePri", 2),
          ("cosUseClass", 3),
          ("cosUsePriClass", 4),
          ("cosGreenYellow", 5))
    )



class OstEgressSchedulingProfileIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class OstEgressQueueIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class OstElpsProtectType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e1plus1UniNoAps", 1),
          ("e1plus1UniAps", 2),
          ("e1plus1BiAps", 3),
          ("e1to1", 4),
          ("notAvailable", 5))
    )



class OstElpsRequestStates(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6,
              7,
              9,
              11,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("noRequest", 0),
          ("doNotRevert", 1),
          ("revertRequest", 2),
          ("exercise", 4),
          ("waitToRestore", 5),
          ("manualSwitchWorking", 6),
          ("manualSwitch", 7),
          ("signalDegrade", 9),
          ("signalFailWorking", 11),
          ("forcedSwitch", 13),
          ("signalFailProtection", 14),
          ("lockoutProtection", 15),
          ("notAvailable", 16))
    )



class OstElpsSignalStates(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nullSignal", 0),
          ("normalSignal", 1),
          ("notAvailable", 2))
    )



class OstErpsLinkState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("up", 1),
          ("down", 2))
    )



class OstErpsPortState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("forward", 1),
          ("blocked", 2))
    )



class OstErpsPortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rp0", 1),
          ("rp1", 2))
    )



class OstErpsRingStates(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("noRequest", 0),
          ("rapsNr", 1),
          ("rapsNrRb", 2),
          ("wtbRunning", 3),
          ("wtbExpires", 4),
          ("wtrRunning", 5),
          ("wtrExpires", 6),
          ("manualSwitch", 7),
          ("rapsManualSwitch", 8),
          ("rapsSignalFail", 9),
          ("localClearSignalFail", 10),
          ("localSignalFail", 11),
          ("rapsForcedSwitch", 12),
          ("forcedSwtich", 13),
          ("clear", 14))
    )



class OstErpsRingStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("initializing", 1),
          ("idle", 2),
          ("protection", 3),
          ("manualSwitch", 4),
          ("forcedSwitch", 5),
          ("pending", 6))
    )



class OstErrorString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class OstEvcNameString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class OstEvcNameStringOrNone(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )



class OstFileNameString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class OstFingerprintString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class OstFloatValue(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class OstFrameCount64(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class OstFrameSizeList(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class OstIndexIntegerNextFree(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



class OstIpPriorityList(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )



class OstIpv6Addr(TextualConvention, OctetString):
    status = "current"
    displayHint = "2x:2x:2x:2x:2x:2x:2x:2x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class OstIpAddr(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )



class OstMhfCreation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ostMHFdefault", 1),
          ("ostMHFexplicit", 2))
    )



class OstMipdMethodOfCreation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ostExplicit", 1),
          ("ostImplicitMa", 2),
          ("ostImplicitMde", 3),
          ("ostExplicitImplicitMa", 4))
    )



class OstModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("ap", 2),
          ("sp", 3))
    )



class OstModuleSingleIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(101, 9999),
    )



class OstPcpPriorityList(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )



class OstPortClockType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveIdle", 1),
          ("adaptiveAcqu", 2),
          ("adaptiveTrk1", 3),
          ("adaptiveTrk2", 4),
          ("holdOver", 5),
          ("coax", 6),
          ("internal", 7),
          ("line", 8))
    )



class OstPortList(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"


class OstPortNumber(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )



class OstPortSingleIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10101, 999999),
    )



class OstPriority(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class OstProbeNameString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class OstProfileNameString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class OstTestResultType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2),
          ("oversubscribe", 3))
    )



class OstTestStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("testNotStarted", 1),
          ("testInProcess", 2),
          ("testStopped", 3),
          ("testCompleted", 4),
          ("testInitializing", 5))
    )



class OstUnsigned64(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class OstUserNameString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class OstVlanId(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class OstVlanIdList(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 110),
    )



# MIB Managed Objects in the order of their OIDs

_Omnitron_ObjectIdentity = ObjectIdentity
omnitron = _Omnitron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342)
)
_IcAgent_ObjectIdentity = ObjectIdentity
icAgent = _IcAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNITRON-TC-MIB",
    **{"OstAccessibiltyType": OstAccessibiltyType,
       "OstClassOfService": OstClassOfService,
       "OstClockFreq": OstClockFreq,
       "OstCosL2cpDstAddr": OstCosL2cpDstAddr,
       "OstCosNameString": OstCosNameString,
       "OstCosNameStringOrNone": OstCosNameStringOrNone,
       "OstCosTrustType": OstCosTrustType,
       "OstEgressSchedulingProfileIndexType": OstEgressSchedulingProfileIndexType,
       "OstEgressQueueIndexType": OstEgressQueueIndexType,
       "OstElpsProtectType": OstElpsProtectType,
       "OstElpsRequestStates": OstElpsRequestStates,
       "OstElpsSignalStates": OstElpsSignalStates,
       "OstErpsLinkState": OstErpsLinkState,
       "OstErpsPortState": OstErpsPortState,
       "OstErpsPortType": OstErpsPortType,
       "OstErpsRingStates": OstErpsRingStates,
       "OstErpsRingStatus": OstErpsRingStatus,
       "OstErrorString": OstErrorString,
       "OstEvcNameString": OstEvcNameString,
       "OstEvcNameStringOrNone": OstEvcNameStringOrNone,
       "OstFileNameString": OstFileNameString,
       "OstFingerprintString": OstFingerprintString,
       "OstFloatValue": OstFloatValue,
       "OstFrameCount64": OstFrameCount64,
       "OstFrameSizeList": OstFrameSizeList,
       "OstIndexIntegerNextFree": OstIndexIntegerNextFree,
       "OstIpPriorityList": OstIpPriorityList,
       "OstIpv6Addr": OstIpv6Addr,
       "OstIpAddr": OstIpAddr,
       "OstMhfCreation": OstMhfCreation,
       "OstMipdMethodOfCreation": OstMipdMethodOfCreation,
       "OstModeType": OstModeType,
       "OstModuleSingleIndex": OstModuleSingleIndex,
       "OstPcpPriorityList": OstPcpPriorityList,
       "OstPortClockType": OstPortClockType,
       "OstPortList": OstPortList,
       "OstPortNumber": OstPortNumber,
       "OstPortSingleIndex": OstPortSingleIndex,
       "OstPriority": OstPriority,
       "OstProbeNameString": OstProbeNameString,
       "OstProfileNameString": OstProfileNameString,
       "OstTestResultType": OstTestResultType,
       "OstTestStatusType": OstTestStatusType,
       "OstUnsigned64": OstUnsigned64,
       "OstUserNameString": OstUserNameString,
       "OstVlanId": OstVlanId,
       "OstVlanIdList": OstVlanIdList,
       "omnitron": omnitron,
       "icAgent": icAgent,
       "ostOmnitronTcMib": ostOmnitronTcMib}
)
