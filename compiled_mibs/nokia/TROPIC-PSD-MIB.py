# SNMP MIB module (TROPIC-PSD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-PSD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:47 2025
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

(Dot1agCfmCcmInterval,
 Dot1agCfmMepIdOrZero,
 dot1agCfmMepEntry) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmCcmInterval",
    "Dot1agCfmMepIdOrZero",
    "dot1agCfmMepEntry")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnLagCommandEntry,) = mibBuilder.importSymbols(
    "TN-LAG-MIB",
    "tnLagCommandEntry")

(tnOamPingCtlEntry,) = mibBuilder.importSymbols(
    "TN-OAM-TEST-MIB",
    "tnOamPingCtlEntry")

(AluWdmPmonPolicyType,) = mibBuilder.importSymbols(
    "TN-PMON-MIB",
    "AluWdmPmonPolicyType")

(TmnxEnabledDisabled,
 TnSwitchID) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TmnxEnabledDisabled",
    "TnSwitchID")

(tnGenericTrapCategory,
 tnGenericTrapConfigurationChangeCounter,
 tnGenericTrapData,
 tnGenericTrapDateAndTime,
 tnGenericTrapDescr,
 tnGenericTrapObject,
 tnGenericTrapObjectCounter32Val,
 tnGenericTrapObjectCounter64Val,
 tnGenericTrapObjectInstance,
 tnGenericTrapObjectInteger32Val,
 tnGenericTrapObjectIpAddressVal,
 tnGenericTrapObjectOctetStringVal,
 tnGenericTrapObjectOidVal,
 tnGenericTrapObjectTimeTicksVal,
 tnGenericTrapObjectUnsigned32Val,
 tnGenericTrapObjectValueType,
 tnGenericTrapSeqNumber,
 tnGenericTrapTime) = mibBuilder.importSymbols(
    "TROPIC-GENERIC-NOTIFICATION-MIB",
    "tnGenericTrapCategory",
    "tnGenericTrapConfigurationChangeCounter",
    "tnGenericTrapData",
    "tnGenericTrapDateAndTime",
    "tnGenericTrapDescr",
    "tnGenericTrapObject",
    "tnGenericTrapObjectCounter32Val",
    "tnGenericTrapObjectCounter64Val",
    "tnGenericTrapObjectInstance",
    "tnGenericTrapObjectInteger32Val",
    "tnGenericTrapObjectIpAddressVal",
    "tnGenericTrapObjectOctetStringVal",
    "tnGenericTrapObjectOidVal",
    "tnGenericTrapObjectTimeTicksVal",
    "tnGenericTrapObjectUnsigned32Val",
    "tnGenericTrapObjectValueType",
    "tnGenericTrapSeqNumber",
    "tnGenericTrapTime")

(tnPsdMIB,
 tnPsdModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnPsdMIB",
    "tnPsdModules")

(tnNetIfEntry,
 tnNetIfIndex) = mibBuilder.importSymbols(
    "TROPIC-L1SERVICE-MIB",
    "tnNetIfEntry",
    "tnNetIfIndex")

(tnOthIfIndex,
 tnOthIfIndexLo,
 tnOthOdukNimEntry,
 tnOthOdukTEntry,
 tnOthOdukTtpEntry) = mibBuilder.importSymbols(
    "TROPIC-OTH-MIB",
    "tnOthIfIndex",
    "tnOthIfIndexLo",
    "tnOthOdukNimEntry",
    "tnOthOdukTEntry",
    "tnOthOdukTtpEntry")

(tnOtukEntry,) = mibBuilder.importSymbols(
    "TROPIC-OTUODU-MIB",
    "tnOtukEntry")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(tnStatsInterval,) = mibBuilder.importSymbols(
    "TROPIC-STATISTICS-MIB",
    "tnStatsInterval")

(AluWdmTypeOfNetIfOperation,
 TnCommand,
 TnCondition,
 TnSfpType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmTypeOfNetIfOperation",
    "TnCommand",
    "TnCondition",
    "TnSfpType")


# MODULE-IDENTITY

tnPsdMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    tnPsdMibModule.setRevisions(
        ("2023-01-04 00:00",
         "2022-12-22 00:00",
         "2022-10-23 00:00",
         "2022-10-12 00:00",
         "2021-08-11 00:00",
         "2021-06-10 00:00",
         "2020-09-29 12:00",
         "2020-02-25 12:00",
         "2018-04-30 12:00",
         "2018-03-19 12:00",
         "2018-02-23 12:00",
         "2018-02-14 12:00",
         "2017-09-25 12:00",
         "2017-08-18 12:00",
         "2017-07-07 12:00",
         "2017-04-10 12:00",
         "2017-03-06 12:00",
         "2017-02-06 12:00",
         "2016-12-21 12:00",
         "2016-10-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TropicPsdAsapIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicPsdAvailabilityStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )



class TropicPsdCardCLEICode(TextualConvention, OctetString):
    status = "current"
    displayHint = "10a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )



class TropicPsdCardCompanyIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicPsdCardCustomerInvField(TextualConvention, OctetString):
    status = "current"
    displayHint = "44a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )



class TropicPsdCardDate(TextualConvention, OctetString):
    status = "current"
    displayHint = "6a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )



class TropicPsdCardFactoryIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicPsdCardMnemonic(TextualConvention, OctetString):
    status = "current"
    displayHint = "8a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class TropicPsdCardPartNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "14a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )



class TropicPsdCardSerialNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "18a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )



class TropicPsdDdmDataType(TextualConvention, Integer32):
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
        *(("ddmVoltage", 1),
          ("ddmTemperature", 2),
          ("ddmLaserBiasCurrent", 3),
          ("ddmTransmittedPower", 4),
          ("ddmReceivedPower", 5))
    )



class TropicPsdDapi(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class TropicPsdFaultAlarmTime(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class TropicPsdFaultLocationType(TextualConvention, Integer32):
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("faultLocUnknown", 0),
          ("faultLocShelf", 1),
          ("faultLocSlot", 2),
          ("faultLocSystem", 3),
          ("faultLocIntfDP", 4),
          ("faultLocIntfMP", 5),
          ("faultLocOtuk", 7),
          ("faultLocOdukT", 8),
          ("faultLocOdukPm", 9),
          ("faultLocOdukP", 10),
          ("faultLocNetIf", 11),
          ("faultLocIntfDPN", 12),
          ("faultLocIntfDPC", 13),
          ("faultLocAps", 14),
          ("faultLocSlm", 15),
          ("faultLocDm", 16),
          ("faultLocMep", 17),
          ("faultLocLag", 18),
          ("faultLocLogIntfDP", 19),
          ("faultLocLogIntfDPC", 20),
          ("faultLocLogIntfDPN", 21),
          ("faultLocOdukPmC", 22),
          ("faultLocOtukC", 23),
          ("faultLocPowerInput", 24))
    )



class TropicPsdFaultSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7,
              12)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("notAlarmed", 7),
          ("warning", 12))
    )



class TropicPsdIsdId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isd0", 1),
          ("isd1", 2))
    )



class TropicPsdIsdStatus(TextualConvention, Integer32):
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
        *(("isdActive", 1),
          ("isdInactive", 2),
          ("isdError", 3),
          ("isdSoak", 4))
    )



class TropicPsdNetIfIndexOrZero(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )



class TropicPsdNtpServerIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicPsdPriorityValue(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class TropicPsdRestartType(TextualConvention, Integer32):
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
        *(("noCmd", 1),
          ("warm", 2),
          ("cold", 3))
    )



class TropicPsdSapi(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class TropicPsdSfpAluPartNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "12a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



class TropicPsdSfpAluSerialNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "18a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )



class TropicPsdSfpBitRate(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1



class TropicPsdSfpCLEICode(TextualConvention, OctetString):
    status = "current"
    displayHint = "10a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )



class TropicPsdSfpConnectorType(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1



class TropicPsdSfpIcs(TextualConvention, OctetString):
    status = "current"
    displayHint = "6a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )



class TropicPsdSfpIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2



class TropicPsdSfpLinkLength(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5



class TropicPsdSfpNokiaPartNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "12a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



class TropicPsdSfpPartNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TropicPsdSfpRevisionNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicPsdSfpTransceiverCode(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class TropicPsdSfpVendorDate(TextualConvention, OctetString):
    status = "current"
    displayHint = "8a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class TropicPsdSfpVendorName(TextualConvention, OctetString):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TropicPsdSfpVendorOUI(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



class TropicPsdSfpVendorSerialNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TropicPsdSfpVendorSpecific(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32



class TropicPsdSfpWavelength(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"


class TropicPsdShelfRealTimePower(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"


class TropicPsdSnmpPortNumberType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicPsdSystemMode(TextualConvention, Integer32):
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("factoryDefault", 1),
          ("otnNid1GbeClientOtu1NetworkMode", 2),
          ("otnNid1GbeClientOtu2NetworkMode", 3),
          ("otnNid10GbeClientOtu2NetworkMode", 4),
          ("otnNid10GbeClientOtu2eNetworkMode", 5),
          ("otnNidOtu1ClientOtu1NetworkMode", 6),
          ("otnNidOtu2ClientOtu2NetworkMode", 7),
          ("otnNidOtu2eClientOtu2eNetworkMode", 8),
          ("ethNid1GbEor10GbEClient10GbENetworkMode", 9),
          ("otnNid1GbEor10GbEClientOtu2OduFlexNetworkMode", 10),
          ("otnNid2x1GbEor10GbEClientOtu2OduFlexNetworkMode", 11))
    )



class TropicPsdTransportIdentifier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TropicPsdVlanId(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_TnPsdSystem_ObjectIdentity = ObjectIdentity
tnPsdSystem = _TnPsdSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1)
)
_TnPsdSystemObjects_ObjectIdentity = ObjectIdentity
tnPsdSystemObjects = _TnPsdSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 1)
)
_TnPsdSystemMode_Type = TropicPsdSystemMode
_TnPsdSystemMode_Object = MibScalar
tnPsdSystemMode = _TnPsdSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 1, 1),
    _TnPsdSystemMode_Type()
)
tnPsdSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdSystemMode.setStatus("current")
_TnPsdSystemModeDescr_Type = SnmpAdminString
_TnPsdSystemModeDescr_Object = MibScalar
tnPsdSystemModeDescr = _TnPsdSystemModeDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 1, 2),
    _TnPsdSystemModeDescr_Type()
)
tnPsdSystemModeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSystemModeDescr.setStatus("current")
_TnPsdSystemAbnormalState_Type = TruthValue
_TnPsdSystemAbnormalState_Object = MibScalar
tnPsdSystemAbnormalState = _TnPsdSystemAbnormalState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 1, 3),
    _TnPsdSystemAbnormalState_Type()
)
tnPsdSystemAbnormalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSystemAbnormalState.setStatus("current")


class _TnPsdSystemSmartConnectLed_Type(Integer32):
    """Custom type tnPsdSystemSmartConnectLed based on Integer32"""
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
        *(("off", 1),
          ("blue", 2),
          ("blueBlink1Hz", 3),
          ("blueBlink5Hz", 4))
    )


_TnPsdSystemSmartConnectLed_Type.__name__ = "Integer32"
_TnPsdSystemSmartConnectLed_Object = MibScalar
tnPsdSystemSmartConnectLed = _TnPsdSystemSmartConnectLed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 1, 4),
    _TnPsdSystemSmartConnectLed_Type()
)
tnPsdSystemSmartConnectLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdSystemSmartConnectLed.setStatus("current")
_TnPsdSystemConformance_ObjectIdentity = ObjectIdentity
tnPsdSystemConformance = _TnPsdSystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 2)
)
_TnPsdSystemGroups_ObjectIdentity = ObjectIdentity
tnPsdSystemGroups = _TnPsdSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 2, 2)
)
_TnPsdEquipment_ObjectIdentity = ObjectIdentity
tnPsdEquipment = _TnPsdEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2)
)
_TnPsdEquipmentNotifs_ObjectIdentity = ObjectIdentity
tnPsdEquipmentNotifs = _TnPsdEquipmentNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 0)
)
_TnPsdEquipmentObjects_ObjectIdentity = ObjectIdentity
tnPsdEquipmentObjects = _TnPsdEquipmentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1)
)
_TnPsdShelfTable_Object = MibTable
tnPsdShelfTable = _TnPsdShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnPsdShelfTable.setStatus("current")
_TnPsdShelfEntry_Object = MibTableRow
tnPsdShelfEntry = _TnPsdShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1)
)
tnPsdShelfEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
)
if mibBuilder.loadTexts:
    tnPsdShelfEntry.setStatus("current")


class _TnPsdShelfName_Type(SnmpAdminString):
    """Custom type tnPsdShelfName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPsdShelfName_Type.__name__ = "SnmpAdminString"
_TnPsdShelfName_Object = MibTableColumn
tnPsdShelfName = _TnPsdShelfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 1),
    _TnPsdShelfName_Type()
)
tnPsdShelfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdShelfName.setStatus("current")


class _TnPsdShelfDescr_Type(SnmpAdminString):
    """Custom type tnPsdShelfDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnPsdShelfDescr_Type.__name__ = "SnmpAdminString"
_TnPsdShelfDescr_Object = MibTableColumn
tnPsdShelfDescr = _TnPsdShelfDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 2),
    _TnPsdShelfDescr_Type()
)
tnPsdShelfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdShelfDescr.setStatus("current")
_TnPsdShelfType_Type = ObjectIdentifier
_TnPsdShelfType_Object = MibTableColumn
tnPsdShelfType = _TnPsdShelfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 3),
    _TnPsdShelfType_Type()
)
tnPsdShelfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdShelfType.setStatus("current")


class _TnPsdShelfLocation_Type(SnmpAdminString):
    """Custom type tnPsdShelfLocation based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPsdShelfLocation_Type.__name__ = "SnmpAdminString"
_TnPsdShelfLocation_Object = MibTableColumn
tnPsdShelfLocation = _TnPsdShelfLocation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 4),
    _TnPsdShelfLocation_Type()
)
tnPsdShelfLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdShelfLocation.setStatus("current")


class _TnPsdShelfLatitude_Type(SnmpAdminString):
    """Custom type tnPsdShelfLatitude based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPsdShelfLatitude_Type.__name__ = "SnmpAdminString"
_TnPsdShelfLatitude_Object = MibTableColumn
tnPsdShelfLatitude = _TnPsdShelfLatitude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 5),
    _TnPsdShelfLatitude_Type()
)
tnPsdShelfLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdShelfLatitude.setStatus("current")


class _TnPsdShelfLongitude_Type(SnmpAdminString):
    """Custom type tnPsdShelfLongitude based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPsdShelfLongitude_Type.__name__ = "SnmpAdminString"
_TnPsdShelfLongitude_Object = MibTableColumn
tnPsdShelfLongitude = _TnPsdShelfLongitude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 6),
    _TnPsdShelfLongitude_Type()
)
tnPsdShelfLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdShelfLongitude.setStatus("current")


class _TnPsdShelfAltitude_Type(SnmpAdminString):
    """Custom type tnPsdShelfAltitude based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPsdShelfAltitude_Type.__name__ = "SnmpAdminString"
_TnPsdShelfAltitude_Object = MibTableColumn
tnPsdShelfAltitude = _TnPsdShelfAltitude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 7),
    _TnPsdShelfAltitude_Type()
)
tnPsdShelfAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdShelfAltitude.setStatus("current")
_TnPsdShelfRealTimePower_Type = TropicPsdShelfRealTimePower
_TnPsdShelfRealTimePower_Object = MibTableColumn
tnPsdShelfRealTimePower = _TnPsdShelfRealTimePower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 8),
    _TnPsdShelfRealTimePower_Type()
)
tnPsdShelfRealTimePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdShelfRealTimePower.setStatus("current")
_TnPsdSlotTable_Object = MibTable
tnPsdSlotTable = _TnPsdSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnPsdSlotTable.setStatus("current")
_TnPsdSlotEntry_Object = MibTableRow
tnPsdSlotEntry = _TnPsdSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 2, 1)
)
tnPsdSlotEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPsdSlotEntry.setStatus("current")
_TnPsdSlotType_Type = ObjectIdentifier
_TnPsdSlotType_Object = MibTableColumn
tnPsdSlotType = _TnPsdSlotType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 2, 1, 1),
    _TnPsdSlotType_Type()
)
tnPsdSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSlotType.setStatus("current")
_TnPsdCardTable_Object = MibTable
tnPsdCardTable = _TnPsdCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnPsdCardTable.setStatus("current")
_TnPsdCardEntry_Object = MibTableRow
tnPsdCardEntry = _TnPsdCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1)
)
tnPsdCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPsdCardEntry.setStatus("current")
_TnPsdCardInvStatus_Type = TropicPsdAvailabilityStatus
_TnPsdCardInvStatus_Object = MibTableColumn
tnPsdCardInvStatus = _TnPsdCardInvStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 1),
    _TnPsdCardInvStatus_Type()
)
tnPsdCardInvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdCardInvStatus.setStatus("current")
_TnPsdCardCompanyID_Type = TropicPsdCardCompanyIdentifier
_TnPsdCardCompanyID_Object = MibTableColumn
tnPsdCardCompanyID = _TnPsdCardCompanyID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 2),
    _TnPsdCardCompanyID_Type()
)
tnPsdCardCompanyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdCardCompanyID.setStatus("current")
_TnPsdCardMnemonic_Type = TropicPsdCardMnemonic
_TnPsdCardMnemonic_Object = MibTableColumn
tnPsdCardMnemonic = _TnPsdCardMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 3),
    _TnPsdCardMnemonic_Type()
)
tnPsdCardMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdCardMnemonic.setStatus("current")
_TnPsdCardCLEI_Type = TropicPsdCardCLEICode
_TnPsdCardCLEI_Object = MibTableColumn
tnPsdCardCLEI = _TnPsdCardCLEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 4),
    _TnPsdCardCLEI_Type()
)
tnPsdCardCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdCardCLEI.setStatus("current")
_TnPsdCardUnitPartNumber_Type = TropicPsdCardPartNumber
_TnPsdCardUnitPartNumber_Object = MibTableColumn
tnPsdCardUnitPartNumber = _TnPsdCardUnitPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 5),
    _TnPsdCardUnitPartNumber_Type()
)
tnPsdCardUnitPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdCardUnitPartNumber.setStatus("current")
_TnPsdCardSwPartNumber_Type = TropicPsdCardPartNumber
_TnPsdCardSwPartNumber_Object = MibTableColumn
tnPsdCardSwPartNumber = _TnPsdCardSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 6),
    _TnPsdCardSwPartNumber_Type()
)
tnPsdCardSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdCardSwPartNumber.setStatus("current")
_TnPsdCardFactoryID_Type = TropicPsdCardFactoryIdentifier
_TnPsdCardFactoryID_Object = MibTableColumn
tnPsdCardFactoryID = _TnPsdCardFactoryID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 7),
    _TnPsdCardFactoryID_Type()
)
tnPsdCardFactoryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdCardFactoryID.setStatus("current")
_TnPsdCardSerialNumber_Type = TropicPsdCardSerialNumber
_TnPsdCardSerialNumber_Object = MibTableColumn
tnPsdCardSerialNumber = _TnPsdCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 8),
    _TnPsdCardSerialNumber_Type()
)
tnPsdCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdCardSerialNumber.setStatus("current")
_TnPsdCardDate_Type = TropicPsdCardDate
_TnPsdCardDate_Object = MibTableColumn
tnPsdCardDate = _TnPsdCardDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 9),
    _TnPsdCardDate_Type()
)
tnPsdCardDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdCardDate.setStatus("current")
_TnPsdCardCustInvField_Type = TropicPsdCardCustomerInvField
_TnPsdCardCustInvField_Object = MibTableColumn
tnPsdCardCustInvField = _TnPsdCardCustInvField_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 10),
    _TnPsdCardCustInvField_Type()
)
tnPsdCardCustInvField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdCardCustInvField.setStatus("current")
_TnPsdShelfRestartTable_Object = MibTable
tnPsdShelfRestartTable = _TnPsdShelfRestartTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnPsdShelfRestartTable.setStatus("current")
_TnPsdShelfRestartEntry_Object = MibTableRow
tnPsdShelfRestartEntry = _TnPsdShelfRestartEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 6, 1)
)
tnPsdShelfRestartEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
)
if mibBuilder.loadTexts:
    tnPsdShelfRestartEntry.setStatus("current")


class _TnPsdShelfRestart_Type(TropicPsdRestartType):
    """Custom type tnPsdShelfRestart based on TropicPsdRestartType"""
    defaultValue = 1


_TnPsdShelfRestart_Type.__name__ = "TropicPsdRestartType"
_TnPsdShelfRestart_Object = MibTableColumn
tnPsdShelfRestart = _TnPsdShelfRestart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 6, 1, 1),
    _TnPsdShelfRestart_Type()
)
tnPsdShelfRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdShelfRestart.setStatus("current")
_TnPsdEquipmentConformance_ObjectIdentity = ObjectIdentity
tnPsdEquipmentConformance = _TnPsdEquipmentConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2)
)
_TnPsdEquipmentGroups_ObjectIdentity = ObjectIdentity
tnPsdEquipmentGroups = _TnPsdEquipmentGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2, 2)
)
_TnPsdInterface_ObjectIdentity = ObjectIdentity
tnPsdInterface = _TnPsdInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3)
)
_TnPsdInterfaceNotifs_ObjectIdentity = ObjectIdentity
tnPsdInterfaceNotifs = _TnPsdInterfaceNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 0)
)
_TnPsdInterfaceObjects_ObjectIdentity = ObjectIdentity
tnPsdInterfaceObjects = _TnPsdInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1)
)
_TnPsdSfpConfigTable_Object = MibTable
tnPsdSfpConfigTable = _TnPsdSfpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tnPsdSfpConfigTable.setStatus("current")
_TnPsdSfpConfigEntry_Object = MibTableRow
tnPsdSfpConfigEntry = _TnPsdSfpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 1, 1)
)
tnPsdSfpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPsdSfpConfigEntry.setStatus("current")
_TnPsdSfpType_Type = TnSfpType
_TnPsdSfpType_Object = MibTableColumn
tnPsdSfpType = _TnPsdSfpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 1, 1, 1),
    _TnPsdSfpType_Type()
)
tnPsdSfpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdSfpType.setStatus("current")
_TnPsdSfpProgrammedChannel_Type = Unsigned32
_TnPsdSfpProgrammedChannel_Object = MibTableColumn
tnPsdSfpProgrammedChannel = _TnPsdSfpProgrammedChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 1, 1, 2),
    _TnPsdSfpProgrammedChannel_Type()
)
tnPsdSfpProgrammedChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdSfpProgrammedChannel.setStatus("current")
_TnPsdSfpInfoTable_Object = MibTable
tnPsdSfpInfoTable = _TnPsdSfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3)
)
if mibBuilder.loadTexts:
    tnPsdSfpInfoTable.setStatus("current")
_TnPsdSfpInfoEntry_Object = MibTableRow
tnPsdSfpInfoEntry = _TnPsdSfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1)
)
tnPsdSfpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPsdSfpInfoEntry.setStatus("current")
_TnPsdSfpInfoInvStatus_Type = TropicPsdAvailabilityStatus
_TnPsdSfpInfoInvStatus_Object = MibTableColumn
tnPsdSfpInfoInvStatus = _TnPsdSfpInfoInvStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 1),
    _TnPsdSfpInfoInvStatus_Type()
)
tnPsdSfpInfoInvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoInvStatus.setStatus("current")
_TnPsdSfpInfoPhysicalIdentifier_Type = TropicPsdSfpIdentifier
_TnPsdSfpInfoPhysicalIdentifier_Object = MibTableColumn
tnPsdSfpInfoPhysicalIdentifier = _TnPsdSfpInfoPhysicalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 2),
    _TnPsdSfpInfoPhysicalIdentifier_Type()
)
tnPsdSfpInfoPhysicalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoPhysicalIdentifier.setStatus("current")


class _TnPsdSfpInfoClassOfWdm_Type(Integer32):
    """Custom type tnPsdSfpInfoClassOfWdm based on Integer32"""
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
        *(("other", 1),
          ("bw", 2),
          ("cwdm", 3),
          ("dwdm", 4))
    )


_TnPsdSfpInfoClassOfWdm_Type.__name__ = "Integer32"
_TnPsdSfpInfoClassOfWdm_Object = MibTableColumn
tnPsdSfpInfoClassOfWdm = _TnPsdSfpInfoClassOfWdm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 3),
    _TnPsdSfpInfoClassOfWdm_Type()
)
tnPsdSfpInfoClassOfWdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoClassOfWdm.setStatus("current")
_TnPsdSfpInfoConnectorType_Type = TropicPsdSfpConnectorType
_TnPsdSfpInfoConnectorType_Object = MibTableColumn
tnPsdSfpInfoConnectorType = _TnPsdSfpInfoConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 4),
    _TnPsdSfpInfoConnectorType_Type()
)
tnPsdSfpInfoConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoConnectorType.setStatus("current")
_TnPsdSfpInfoTransceiverCode_Type = TropicPsdSfpTransceiverCode
_TnPsdSfpInfoTransceiverCode_Object = MibTableColumn
tnPsdSfpInfoTransceiverCode = _TnPsdSfpInfoTransceiverCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 5),
    _TnPsdSfpInfoTransceiverCode_Type()
)
tnPsdSfpInfoTransceiverCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoTransceiverCode.setStatus("current")
_TnPsdSfpInfoBitRateNominal_Type = TropicPsdSfpBitRate
_TnPsdSfpInfoBitRateNominal_Object = MibTableColumn
tnPsdSfpInfoBitRateNominal = _TnPsdSfpInfoBitRateNominal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 6),
    _TnPsdSfpInfoBitRateNominal_Type()
)
tnPsdSfpInfoBitRateNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoBitRateNominal.setStatus("current")


class _TnPsdSfpInfoLinkType_Type(Integer32):
    """Custom type tnPsdSfpInfoLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("linkTypeNotApplicable", 0),
          ("link9umCoreFibre", 1),
          ("link50umCoreFibre", 2),
          ("link62um5CoreFibre", 3),
          ("linkCopperCable", 4))
    )


_TnPsdSfpInfoLinkType_Type.__name__ = "Integer32"
_TnPsdSfpInfoLinkType_Object = MibTableColumn
tnPsdSfpInfoLinkType = _TnPsdSfpInfoLinkType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 7),
    _TnPsdSfpInfoLinkType_Type()
)
tnPsdSfpInfoLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoLinkType.setStatus("current")
_TnPsdSfpInfoLinkMaxLength_Type = Unsigned32
_TnPsdSfpInfoLinkMaxLength_Object = MibTableColumn
tnPsdSfpInfoLinkMaxLength = _TnPsdSfpInfoLinkMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 8),
    _TnPsdSfpInfoLinkMaxLength_Type()
)
tnPsdSfpInfoLinkMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoLinkMaxLength.setStatus("current")
_TnPsdSfpInfoLinkLengthOverrun_Type = TruthValue
_TnPsdSfpInfoLinkLengthOverrun_Object = MibTableColumn
tnPsdSfpInfoLinkLengthOverrun = _TnPsdSfpInfoLinkLengthOverrun_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 9),
    _TnPsdSfpInfoLinkLengthOverrun_Type()
)
tnPsdSfpInfoLinkLengthOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoLinkLengthOverrun.setStatus("current")


class _TnPsdSfpInfoLinkLengthUnits_Type(Integer32):
    """Custom type tnPsdSfpInfoLinkLengthUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("unitsNotApplicable", 0),
          ("unitsM1", 1),
          ("unitsM10", 10),
          ("unitsKm1", 1000))
    )


_TnPsdSfpInfoLinkLengthUnits_Type.__name__ = "Integer32"
_TnPsdSfpInfoLinkLengthUnits_Object = MibTableColumn
tnPsdSfpInfoLinkLengthUnits = _TnPsdSfpInfoLinkLengthUnits_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 10),
    _TnPsdSfpInfoLinkLengthUnits_Type()
)
tnPsdSfpInfoLinkLengthUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoLinkLengthUnits.setStatus("current")
_TnPsdSfpInfoLinkLength_Type = TropicPsdSfpLinkLength
_TnPsdSfpInfoLinkLength_Object = MibTableColumn
tnPsdSfpInfoLinkLength = _TnPsdSfpInfoLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 11),
    _TnPsdSfpInfoLinkLength_Type()
)
tnPsdSfpInfoLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoLinkLength.setStatus("current")
_TnPsdSfpInfoVendorName_Type = TropicPsdSfpVendorName
_TnPsdSfpInfoVendorName_Object = MibTableColumn
tnPsdSfpInfoVendorName = _TnPsdSfpInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 12),
    _TnPsdSfpInfoVendorName_Type()
)
tnPsdSfpInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoVendorName.setStatus("current")
_TnPsdSfpInfoVendorOUI_Type = TropicPsdSfpVendorOUI
_TnPsdSfpInfoVendorOUI_Object = MibTableColumn
tnPsdSfpInfoVendorOUI = _TnPsdSfpInfoVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 13),
    _TnPsdSfpInfoVendorOUI_Type()
)
tnPsdSfpInfoVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoVendorOUI.setStatus("current")
_TnPsdSfpInfoPartNumber_Type = TropicPsdSfpPartNumber
_TnPsdSfpInfoPartNumber_Object = MibTableColumn
tnPsdSfpInfoPartNumber = _TnPsdSfpInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 14),
    _TnPsdSfpInfoPartNumber_Type()
)
tnPsdSfpInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoPartNumber.setStatus("current")
_TnPsdSfpInfoRevisionNumber_Type = TropicPsdSfpRevisionNumber
_TnPsdSfpInfoRevisionNumber_Object = MibTableColumn
tnPsdSfpInfoRevisionNumber = _TnPsdSfpInfoRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 15),
    _TnPsdSfpInfoRevisionNumber_Type()
)
tnPsdSfpInfoRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoRevisionNumber.setStatus("current")
_TnPsdSfpInfoWavelength_Type = TropicPsdSfpWavelength
_TnPsdSfpInfoWavelength_Object = MibTableColumn
tnPsdSfpInfoWavelength = _TnPsdSfpInfoWavelength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 16),
    _TnPsdSfpInfoWavelength_Type()
)
tnPsdSfpInfoWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoWavelength.setStatus("current")
_TnPsdSfpInfoBitRateMaximum_Type = TropicPsdSfpBitRate
_TnPsdSfpInfoBitRateMaximum_Object = MibTableColumn
tnPsdSfpInfoBitRateMaximum = _TnPsdSfpInfoBitRateMaximum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 17),
    _TnPsdSfpInfoBitRateMaximum_Type()
)
tnPsdSfpInfoBitRateMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoBitRateMaximum.setStatus("current")
_TnPsdSfpInfoBitRateMinimum_Type = TropicPsdSfpBitRate
_TnPsdSfpInfoBitRateMinimum_Object = MibTableColumn
tnPsdSfpInfoBitRateMinimum = _TnPsdSfpInfoBitRateMinimum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 18),
    _TnPsdSfpInfoBitRateMinimum_Type()
)
tnPsdSfpInfoBitRateMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoBitRateMinimum.setStatus("current")
_TnPsdSfpInfoVendorSerialNumber_Type = TropicPsdSfpVendorSerialNumber
_TnPsdSfpInfoVendorSerialNumber_Object = MibTableColumn
tnPsdSfpInfoVendorSerialNumber = _TnPsdSfpInfoVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 19),
    _TnPsdSfpInfoVendorSerialNumber_Type()
)
tnPsdSfpInfoVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoVendorSerialNumber.setStatus("current")
_TnPsdSfpInfoVendorDate_Type = TropicPsdSfpVendorDate
_TnPsdSfpInfoVendorDate_Object = MibTableColumn
tnPsdSfpInfoVendorDate = _TnPsdSfpInfoVendorDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 20),
    _TnPsdSfpInfoVendorDate_Type()
)
tnPsdSfpInfoVendorDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoVendorDate.setStatus("current")
_TnPsdSfpInfoVendorSpecific_Type = TropicPsdSfpVendorSpecific
_TnPsdSfpInfoVendorSpecific_Object = MibTableColumn
tnPsdSfpInfoVendorSpecific = _TnPsdSfpInfoVendorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 21),
    _TnPsdSfpInfoVendorSpecific_Type()
)
tnPsdSfpInfoVendorSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoVendorSpecific.setStatus("current")
_TnPsdSfpInfoCLEI_Type = TropicPsdSfpCLEICode
_TnPsdSfpInfoCLEI_Object = MibTableColumn
tnPsdSfpInfoCLEI = _TnPsdSfpInfoCLEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 22),
    _TnPsdSfpInfoCLEI_Type()
)
tnPsdSfpInfoCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoCLEI.setStatus("current")
_TnPsdSfpInfoAluPartNumber_Type = TropicPsdSfpAluPartNumber
_TnPsdSfpInfoAluPartNumber_Object = MibTableColumn
tnPsdSfpInfoAluPartNumber = _TnPsdSfpInfoAluPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 23),
    _TnPsdSfpInfoAluPartNumber_Type()
)
tnPsdSfpInfoAluPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoAluPartNumber.setStatus("current")
_TnPsdSfpInfoAluSerialNumber_Type = TropicPsdSfpAluSerialNumber
_TnPsdSfpInfoAluSerialNumber_Object = MibTableColumn
tnPsdSfpInfoAluSerialNumber = _TnPsdSfpInfoAluSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 24),
    _TnPsdSfpInfoAluSerialNumber_Type()
)
tnPsdSfpInfoAluSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoAluSerialNumber.setStatus("current")
_TnPsdSfpInfoIcs_Type = TropicPsdSfpIcs
_TnPsdSfpInfoIcs_Object = MibTableColumn
tnPsdSfpInfoIcs = _TnPsdSfpInfoIcs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 25),
    _TnPsdSfpInfoIcs_Type()
)
tnPsdSfpInfoIcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoIcs.setStatus("current")
_TnPsdSfpInfoNokiaPartNumber_Type = TropicPsdSfpNokiaPartNumber
_TnPsdSfpInfoNokiaPartNumber_Object = MibTableColumn
tnPsdSfpInfoNokiaPartNumber = _TnPsdSfpInfoNokiaPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 26),
    _TnPsdSfpInfoNokiaPartNumber_Type()
)
tnPsdSfpInfoNokiaPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoNokiaPartNumber.setStatus("current")
_TnPsdSfpInfoTunable_Type = TruthValue
_TnPsdSfpInfoTunable_Object = MibTableColumn
tnPsdSfpInfoTunable = _TnPsdSfpInfoTunable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 27),
    _TnPsdSfpInfoTunable_Type()
)
tnPsdSfpInfoTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoTunable.setStatus("current")


class _TnPsdSfpInfoFrequency_Type(SnmpAdminString):
    """Custom type tnPsdSfpInfoFrequency based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TnPsdSfpInfoFrequency_Type.__name__ = "SnmpAdminString"
_TnPsdSfpInfoFrequency_Object = MibTableColumn
tnPsdSfpInfoFrequency = _TnPsdSfpInfoFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 28),
    _TnPsdSfpInfoFrequency_Type()
)
tnPsdSfpInfoFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoFrequency.setStatus("current")


class _TnPsdSfpInfoFrequencyLow_Type(SnmpAdminString):
    """Custom type tnPsdSfpInfoFrequencyLow based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TnPsdSfpInfoFrequencyLow_Type.__name__ = "SnmpAdminString"
_TnPsdSfpInfoFrequencyLow_Object = MibTableColumn
tnPsdSfpInfoFrequencyLow = _TnPsdSfpInfoFrequencyLow_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 29),
    _TnPsdSfpInfoFrequencyLow_Type()
)
tnPsdSfpInfoFrequencyLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoFrequencyLow.setStatus("current")


class _TnPsdSfpInfoFrequencyHigh_Type(SnmpAdminString):
    """Custom type tnPsdSfpInfoFrequencyHigh based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TnPsdSfpInfoFrequencyHigh_Type.__name__ = "SnmpAdminString"
_TnPsdSfpInfoFrequencyHigh_Object = MibTableColumn
tnPsdSfpInfoFrequencyHigh = _TnPsdSfpInfoFrequencyHigh_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 30),
    _TnPsdSfpInfoFrequencyHigh_Type()
)
tnPsdSfpInfoFrequencyHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoFrequencyHigh.setStatus("current")


class _TnPsdSfpInfoFrequencyGrid_Type(SnmpAdminString):
    """Custom type tnPsdSfpInfoFrequencyGrid based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TnPsdSfpInfoFrequencyGrid_Type.__name__ = "SnmpAdminString"
_TnPsdSfpInfoFrequencyGrid_Object = MibTableColumn
tnPsdSfpInfoFrequencyGrid = _TnPsdSfpInfoFrequencyGrid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 31),
    _TnPsdSfpInfoFrequencyGrid_Type()
)
tnPsdSfpInfoFrequencyGrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoFrequencyGrid.setStatus("current")


class _TnPsdSfpInfoTuningStatus_Type(Integer32):
    """Custom type tnPsdSfpInfoTuningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("tuningOK", 1),
          ("tuningFreqProvisionedToZero", 2),
          ("tuningInProgress", 3),
          ("tuningFreqProvisionedOutOfRange", 4),
          ("tuningFailure", 5))
    )


_TnPsdSfpInfoTuningStatus_Type.__name__ = "Integer32"
_TnPsdSfpInfoTuningStatus_Object = MibTableColumn
tnPsdSfpInfoTuningStatus = _TnPsdSfpInfoTuningStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 32),
    _TnPsdSfpInfoTuningStatus_Type()
)
tnPsdSfpInfoTuningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdSfpInfoTuningStatus.setStatus("current")
_TnPsdDdmDataTable_Object = MibTable
tnPsdDdmDataTable = _TnPsdDdmDataTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 4)
)
if mibBuilder.loadTexts:
    tnPsdDdmDataTable.setStatus("current")
_TnPsdDdmDataEntry_Object = MibTableRow
tnPsdDdmDataEntry = _TnPsdDdmDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 4, 1)
)
tnPsdDdmDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-PSD-MIB", "tnPsdDdmDataType"),
)
if mibBuilder.loadTexts:
    tnPsdDdmDataEntry.setStatus("current")
_TnPsdDdmDataType_Type = TropicPsdDdmDataType
_TnPsdDdmDataType_Object = MibTableColumn
tnPsdDdmDataType = _TnPsdDdmDataType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 4, 1, 1),
    _TnPsdDdmDataType_Type()
)
tnPsdDdmDataType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdDdmDataType.setStatus("current")
_TnPsdDdmDataValue_Type = Integer32
_TnPsdDdmDataValue_Object = MibTableColumn
tnPsdDdmDataValue = _TnPsdDdmDataValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 4, 1, 2),
    _TnPsdDdmDataValue_Type()
)
tnPsdDdmDataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdDdmDataValue.setStatus("current")
_TnPsdLagCommandTable_Object = MibTable
tnPsdLagCommandTable = _TnPsdLagCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 5)
)
if mibBuilder.loadTexts:
    tnPsdLagCommandTable.setStatus("current")
_TnPsdLagCommandEntry_Object = MibTableRow
tnPsdLagCommandEntry = _TnPsdLagCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tnPsdLagCommandEntry.setStatus("current")
_TnPsdLagCommandSubgroupSelected_Type = TruthValue
_TnPsdLagCommandSubgroupSelected_Object = MibTableColumn
tnPsdLagCommandSubgroupSelected = _TnPsdLagCommandSubgroupSelected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 5, 1, 1),
    _TnPsdLagCommandSubgroupSelected_Type()
)
tnPsdLagCommandSubgroupSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdLagCommandSubgroupSelected.setStatus("current")
_TnPsdAlsTable_Object = MibTable
tnPsdAlsTable = _TnPsdAlsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 6)
)
if mibBuilder.loadTexts:
    tnPsdAlsTable.setStatus("current")
_TnPsdAlsEntry_Object = MibTableRow
tnPsdAlsEntry = _TnPsdAlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 6, 1)
)
tnPsdAlsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPsdAlsEntry.setStatus("current")


class _TnPsdAlsEnabled_Type(TruthValue):
    """Custom type tnPsdAlsEnabled based on TruthValue"""
    defaultValue = 2


_TnPsdAlsEnabled_Type.__name__ = "TruthValue"
_TnPsdAlsEnabled_Object = MibTableColumn
tnPsdAlsEnabled = _TnPsdAlsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 6, 1, 1),
    _TnPsdAlsEnabled_Type()
)
tnPsdAlsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdAlsEnabled.setStatus("current")


class _TnPsdAlsWaitToRestart_Type(Unsigned32):
    """Custom type tnPsdAlsWaitToRestart based on Unsigned32"""
    defaultValue = 100


_TnPsdAlsWaitToRestart_Type.__name__ = "Unsigned32"
_TnPsdAlsWaitToRestart_Object = MibTableColumn
tnPsdAlsWaitToRestart = _TnPsdAlsWaitToRestart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 6, 1, 2),
    _TnPsdAlsWaitToRestart_Type()
)
tnPsdAlsWaitToRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdAlsWaitToRestart.setStatus("current")


class _TnPsdAlsTxTime_Type(Unsigned32):
    """Custom type tnPsdAlsTxTime based on Unsigned32"""
    defaultValue = 20


_TnPsdAlsTxTime_Type.__name__ = "Unsigned32"
_TnPsdAlsTxTime_Object = MibTableColumn
tnPsdAlsTxTime = _TnPsdAlsTxTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 6, 1, 3),
    _TnPsdAlsTxTime_Type()
)
tnPsdAlsTxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdAlsTxTime.setStatus("current")


class _TnPsdAlsState_Type(Integer32):
    """Custom type tnPsdAlsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_TnPsdAlsState_Type.__name__ = "Integer32"
_TnPsdAlsState_Object = MibTableColumn
tnPsdAlsState = _TnPsdAlsState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 6, 1, 4),
    _TnPsdAlsState_Type()
)
tnPsdAlsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdAlsState.setStatus("current")
_TnPsdAlsActiveCheck_Type = TruthValue
_TnPsdAlsActiveCheck_Object = MibTableColumn
tnPsdAlsActiveCheck = _TnPsdAlsActiveCheck_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 6, 1, 5),
    _TnPsdAlsActiveCheck_Type()
)
tnPsdAlsActiveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdAlsActiveCheck.setStatus("current")
_TnPsdAlsActiveCheckForTest_Type = TruthValue
_TnPsdAlsActiveCheckForTest_Object = MibTableColumn
tnPsdAlsActiveCheckForTest = _TnPsdAlsActiveCheckForTest_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 6, 1, 6),
    _TnPsdAlsActiveCheckForTest_Type()
)
tnPsdAlsActiveCheckForTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdAlsActiveCheckForTest.setStatus("current")
_TnPsdInterfaceConformance_ObjectIdentity = ObjectIdentity
tnPsdInterfaceConformance = _TnPsdInterfaceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2)
)
_TnPsdInterfaceGroups_ObjectIdentity = ObjectIdentity
tnPsdInterfaceGroups = _TnPsdInterfaceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2)
)
_TnPsdSnmp_ObjectIdentity = ObjectIdentity
tnPsdSnmp = _TnPsdSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4)
)
_TnPsdSnmpNotifs_ObjectIdentity = ObjectIdentity
tnPsdSnmpNotifs = _TnPsdSnmpNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 0)
)
_TnPsdSnmpObjects_ObjectIdentity = ObjectIdentity
tnPsdSnmpObjects = _TnPsdSnmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1)
)
_TnPsdSnmpTrapDestTable_Object = MibTable
tnPsdSnmpTrapDestTable = _TnPsdSnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestTable.setStatus("current")
_TnPsdSnmpTrapDestEntry_Object = MibTableRow
tnPsdSnmpTrapDestEntry = _TnPsdSnmpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1)
)
tnPsdSnmpTrapDestEntry.setIndexNames(
    (0, "TROPIC-PSD-MIB", "tnPsdSnmpTrapDestServerId"),
)
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestEntry.setStatus("current")


class _TnPsdSnmpTrapDestServerId_Type(OctetString):
    """Custom type tnPsdSnmpTrapDestServerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPsdSnmpTrapDestServerId_Type.__name__ = "OctetString"
_TnPsdSnmpTrapDestServerId_Object = MibTableColumn
tnPsdSnmpTrapDestServerId = _TnPsdSnmpTrapDestServerId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 1),
    _TnPsdSnmpTrapDestServerId_Type()
)
tnPsdSnmpTrapDestServerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestServerId.setStatus("current")


class _TnPsdSnmpTrapDestAddrType_Type(InetAddressType):
    """Custom type tnPsdSnmpTrapDestAddrType based on InetAddressType"""
    defaultValue = 0


_TnPsdSnmpTrapDestAddrType_Type.__name__ = "InetAddressType"
_TnPsdSnmpTrapDestAddrType_Object = MibTableColumn
tnPsdSnmpTrapDestAddrType = _TnPsdSnmpTrapDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 2),
    _TnPsdSnmpTrapDestAddrType_Type()
)
tnPsdSnmpTrapDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestAddrType.setStatus("current")
_TnPsdSnmpTrapDestAddr_Type = InetAddress
_TnPsdSnmpTrapDestAddr_Object = MibTableColumn
tnPsdSnmpTrapDestAddr = _TnPsdSnmpTrapDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 3),
    _TnPsdSnmpTrapDestAddr_Type()
)
tnPsdSnmpTrapDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestAddr.setStatus("current")


class _TnPsdSnmpTrapDestPort_Type(TropicPsdSnmpPortNumberType):
    """Custom type tnPsdSnmpTrapDestPort based on TropicPsdSnmpPortNumberType"""
    defaultValue = 162


_TnPsdSnmpTrapDestPort_Type.__name__ = "TropicPsdSnmpPortNumberType"
_TnPsdSnmpTrapDestPort_Object = MibTableColumn
tnPsdSnmpTrapDestPort = _TnPsdSnmpTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 4),
    _TnPsdSnmpTrapDestPort_Type()
)
tnPsdSnmpTrapDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestPort.setStatus("current")


class _TnPsdSnmpTrapDestCommunity_Type(OctetString):
    """Custom type tnPsdSnmpTrapDestCommunity based on OctetString"""
    defaultValue = OctetString("alarm")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPsdSnmpTrapDestCommunity_Type.__name__ = "OctetString"
_TnPsdSnmpTrapDestCommunity_Object = MibTableColumn
tnPsdSnmpTrapDestCommunity = _TnPsdSnmpTrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 5),
    _TnPsdSnmpTrapDestCommunity_Type()
)
tnPsdSnmpTrapDestCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestCommunity.setStatus("current")


class _TnPsdSnmpTrapDestDyingGasp_Type(TruthValue):
    """Custom type tnPsdSnmpTrapDestDyingGasp based on TruthValue"""
    defaultValue = 2


_TnPsdSnmpTrapDestDyingGasp_Type.__name__ = "TruthValue"
_TnPsdSnmpTrapDestDyingGasp_Object = MibTableColumn
tnPsdSnmpTrapDestDyingGasp = _TnPsdSnmpTrapDestDyingGasp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 6),
    _TnPsdSnmpTrapDestDyingGasp_Type()
)
tnPsdSnmpTrapDestDyingGasp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestDyingGasp.setStatus("current")
_TnPsdSnmpTrapDestRowStatus_Type = RowStatus
_TnPsdSnmpTrapDestRowStatus_Object = MibTableColumn
tnPsdSnmpTrapDestRowStatus = _TnPsdSnmpTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 7),
    _TnPsdSnmpTrapDestRowStatus_Type()
)
tnPsdSnmpTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestRowStatus.setStatus("current")


class _TnPsdSnmpTrapDestSnmpVersion_Type(Integer32):
    """Custom type tnPsdSnmpTrapDestSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv2c", 2),
          ("snmpv3", 3))
    )


_TnPsdSnmpTrapDestSnmpVersion_Type.__name__ = "Integer32"
_TnPsdSnmpTrapDestSnmpVersion_Object = MibTableColumn
tnPsdSnmpTrapDestSnmpVersion = _TnPsdSnmpTrapDestSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 8),
    _TnPsdSnmpTrapDestSnmpVersion_Type()
)
tnPsdSnmpTrapDestSnmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestSnmpVersion.setStatus("current")


class _TnPsdSnmpTrapDestUserName_Type(SnmpAdminString):
    """Custom type tnPsdSnmpTrapDestUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnPsdSnmpTrapDestUserName_Type.__name__ = "SnmpAdminString"
_TnPsdSnmpTrapDestUserName_Object = MibTableColumn
tnPsdSnmpTrapDestUserName = _TnPsdSnmpTrapDestUserName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 9),
    _TnPsdSnmpTrapDestUserName_Type()
)
tnPsdSnmpTrapDestUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestUserName.setStatus("current")
_TnPsdSnmpConformance_ObjectIdentity = ObjectIdentity
tnPsdSnmpConformance = _TnPsdSnmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 2)
)
_TnPsdSnmpGroups_ObjectIdentity = ObjectIdentity
tnPsdSnmpGroups = _TnPsdSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 2, 2)
)
_TnPsdDatabase_ObjectIdentity = ObjectIdentity
tnPsdDatabase = _TnPsdDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5)
)
_TnPsdDatabaseObjects_ObjectIdentity = ObjectIdentity
tnPsdDatabaseObjects = _TnPsdDatabaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5, 1)
)


class _TnPsdDatabaseBackupAndRestoreRemoteHostAddrType_Type(InetAddressType):
    """Custom type tnPsdDatabaseBackupAndRestoreRemoteHostAddrType based on InetAddressType"""
    defaultValue = 0


_TnPsdDatabaseBackupAndRestoreRemoteHostAddrType_Type.__name__ = "InetAddressType"
_TnPsdDatabaseBackupAndRestoreRemoteHostAddrType_Object = MibScalar
tnPsdDatabaseBackupAndRestoreRemoteHostAddrType = _TnPsdDatabaseBackupAndRestoreRemoteHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5, 1, 1),
    _TnPsdDatabaseBackupAndRestoreRemoteHostAddrType_Type()
)
tnPsdDatabaseBackupAndRestoreRemoteHostAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdDatabaseBackupAndRestoreRemoteHostAddrType.setStatus("current")
_TnPsdDatabaseBackupAndRestoreRemoteHostAddr_Type = InetAddress
_TnPsdDatabaseBackupAndRestoreRemoteHostAddr_Object = MibScalar
tnPsdDatabaseBackupAndRestoreRemoteHostAddr = _TnPsdDatabaseBackupAndRestoreRemoteHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5, 1, 2),
    _TnPsdDatabaseBackupAndRestoreRemoteHostAddr_Type()
)
tnPsdDatabaseBackupAndRestoreRemoteHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdDatabaseBackupAndRestoreRemoteHostAddr.setStatus("current")
_TnPsdDatabaseConformance_ObjectIdentity = ObjectIdentity
tnPsdDatabaseConformance = _TnPsdDatabaseConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5, 2)
)
_TnPsdDatabaseGroups_ObjectIdentity = ObjectIdentity
tnPsdDatabaseGroups = _TnPsdDatabaseGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5, 2, 2)
)
_TnPsdSoftware_ObjectIdentity = ObjectIdentity
tnPsdSoftware = _TnPsdSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6)
)
_TnPsdSoftwareNotifs_ObjectIdentity = ObjectIdentity
tnPsdSoftwareNotifs = _TnPsdSoftwareNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 0)
)
_TnPsdSoftwareObjects_ObjectIdentity = ObjectIdentity
tnPsdSoftwareObjects = _TnPsdSoftwareObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1)
)


class _TnPsdSoftwareRemoteHostAddrType_Type(InetAddressType):
    """Custom type tnPsdSoftwareRemoteHostAddrType based on InetAddressType"""
    defaultValue = 0


_TnPsdSoftwareRemoteHostAddrType_Type.__name__ = "InetAddressType"
_TnPsdSoftwareRemoteHostAddrType_Object = MibScalar
tnPsdSoftwareRemoteHostAddrType = _TnPsdSoftwareRemoteHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 1),
    _TnPsdSoftwareRemoteHostAddrType_Type()
)
tnPsdSoftwareRemoteHostAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdSoftwareRemoteHostAddrType.setStatus("current")
_TnPsdSoftwareRemoteHostAddr_Type = InetAddress
_TnPsdSoftwareRemoteHostAddr_Object = MibScalar
tnPsdSoftwareRemoteHostAddr = _TnPsdSoftwareRemoteHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 2),
    _TnPsdSoftwareRemoteHostAddr_Type()
)
tnPsdSoftwareRemoteHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdSoftwareRemoteHostAddr.setStatus("current")
_TnPsdShelfIsdTable_Object = MibTable
tnPsdShelfIsdTable = _TnPsdShelfIsdTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3)
)
if mibBuilder.loadTexts:
    tnPsdShelfIsdTable.setStatus("current")
_TnPsdShelfIsdEntry_Object = MibTableRow
tnPsdShelfIsdEntry = _TnPsdShelfIsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1)
)
tnPsdShelfIsdEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-PSD-MIB", "tnPsdShelfIsdId"),
)
if mibBuilder.loadTexts:
    tnPsdShelfIsdEntry.setStatus("current")
_TnPsdShelfIsdId_Type = TropicPsdIsdId
_TnPsdShelfIsdId_Object = MibTableColumn
tnPsdShelfIsdId = _TnPsdShelfIsdId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 1),
    _TnPsdShelfIsdId_Type()
)
tnPsdShelfIsdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdShelfIsdId.setStatus("current")
_TnPsdShelfIsdStatus_Type = TropicPsdIsdStatus
_TnPsdShelfIsdStatus_Object = MibTableColumn
tnPsdShelfIsdStatus = _TnPsdShelfIsdStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 2),
    _TnPsdShelfIsdStatus_Type()
)
tnPsdShelfIsdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdShelfIsdStatus.setStatus("current")
_TnPsdShelfIsdBuildTime_Type = DateAndTime
_TnPsdShelfIsdBuildTime_Object = MibTableColumn
tnPsdShelfIsdBuildTime = _TnPsdShelfIsdBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 3),
    _TnPsdShelfIsdBuildTime_Type()
)
tnPsdShelfIsdBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdShelfIsdBuildTime.setStatus("current")


class _TnPsdShelfIsdItemCode_Type(SnmpAdminString):
    """Custom type tnPsdShelfIsdItemCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_TnPsdShelfIsdItemCode_Type.__name__ = "SnmpAdminString"
_TnPsdShelfIsdItemCode_Object = MibTableColumn
tnPsdShelfIsdItemCode = _TnPsdShelfIsdItemCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 4),
    _TnPsdShelfIsdItemCode_Type()
)
tnPsdShelfIsdItemCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdShelfIsdItemCode.setStatus("current")
_TnPsdShelfIsdMaintenance_Type = TruthValue
_TnPsdShelfIsdMaintenance_Object = MibTableColumn
tnPsdShelfIsdMaintenance = _TnPsdShelfIsdMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 6),
    _TnPsdShelfIsdMaintenance_Type()
)
tnPsdShelfIsdMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdShelfIsdMaintenance.setStatus("current")
_TnPsdShelfIsdCompatible_Type = TruthValue
_TnPsdShelfIsdCompatible_Object = MibTableColumn
tnPsdShelfIsdCompatible = _TnPsdShelfIsdCompatible_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 7),
    _TnPsdShelfIsdCompatible_Type()
)
tnPsdShelfIsdCompatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdShelfIsdCompatible.setStatus("current")


class _TnPsdShelfIsdSwRelease_Type(SnmpAdminString):
    """Custom type tnPsdShelfIsdSwRelease based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnPsdShelfIsdSwRelease_Type.__name__ = "SnmpAdminString"
_TnPsdShelfIsdSwRelease_Object = MibTableColumn
tnPsdShelfIsdSwRelease = _TnPsdShelfIsdSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 8),
    _TnPsdShelfIsdSwRelease_Type()
)
tnPsdShelfIsdSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdShelfIsdSwRelease.setStatus("current")
_TnPsdSoftwareConformance_ObjectIdentity = ObjectIdentity
tnPsdSoftwareConformance = _TnPsdSoftwareConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 2)
)
_TnPsdSoftwareGroups_ObjectIdentity = ObjectIdentity
tnPsdSoftwareGroups = _TnPsdSoftwareGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 2, 2)
)
_TnPsdTime_ObjectIdentity = ObjectIdentity
tnPsdTime = _TnPsdTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7)
)
_TnPsdTimeNotifs_ObjectIdentity = ObjectIdentity
tnPsdTimeNotifs = _TnPsdTimeNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 0)
)
_TnPsdTimeObjects_ObjectIdentity = ObjectIdentity
tnPsdTimeObjects = _TnPsdTimeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1)
)
_TnPsdShelfTimeTable_Object = MibTable
tnPsdShelfTimeTable = _TnPsdShelfTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 1)
)
if mibBuilder.loadTexts:
    tnPsdShelfTimeTable.setStatus("current")
_TnPsdShelfTimeEntry_Object = MibTableRow
tnPsdShelfTimeEntry = _TnPsdShelfTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 1, 1)
)
tnPsdShelfTimeEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
)
if mibBuilder.loadTexts:
    tnPsdShelfTimeEntry.setStatus("current")
_TnPsdShelfTime_Type = DateAndTime
_TnPsdShelfTime_Object = MibTableColumn
tnPsdShelfTime = _TnPsdShelfTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 1, 1, 1),
    _TnPsdShelfTime_Type()
)
tnPsdShelfTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdShelfTime.setStatus("current")
_TnPsdNtpTable_Object = MibTable
tnPsdNtpTable = _TnPsdNtpTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 2)
)
if mibBuilder.loadTexts:
    tnPsdNtpTable.setStatus("current")
_TnPsdNtpEntry_Object = MibTableRow
tnPsdNtpEntry = _TnPsdNtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 2, 1)
)
tnPsdNtpEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
)
if mibBuilder.loadTexts:
    tnPsdNtpEntry.setStatus("current")


class _TnPsdNtpState_Type(Integer32):
    """Custom type tnPsdNtpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnPsdNtpState_Type.__name__ = "Integer32"
_TnPsdNtpState_Object = MibTableColumn
tnPsdNtpState = _TnPsdNtpState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 2, 1, 1),
    _TnPsdNtpState_Type()
)
tnPsdNtpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdNtpState.setStatus("current")


class _TnPsdNtpStatus_Type(Integer32):
    """Custom type tnPsdNtpStatus based on Integer32"""
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
        *(("notSynchronized", 1),
          ("synchronized", 2),
          ("initializing", 3),
          ("unreachable", 4),
          ("unknown", 5))
    )


_TnPsdNtpStatus_Type.__name__ = "Integer32"
_TnPsdNtpStatus_Object = MibTableColumn
tnPsdNtpStatus = _TnPsdNtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 2, 1, 2),
    _TnPsdNtpStatus_Type()
)
tnPsdNtpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdNtpStatus.setStatus("current")
_TnPsdNtpStratum_Type = Unsigned32
_TnPsdNtpStratum_Object = MibTableColumn
tnPsdNtpStratum = _TnPsdNtpStratum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 2, 1, 3),
    _TnPsdNtpStratum_Type()
)
tnPsdNtpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdNtpStratum.setStatus("current")
_TnPsdNtpAccuracy_Type = Unsigned32
_TnPsdNtpAccuracy_Object = MibTableColumn
tnPsdNtpAccuracy = _TnPsdNtpAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 2, 1, 4),
    _TnPsdNtpAccuracy_Type()
)
tnPsdNtpAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdNtpAccuracy.setStatus("current")
_TnPsdNtpServerTable_Object = MibTable
tnPsdNtpServerTable = _TnPsdNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3)
)
if mibBuilder.loadTexts:
    tnPsdNtpServerTable.setStatus("current")
_TnPsdNtpServerEntry_Object = MibTableRow
tnPsdNtpServerEntry = _TnPsdNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1)
)
tnPsdNtpServerEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-PSD-MIB", "tnPsdNtpServerIndex"),
)
if mibBuilder.loadTexts:
    tnPsdNtpServerEntry.setStatus("current")
_TnPsdNtpServerIndex_Type = TropicPsdNtpServerIndexType
_TnPsdNtpServerIndex_Object = MibTableColumn
tnPsdNtpServerIndex = _TnPsdNtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 1),
    _TnPsdNtpServerIndex_Type()
)
tnPsdNtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdNtpServerIndex.setStatus("current")


class _TnPsdNtpServerAddrType_Type(InetAddressType):
    """Custom type tnPsdNtpServerAddrType based on InetAddressType"""
    defaultValue = 0


_TnPsdNtpServerAddrType_Type.__name__ = "InetAddressType"
_TnPsdNtpServerAddrType_Object = MibTableColumn
tnPsdNtpServerAddrType = _TnPsdNtpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 2),
    _TnPsdNtpServerAddrType_Type()
)
tnPsdNtpServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdNtpServerAddrType.setStatus("current")
_TnPsdNtpServerAddr_Type = InetAddress
_TnPsdNtpServerAddr_Object = MibTableColumn
tnPsdNtpServerAddr = _TnPsdNtpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 3),
    _TnPsdNtpServerAddr_Type()
)
tnPsdNtpServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdNtpServerAddr.setStatus("current")
_TnPsdNtpServerSystemServer_Type = TruthValue
_TnPsdNtpServerSystemServer_Object = MibTableColumn
tnPsdNtpServerSystemServer = _TnPsdNtpServerSystemServer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 4),
    _TnPsdNtpServerSystemServer_Type()
)
tnPsdNtpServerSystemServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdNtpServerSystemServer.setStatus("current")
_TnPsdNtpServerReachable_Type = TruthValue
_TnPsdNtpServerReachable_Object = MibTableColumn
tnPsdNtpServerReachable = _TnPsdNtpServerReachable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 5),
    _TnPsdNtpServerReachable_Type()
)
tnPsdNtpServerReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdNtpServerReachable.setStatus("current")


class _TnPsdNtpServerReachabilityData_Type(Unsigned32):
    """Custom type tnPsdNtpServerReachabilityData based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnPsdNtpServerReachabilityData_Type.__name__ = "Unsigned32"
_TnPsdNtpServerReachabilityData_Object = MibTableColumn
tnPsdNtpServerReachabilityData = _TnPsdNtpServerReachabilityData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 6),
    _TnPsdNtpServerReachabilityData_Type()
)
tnPsdNtpServerReachabilityData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdNtpServerReachabilityData.setStatus("current")
_TnPsdNtpServerPollTime_Type = Unsigned32
_TnPsdNtpServerPollTime_Object = MibTableColumn
tnPsdNtpServerPollTime = _TnPsdNtpServerPollTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 7),
    _TnPsdNtpServerPollTime_Type()
)
tnPsdNtpServerPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdNtpServerPollTime.setStatus("current")
_TnPsdTimeConformance_ObjectIdentity = ObjectIdentity
tnPsdTimeConformance = _TnPsdTimeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 2)
)
_TnPsdTimeGroups_ObjectIdentity = ObjectIdentity
tnPsdTimeGroups = _TnPsdTimeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 2, 2)
)
_TnPsdIp_ObjectIdentity = ObjectIdentity
tnPsdIp = _TnPsdIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8)
)
_TnPsdIpNotifs_ObjectIdentity = ObjectIdentity
tnPsdIpNotifs = _TnPsdIpNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0)
)
_TnPsdIpObjects_ObjectIdentity = ObjectIdentity
tnPsdIpObjects = _TnPsdIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1)
)
_TnPsdEnforceSrcIpV4ToLoopbackIpV4_Type = TruthValue
_TnPsdEnforceSrcIpV4ToLoopbackIpV4_Object = MibScalar
tnPsdEnforceSrcIpV4ToLoopbackIpV4 = _TnPsdEnforceSrcIpV4ToLoopbackIpV4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 1),
    _TnPsdEnforceSrcIpV4ToLoopbackIpV4_Type()
)
tnPsdEnforceSrcIpV4ToLoopbackIpV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdEnforceSrcIpV4ToLoopbackIpV4.setStatus("current")
_TnPsdEnforceSrcIpV6ToLoopbackIpV6_Type = TruthValue
_TnPsdEnforceSrcIpV6ToLoopbackIpV6_Object = MibScalar
tnPsdEnforceSrcIpV6ToLoopbackIpV6 = _TnPsdEnforceSrcIpV6ToLoopbackIpV6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 2),
    _TnPsdEnforceSrcIpV6ToLoopbackIpV6_Type()
)
tnPsdEnforceSrcIpV6ToLoopbackIpV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdEnforceSrcIpV6ToLoopbackIpV6.setStatus("current")
_TnPsdManualIpv4AddressTable_Object = MibTable
tnPsdManualIpv4AddressTable = _TnPsdManualIpv4AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 3)
)
if mibBuilder.loadTexts:
    tnPsdManualIpv4AddressTable.setStatus("current")
_TnPsdManualIpv4AddressEntry_Object = MibTableRow
tnPsdManualIpv4AddressEntry = _TnPsdManualIpv4AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 3, 1)
)
tnPsdManualIpv4AddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPsdManualIpv4AddressEntry.setStatus("current")
_TnPsdManualIpv4AddressAddrType_Type = InetAddressType
_TnPsdManualIpv4AddressAddrType_Object = MibTableColumn
tnPsdManualIpv4AddressAddrType = _TnPsdManualIpv4AddressAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 3, 1, 1),
    _TnPsdManualIpv4AddressAddrType_Type()
)
tnPsdManualIpv4AddressAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdManualIpv4AddressAddrType.setStatus("current")


class _TnPsdManualIpv4AddressAddr_Type(InetAddress):
    """Custom type tnPsdManualIpv4AddressAddr based on InetAddress"""
    defaultHexValue = "00000000"


_TnPsdManualIpv4AddressAddr_Type.__name__ = "InetAddress"
_TnPsdManualIpv4AddressAddr_Object = MibTableColumn
tnPsdManualIpv4AddressAddr = _TnPsdManualIpv4AddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 3, 1, 2),
    _TnPsdManualIpv4AddressAddr_Type()
)
tnPsdManualIpv4AddressAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdManualIpv4AddressAddr.setStatus("current")


class _TnPsdManualIpv4AddressPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tnPsdManualIpv4AddressPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TnPsdManualIpv4AddressPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TnPsdManualIpv4AddressPrefixLen_Object = MibTableColumn
tnPsdManualIpv4AddressPrefixLen = _TnPsdManualIpv4AddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 3, 1, 3),
    _TnPsdManualIpv4AddressPrefixLen_Type()
)
tnPsdManualIpv4AddressPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdManualIpv4AddressPrefixLen.setStatus("current")
_TnPsdManualIpv6AddressTable_Object = MibTable
tnPsdManualIpv6AddressTable = _TnPsdManualIpv6AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 4)
)
if mibBuilder.loadTexts:
    tnPsdManualIpv6AddressTable.setStatus("current")
_TnPsdManualIpv6AddressEntry_Object = MibTableRow
tnPsdManualIpv6AddressEntry = _TnPsdManualIpv6AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 4, 1)
)
tnPsdManualIpv6AddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPsdManualIpv6AddressEntry.setStatus("current")
_TnPsdManualIpv6AddressAddrType_Type = InetAddressType
_TnPsdManualIpv6AddressAddrType_Object = MibTableColumn
tnPsdManualIpv6AddressAddrType = _TnPsdManualIpv6AddressAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 4, 1, 1),
    _TnPsdManualIpv6AddressAddrType_Type()
)
tnPsdManualIpv6AddressAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdManualIpv6AddressAddrType.setStatus("current")


class _TnPsdManualIpv6AddressAddr_Type(InetAddress):
    """Custom type tnPsdManualIpv6AddressAddr based on InetAddress"""
    defaultHexValue = "00000000000000000000000000000000"


_TnPsdManualIpv6AddressAddr_Type.__name__ = "InetAddress"
_TnPsdManualIpv6AddressAddr_Object = MibTableColumn
tnPsdManualIpv6AddressAddr = _TnPsdManualIpv6AddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 4, 1, 2),
    _TnPsdManualIpv6AddressAddr_Type()
)
tnPsdManualIpv6AddressAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdManualIpv6AddressAddr.setStatus("current")


class _TnPsdManualIpv6AddressPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tnPsdManualIpv6AddressPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TnPsdManualIpv6AddressPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TnPsdManualIpv6AddressPrefixLen_Object = MibTableColumn
tnPsdManualIpv6AddressPrefixLen = _TnPsdManualIpv6AddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 4, 1, 3),
    _TnPsdManualIpv6AddressPrefixLen_Type()
)
tnPsdManualIpv6AddressPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdManualIpv6AddressPrefixLen.setStatus("current")
_TnPsdActualIpAddressTable_Object = MibTable
tnPsdActualIpAddressTable = _TnPsdActualIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 5)
)
if mibBuilder.loadTexts:
    tnPsdActualIpAddressTable.setStatus("current")
_TnPsdActualIpAddressEntry_Object = MibTableRow
tnPsdActualIpAddressEntry = _TnPsdActualIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 5, 1)
)
tnPsdActualIpAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-PSD-MIB", "tnPsdActualIpAddressAddrType"),
    (0, "TROPIC-PSD-MIB", "tnPsdActualIpAddressAddr"),
)
if mibBuilder.loadTexts:
    tnPsdActualIpAddressEntry.setStatus("current")
_TnPsdActualIpAddressAddrType_Type = InetAddressType
_TnPsdActualIpAddressAddrType_Object = MibTableColumn
tnPsdActualIpAddressAddrType = _TnPsdActualIpAddressAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 5, 1, 1),
    _TnPsdActualIpAddressAddrType_Type()
)
tnPsdActualIpAddressAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdActualIpAddressAddrType.setStatus("current")


class _TnPsdActualIpAddressAddr_Type(InetAddress):
    """Custom type tnPsdActualIpAddressAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TnPsdActualIpAddressAddr_Type.__name__ = "InetAddress"
_TnPsdActualIpAddressAddr_Object = MibTableColumn
tnPsdActualIpAddressAddr = _TnPsdActualIpAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 5, 1, 2),
    _TnPsdActualIpAddressAddr_Type()
)
tnPsdActualIpAddressAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdActualIpAddressAddr.setStatus("current")
_TnPsdActualIpAddressPrefixLen_Type = InetAddressPrefixLength
_TnPsdActualIpAddressPrefixLen_Object = MibTableColumn
tnPsdActualIpAddressPrefixLen = _TnPsdActualIpAddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 5, 1, 3),
    _TnPsdActualIpAddressPrefixLen_Type()
)
tnPsdActualIpAddressPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdActualIpAddressPrefixLen.setStatus("current")
_TnPsdDhcpClientTable_Object = MibTable
tnPsdDhcpClientTable = _TnPsdDhcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 6)
)
if mibBuilder.loadTexts:
    tnPsdDhcpClientTable.setStatus("current")
_TnPsdDhcpClientEntry_Object = MibTableRow
tnPsdDhcpClientEntry = _TnPsdDhcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 6, 1)
)
tnPsdDhcpClientEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPsdDhcpClientEntry.setStatus("current")


class _TnPsdDhcpClientV4Enabled_Type(TruthValue):
    """Custom type tnPsdDhcpClientV4Enabled based on TruthValue"""
    defaultValue = 2


_TnPsdDhcpClientV4Enabled_Type.__name__ = "TruthValue"
_TnPsdDhcpClientV4Enabled_Object = MibTableColumn
tnPsdDhcpClientV4Enabled = _TnPsdDhcpClientV4Enabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 6, 1, 1),
    _TnPsdDhcpClientV4Enabled_Type()
)
tnPsdDhcpClientV4Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdDhcpClientV4Enabled.setStatus("current")
_TnPsdStaticRouteTable_Object = MibTable
tnPsdStaticRouteTable = _TnPsdStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7)
)
if mibBuilder.loadTexts:
    tnPsdStaticRouteTable.setStatus("current")
_TnPsdStaticRouteEntry_Object = MibTableRow
tnPsdStaticRouteEntry = _TnPsdStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1)
)
tnPsdStaticRouteEntry.setIndexNames(
    (0, "TROPIC-PSD-MIB", "tnPsdStaticRouteDestType"),
    (0, "TROPIC-PSD-MIB", "tnPsdStaticRouteDest"),
    (0, "TROPIC-PSD-MIB", "tnPsdStaticRoutePrefixLen"),
    (0, "TROPIC-PSD-MIB", "tnPsdStaticRouteGatewayType"),
    (0, "TROPIC-PSD-MIB", "tnPsdStaticRouteGateway"),
    (0, "TROPIC-PSD-MIB", "tnPsdStaticRouteIfIndex"),
    (0, "TROPIC-PSD-MIB", "tnPsdStaticRouteNetIfIndex"),
)
if mibBuilder.loadTexts:
    tnPsdStaticRouteEntry.setStatus("current")
_TnPsdStaticRouteDestType_Type = InetAddressType
_TnPsdStaticRouteDestType_Object = MibTableColumn
tnPsdStaticRouteDestType = _TnPsdStaticRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 1),
    _TnPsdStaticRouteDestType_Type()
)
tnPsdStaticRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdStaticRouteDestType.setStatus("current")


class _TnPsdStaticRouteDest_Type(InetAddress):
    """Custom type tnPsdStaticRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TnPsdStaticRouteDest_Type.__name__ = "InetAddress"
_TnPsdStaticRouteDest_Object = MibTableColumn
tnPsdStaticRouteDest = _TnPsdStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 2),
    _TnPsdStaticRouteDest_Type()
)
tnPsdStaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdStaticRouteDest.setStatus("current")
_TnPsdStaticRoutePrefixLen_Type = InetAddressPrefixLength
_TnPsdStaticRoutePrefixLen_Object = MibTableColumn
tnPsdStaticRoutePrefixLen = _TnPsdStaticRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 3),
    _TnPsdStaticRoutePrefixLen_Type()
)
tnPsdStaticRoutePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdStaticRoutePrefixLen.setStatus("current")
_TnPsdStaticRouteGatewayType_Type = InetAddressType
_TnPsdStaticRouteGatewayType_Object = MibTableColumn
tnPsdStaticRouteGatewayType = _TnPsdStaticRouteGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 4),
    _TnPsdStaticRouteGatewayType_Type()
)
tnPsdStaticRouteGatewayType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdStaticRouteGatewayType.setStatus("current")


class _TnPsdStaticRouteGateway_Type(InetAddress):
    """Custom type tnPsdStaticRouteGateway based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TnPsdStaticRouteGateway_Type.__name__ = "InetAddress"
_TnPsdStaticRouteGateway_Object = MibTableColumn
tnPsdStaticRouteGateway = _TnPsdStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 5),
    _TnPsdStaticRouteGateway_Type()
)
tnPsdStaticRouteGateway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdStaticRouteGateway.setStatus("current")
_TnPsdStaticRouteIfIndex_Type = InterfaceIndexOrZero
_TnPsdStaticRouteIfIndex_Object = MibTableColumn
tnPsdStaticRouteIfIndex = _TnPsdStaticRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 6),
    _TnPsdStaticRouteIfIndex_Type()
)
tnPsdStaticRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdStaticRouteIfIndex.setStatus("current")
_TnPsdStaticRouteNetIfIndex_Type = TropicPsdNetIfIndexOrZero
_TnPsdStaticRouteNetIfIndex_Object = MibTableColumn
tnPsdStaticRouteNetIfIndex = _TnPsdStaticRouteNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 7),
    _TnPsdStaticRouteNetIfIndex_Type()
)
tnPsdStaticRouteNetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdStaticRouteNetIfIndex.setStatus("current")


class _TnPsdStaticRouteMetric_Type(Integer32):
    """Custom type tnPsdStaticRouteMetric based on Integer32"""
    defaultValue = 100


_TnPsdStaticRouteMetric_Type.__name__ = "Integer32"
_TnPsdStaticRouteMetric_Object = MibTableColumn
tnPsdStaticRouteMetric = _TnPsdStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 8),
    _TnPsdStaticRouteMetric_Type()
)
tnPsdStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdStaticRouteMetric.setStatus("current")
_TnPsdStaticRouteRowStatus_Type = RowStatus
_TnPsdStaticRouteRowStatus_Object = MibTableColumn
tnPsdStaticRouteRowStatus = _TnPsdStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 9),
    _TnPsdStaticRouteRowStatus_Type()
)
tnPsdStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdStaticRouteRowStatus.setStatus("current")
_TnPsdActualRouteTable_Object = MibTable
tnPsdActualRouteTable = _TnPsdActualRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8)
)
if mibBuilder.loadTexts:
    tnPsdActualRouteTable.setStatus("current")
_TnPsdActualRouteEntry_Object = MibTableRow
tnPsdActualRouteEntry = _TnPsdActualRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1)
)
tnPsdActualRouteEntry.setIndexNames(
    (0, "TROPIC-PSD-MIB", "tnPsdActualRouteDestType"),
    (0, "TROPIC-PSD-MIB", "tnPsdActualRouteDest"),
    (0, "TROPIC-PSD-MIB", "tnPsdActualRoutePrefixLen"),
    (0, "TROPIC-PSD-MIB", "tnPsdActualRouteGatewayType"),
    (0, "TROPIC-PSD-MIB", "tnPsdActualRouteGateway"),
    (0, "TROPIC-PSD-MIB", "tnPsdActualRouteIfIndex"),
    (0, "TROPIC-PSD-MIB", "tnPsdActualRouteNetIfIndex"),
)
if mibBuilder.loadTexts:
    tnPsdActualRouteEntry.setStatus("current")
_TnPsdActualRouteDestType_Type = InetAddressType
_TnPsdActualRouteDestType_Object = MibTableColumn
tnPsdActualRouteDestType = _TnPsdActualRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 1),
    _TnPsdActualRouteDestType_Type()
)
tnPsdActualRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdActualRouteDestType.setStatus("current")


class _TnPsdActualRouteDest_Type(InetAddress):
    """Custom type tnPsdActualRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TnPsdActualRouteDest_Type.__name__ = "InetAddress"
_TnPsdActualRouteDest_Object = MibTableColumn
tnPsdActualRouteDest = _TnPsdActualRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 2),
    _TnPsdActualRouteDest_Type()
)
tnPsdActualRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdActualRouteDest.setStatus("current")
_TnPsdActualRoutePrefixLen_Type = InetAddressPrefixLength
_TnPsdActualRoutePrefixLen_Object = MibTableColumn
tnPsdActualRoutePrefixLen = _TnPsdActualRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 3),
    _TnPsdActualRoutePrefixLen_Type()
)
tnPsdActualRoutePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdActualRoutePrefixLen.setStatus("current")
_TnPsdActualRouteGatewayType_Type = InetAddressType
_TnPsdActualRouteGatewayType_Object = MibTableColumn
tnPsdActualRouteGatewayType = _TnPsdActualRouteGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 4),
    _TnPsdActualRouteGatewayType_Type()
)
tnPsdActualRouteGatewayType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdActualRouteGatewayType.setStatus("current")


class _TnPsdActualRouteGateway_Type(InetAddress):
    """Custom type tnPsdActualRouteGateway based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TnPsdActualRouteGateway_Type.__name__ = "InetAddress"
_TnPsdActualRouteGateway_Object = MibTableColumn
tnPsdActualRouteGateway = _TnPsdActualRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 5),
    _TnPsdActualRouteGateway_Type()
)
tnPsdActualRouteGateway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdActualRouteGateway.setStatus("current")
_TnPsdActualRouteIfIndex_Type = InterfaceIndexOrZero
_TnPsdActualRouteIfIndex_Object = MibTableColumn
tnPsdActualRouteIfIndex = _TnPsdActualRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 6),
    _TnPsdActualRouteIfIndex_Type()
)
tnPsdActualRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdActualRouteIfIndex.setStatus("current")
_TnPsdActualRouteNetIfIndex_Type = TropicPsdNetIfIndexOrZero
_TnPsdActualRouteNetIfIndex_Object = MibTableColumn
tnPsdActualRouteNetIfIndex = _TnPsdActualRouteNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 7),
    _TnPsdActualRouteNetIfIndex_Type()
)
tnPsdActualRouteNetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdActualRouteNetIfIndex.setStatus("current")
_TnPsdActualRouteMetric_Type = Integer32
_TnPsdActualRouteMetric_Object = MibTableColumn
tnPsdActualRouteMetric = _TnPsdActualRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 8),
    _TnPsdActualRouteMetric_Type()
)
tnPsdActualRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdActualRouteMetric.setStatus("current")
_TnPsdNetIfTable_Object = MibTable
tnPsdNetIfTable = _TnPsdNetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9)
)
if mibBuilder.loadTexts:
    tnPsdNetIfTable.setStatus("current")
_TnPsdNetIfEntry_Object = MibTableRow
tnPsdNetIfEntry = _TnPsdNetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tnPsdNetIfEntry.setStatus("current")


class _TnPsdNetIfIpAddrType_Type(InetAddressType):
    """Custom type tnPsdNetIfIpAddrType based on InetAddressType"""
    defaultValue = 1


_TnPsdNetIfIpAddrType_Type.__name__ = "InetAddressType"
_TnPsdNetIfIpAddrType_Object = MibTableColumn
tnPsdNetIfIpAddrType = _TnPsdNetIfIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 1),
    _TnPsdNetIfIpAddrType_Type()
)
tnPsdNetIfIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdNetIfIpAddrType.setStatus("current")


class _TnPsdNetIfIpAddr_Type(InetAddress):
    """Custom type tnPsdNetIfIpAddr based on InetAddress"""
    defaultHexValue = "00000000"


_TnPsdNetIfIpAddr_Type.__name__ = "InetAddress"
_TnPsdNetIfIpAddr_Object = MibTableColumn
tnPsdNetIfIpAddr = _TnPsdNetIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 2),
    _TnPsdNetIfIpAddr_Type()
)
tnPsdNetIfIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdNetIfIpAddr.setStatus("current")


class _TnPsdNetIfIpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tnPsdNetIfIpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 32


_TnPsdNetIfIpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TnPsdNetIfIpPrefixLen_Object = MibTableColumn
tnPsdNetIfIpPrefixLen = _TnPsdNetIfIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 3),
    _TnPsdNetIfIpPrefixLen_Type()
)
tnPsdNetIfIpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdNetIfIpPrefixLen.setStatus("current")


class _TnPsdNetIfOperStatus_Type(Integer32):
    """Custom type tnPsdNetIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 4))
    )


_TnPsdNetIfOperStatus_Type.__name__ = "Integer32"
_TnPsdNetIfOperStatus_Object = MibTableColumn
tnPsdNetIfOperStatus = _TnPsdNetIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 4),
    _TnPsdNetIfOperStatus_Type()
)
tnPsdNetIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdNetIfOperStatus.setStatus("current")
_TnPsdNetIfRemoteIpAddrType_Type = InetAddressType
_TnPsdNetIfRemoteIpAddrType_Object = MibTableColumn
tnPsdNetIfRemoteIpAddrType = _TnPsdNetIfRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 5),
    _TnPsdNetIfRemoteIpAddrType_Type()
)
tnPsdNetIfRemoteIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdNetIfRemoteIpAddrType.setStatus("current")
_TnPsdNetIfRemoteIpAddr_Type = InetAddress
_TnPsdNetIfRemoteIpAddr_Object = MibTableColumn
tnPsdNetIfRemoteIpAddr = _TnPsdNetIfRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 6),
    _TnPsdNetIfRemoteIpAddr_Type()
)
tnPsdNetIfRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdNetIfRemoteIpAddr.setStatus("current")


class _TnPsdNetIfMonitoring_Type(Integer32):
    """Custom type tnPsdNetIfMonitoring based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnPsdNetIfMonitoring_Type.__name__ = "Integer32"
_TnPsdNetIfMonitoring_Object = MibTableColumn
tnPsdNetIfMonitoring = _TnPsdNetIfMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 7),
    _TnPsdNetIfMonitoring_Type()
)
tnPsdNetIfMonitoring.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdNetIfMonitoring.setStatus("current")


class _TnPsdNetIfIp6AddrType_Type(InetAddressType):
    """Custom type tnPsdNetIfIp6AddrType based on InetAddressType"""
    defaultValue = 2


_TnPsdNetIfIp6AddrType_Type.__name__ = "InetAddressType"
_TnPsdNetIfIp6AddrType_Object = MibTableColumn
tnPsdNetIfIp6AddrType = _TnPsdNetIfIp6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 8),
    _TnPsdNetIfIp6AddrType_Type()
)
tnPsdNetIfIp6AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdNetIfIp6AddrType.setStatus("current")


class _TnPsdNetIfIp6Addr_Type(InetAddress):
    """Custom type tnPsdNetIfIp6Addr based on InetAddress"""
    defaultHexValue = "00000000000000000000000000000000"


_TnPsdNetIfIp6Addr_Type.__name__ = "InetAddress"
_TnPsdNetIfIp6Addr_Object = MibTableColumn
tnPsdNetIfIp6Addr = _TnPsdNetIfIp6Addr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 9),
    _TnPsdNetIfIp6Addr_Type()
)
tnPsdNetIfIp6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdNetIfIp6Addr.setStatus("current")


class _TnPsdNetIfIp6PrefixLen_Type(InetAddressPrefixLength):
    """Custom type tnPsdNetIfIp6PrefixLen based on InetAddressPrefixLength"""
    defaultValue = 128


_TnPsdNetIfIp6PrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TnPsdNetIfIp6PrefixLen_Object = MibTableColumn
tnPsdNetIfIp6PrefixLen = _TnPsdNetIfIp6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 10),
    _TnPsdNetIfIp6PrefixLen_Type()
)
tnPsdNetIfIp6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdNetIfIp6PrefixLen.setStatus("current")
_TnPsdNetIfRemoteIp6AddrType_Type = InetAddressType
_TnPsdNetIfRemoteIp6AddrType_Object = MibTableColumn
tnPsdNetIfRemoteIp6AddrType = _TnPsdNetIfRemoteIp6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 11),
    _TnPsdNetIfRemoteIp6AddrType_Type()
)
tnPsdNetIfRemoteIp6AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdNetIfRemoteIp6AddrType.setStatus("current")
_TnPsdNetIfRemoteIp6Addr_Type = InetAddress
_TnPsdNetIfRemoteIp6Addr_Object = MibTableColumn
tnPsdNetIfRemoteIp6Addr = _TnPsdNetIfRemoteIp6Addr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 12),
    _TnPsdNetIfRemoteIp6Addr_Type()
)
tnPsdNetIfRemoteIp6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdNetIfRemoteIp6Addr.setStatus("current")


class _TnPsdNetIfMonitoring6_Type(Integer32):
    """Custom type tnPsdNetIfMonitoring6 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnPsdNetIfMonitoring6_Type.__name__ = "Integer32"
_TnPsdNetIfMonitoring6_Object = MibTableColumn
tnPsdNetIfMonitoring6 = _TnPsdNetIfMonitoring6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 13),
    _TnPsdNetIfMonitoring6_Type()
)
tnPsdNetIfMonitoring6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdNetIfMonitoring6.setStatus("current")
_TnPsdNetIfEthFacilityTable_Object = MibTable
tnPsdNetIfEthFacilityTable = _TnPsdNetIfEthFacilityTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10)
)
if mibBuilder.loadTexts:
    tnPsdNetIfEthFacilityTable.setStatus("current")
_TnPsdNetIfEthFacilityEntry_Object = MibTableRow
tnPsdNetIfEthFacilityEntry = _TnPsdNetIfEthFacilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10, 1)
)
tnPsdNetIfEthFacilityEntry.setIndexNames(
    (0, "TROPIC-L1SERVICE-MIB", "tnNetIfIndex"),
    (0, "TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityTpid"),
    (0, "TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityVlanId"),
)
if mibBuilder.loadTexts:
    tnPsdNetIfEthFacilityEntry.setStatus("current")
_TnPsdNetIfEthFacilityTpid_Type = TropicPsdTransportIdentifier
_TnPsdNetIfEthFacilityTpid_Object = MibTableColumn
tnPsdNetIfEthFacilityTpid = _TnPsdNetIfEthFacilityTpid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10, 1, 1),
    _TnPsdNetIfEthFacilityTpid_Type()
)
tnPsdNetIfEthFacilityTpid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdNetIfEthFacilityTpid.setStatus("current")
_TnPsdNetIfEthFacilityVlanId_Type = TropicPsdVlanId
_TnPsdNetIfEthFacilityVlanId_Object = MibTableColumn
tnPsdNetIfEthFacilityVlanId = _TnPsdNetIfEthFacilityVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10, 1, 2),
    _TnPsdNetIfEthFacilityVlanId_Type()
)
tnPsdNetIfEthFacilityVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdNetIfEthFacilityVlanId.setStatus("current")
_TnPsdNetIfEthFacilityTypeOfOperation_Type = AluWdmTypeOfNetIfOperation
_TnPsdNetIfEthFacilityTypeOfOperation_Object = MibTableColumn
tnPsdNetIfEthFacilityTypeOfOperation = _TnPsdNetIfEthFacilityTypeOfOperation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10, 1, 3),
    _TnPsdNetIfEthFacilityTypeOfOperation_Type()
)
tnPsdNetIfEthFacilityTypeOfOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdNetIfEthFacilityTypeOfOperation.setStatus("current")


class _TnPsdNetIfEthFacilityPriorityEgress_Type(TropicPsdPriorityValue):
    """Custom type tnPsdNetIfEthFacilityPriorityEgress based on TropicPsdPriorityValue"""
    defaultValue = 7


_TnPsdNetIfEthFacilityPriorityEgress_Type.__name__ = "TropicPsdPriorityValue"
_TnPsdNetIfEthFacilityPriorityEgress_Object = MibTableColumn
tnPsdNetIfEthFacilityPriorityEgress = _TnPsdNetIfEthFacilityPriorityEgress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10, 1, 4),
    _TnPsdNetIfEthFacilityPriorityEgress_Type()
)
tnPsdNetIfEthFacilityPriorityEgress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdNetIfEthFacilityPriorityEgress.setStatus("current")


class _TnPsdNetIfEthFacilityDropEligibleEgress_Type(TruthValue):
    """Custom type tnPsdNetIfEthFacilityDropEligibleEgress based on TruthValue"""
    defaultValue = 2


_TnPsdNetIfEthFacilityDropEligibleEgress_Type.__name__ = "TruthValue"
_TnPsdNetIfEthFacilityDropEligibleEgress_Object = MibTableColumn
tnPsdNetIfEthFacilityDropEligibleEgress = _TnPsdNetIfEthFacilityDropEligibleEgress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10, 1, 5),
    _TnPsdNetIfEthFacilityDropEligibleEgress_Type()
)
tnPsdNetIfEthFacilityDropEligibleEgress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdNetIfEthFacilityDropEligibleEgress.setStatus("current")
_TnPsdProxyArpTable_Object = MibTable
tnPsdProxyArpTable = _TnPsdProxyArpTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 11)
)
if mibBuilder.loadTexts:
    tnPsdProxyArpTable.setStatus("current")
_TnPsdProxyArpEntry_Object = MibTableRow
tnPsdProxyArpEntry = _TnPsdProxyArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 11, 1)
)
tnPsdProxyArpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPsdProxyArpEntry.setStatus("current")


class _TnPsdProxyArp_Type(TmnxEnabledDisabled):
    """Custom type tnPsdProxyArp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnPsdProxyArp_Type.__name__ = "TmnxEnabledDisabled"
_TnPsdProxyArp_Object = MibTableColumn
tnPsdProxyArp = _TnPsdProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 11, 1, 1),
    _TnPsdProxyArp_Type()
)
tnPsdProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdProxyArp.setStatus("current")
_TnPsdIpConformance_ObjectIdentity = ObjectIdentity
tnPsdIpConformance = _TnPsdIpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2)
)
_TnPsdIpGroups_ObjectIdentity = ObjectIdentity
tnPsdIpGroups = _TnPsdIpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2)
)
_TnPsdFault_ObjectIdentity = ObjectIdentity
tnPsdFault = _TnPsdFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9)
)
_TnPsdFaultNotifs_ObjectIdentity = ObjectIdentity
tnPsdFaultNotifs = _TnPsdFaultNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 0)
)
_TnPsdFaultObjects_ObjectIdentity = ObjectIdentity
tnPsdFaultObjects = _TnPsdFaultObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1)
)
_TnPsdAsapTable_Object = MibTable
tnPsdAsapTable = _TnPsdAsapTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 1)
)
if mibBuilder.loadTexts:
    tnPsdAsapTable.setStatus("current")
_TnPsdAsapEntry_Object = MibTableRow
tnPsdAsapEntry = _TnPsdAsapEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 1, 1)
)
tnPsdAsapEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-PSD-MIB", "tnPsdAsapIndex"),
)
if mibBuilder.loadTexts:
    tnPsdAsapEntry.setStatus("current")
_TnPsdAsapIndex_Type = TropicPsdAsapIndexType
_TnPsdAsapIndex_Object = MibTableColumn
tnPsdAsapIndex = _TnPsdAsapIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 1, 1, 1),
    _TnPsdAsapIndex_Type()
)
tnPsdAsapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdAsapIndex.setStatus("current")


class _TnPsdAsapName_Type(SnmpAdminString):
    """Custom type tnPsdAsapName based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnPsdAsapName_Type.__name__ = "SnmpAdminString"
_TnPsdAsapName_Object = MibTableColumn
tnPsdAsapName = _TnPsdAsapName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 1, 1, 2),
    _TnPsdAsapName_Type()
)
tnPsdAsapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdAsapName.setStatus("current")
_TnPsdAsapFaultProfileTable_Object = MibTable
tnPsdAsapFaultProfileTable = _TnPsdAsapFaultProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2)
)
if mibBuilder.loadTexts:
    tnPsdAsapFaultProfileTable.setStatus("current")
_TnPsdAsapFaultProfileEntry_Object = MibTableRow
tnPsdAsapFaultProfileEntry = _TnPsdAsapFaultProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1)
)
tnPsdAsapFaultProfileEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-PSD-MIB", "tnPsdAsapIndex"),
    (0, "TROPIC-PSD-MIB", "tnPsdAsapFaultProfileCondition"),
    (0, "TROPIC-PSD-MIB", "tnPsdAsapFaultProfileLocationType"),
)
if mibBuilder.loadTexts:
    tnPsdAsapFaultProfileEntry.setStatus("current")
_TnPsdAsapFaultProfileCondition_Type = TnCondition
_TnPsdAsapFaultProfileCondition_Object = MibTableColumn
tnPsdAsapFaultProfileCondition = _TnPsdAsapFaultProfileCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1, 1),
    _TnPsdAsapFaultProfileCondition_Type()
)
tnPsdAsapFaultProfileCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdAsapFaultProfileCondition.setStatus("current")
_TnPsdAsapFaultProfileLocationType_Type = TropicPsdFaultLocationType
_TnPsdAsapFaultProfileLocationType_Object = MibTableColumn
tnPsdAsapFaultProfileLocationType = _TnPsdAsapFaultProfileLocationType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1, 2),
    _TnPsdAsapFaultProfileLocationType_Type()
)
tnPsdAsapFaultProfileLocationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdAsapFaultProfileLocationType.setStatus("current")
_TnPsdAsapFaultProfileSeverity_Type = TropicPsdFaultSeverity
_TnPsdAsapFaultProfileSeverity_Object = MibTableColumn
tnPsdAsapFaultProfileSeverity = _TnPsdAsapFaultProfileSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1, 3),
    _TnPsdAsapFaultProfileSeverity_Type()
)
tnPsdAsapFaultProfileSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdAsapFaultProfileSeverity.setStatus("current")
_TnPsdAsapFaultProfileReported_Type = TruthValue
_TnPsdAsapFaultProfileReported_Object = MibTableColumn
tnPsdAsapFaultProfileReported = _TnPsdAsapFaultProfileReported_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1, 4),
    _TnPsdAsapFaultProfileReported_Type()
)
tnPsdAsapFaultProfileReported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdAsapFaultProfileReported.setStatus("current")
_TnPsdAsapFaultProfileServiceAffecting_Type = TruthValue
_TnPsdAsapFaultProfileServiceAffecting_Object = MibTableColumn
tnPsdAsapFaultProfileServiceAffecting = _TnPsdAsapFaultProfileServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1, 5),
    _TnPsdAsapFaultProfileServiceAffecting_Type()
)
tnPsdAsapFaultProfileServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdAsapFaultProfileServiceAffecting.setStatus("current")
_TnPsdAsapFaultProfileAlarmText_Type = SnmpAdminString
_TnPsdAsapFaultProfileAlarmText_Object = MibTableColumn
tnPsdAsapFaultProfileAlarmText = _TnPsdAsapFaultProfileAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1, 6),
    _TnPsdAsapFaultProfileAlarmText_Type()
)
tnPsdAsapFaultProfileAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdAsapFaultProfileAlarmText.setStatus("current")
_TnPsdFaultTable_Object = MibTable
tnPsdFaultTable = _TnPsdFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 3)
)
if mibBuilder.loadTexts:
    tnPsdFaultTable.setStatus("current")
_TnPsdFaultEntry_Object = MibTableRow
tnPsdFaultEntry = _TnPsdFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 3, 1)
)
tnPsdFaultEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
)
if mibBuilder.loadTexts:
    tnPsdFaultEntry.setStatus("current")


class _TnPsdFaultAlarmRaiseTime_Type(TropicPsdFaultAlarmTime):
    """Custom type tnPsdFaultAlarmRaiseTime based on TropicPsdFaultAlarmTime"""
    defaultValue = 25


_TnPsdFaultAlarmRaiseTime_Type.__name__ = "TropicPsdFaultAlarmTime"
_TnPsdFaultAlarmRaiseTime_Object = MibTableColumn
tnPsdFaultAlarmRaiseTime = _TnPsdFaultAlarmRaiseTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 3, 1, 1),
    _TnPsdFaultAlarmRaiseTime_Type()
)
tnPsdFaultAlarmRaiseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdFaultAlarmRaiseTime.setStatus("current")
if mibBuilder.loadTexts:
    tnPsdFaultAlarmRaiseTime.setUnits("deciseconds")


class _TnPsdFaultAlarmClearTime_Type(TropicPsdFaultAlarmTime):
    """Custom type tnPsdFaultAlarmClearTime based on TropicPsdFaultAlarmTime"""
    defaultValue = 100


_TnPsdFaultAlarmClearTime_Type.__name__ = "TropicPsdFaultAlarmTime"
_TnPsdFaultAlarmClearTime_Object = MibTableColumn
tnPsdFaultAlarmClearTime = _TnPsdFaultAlarmClearTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 3, 1, 2),
    _TnPsdFaultAlarmClearTime_Type()
)
tnPsdFaultAlarmClearTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdFaultAlarmClearTime.setStatus("current")
if mibBuilder.loadTexts:
    tnPsdFaultAlarmClearTime.setUnits("deciseconds")
_TnPsdFaultConformance_ObjectIdentity = ObjectIdentity
tnPsdFaultConformance = _TnPsdFaultConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 2)
)
_TnPsdFaultGroups_ObjectIdentity = ObjectIdentity
tnPsdFaultGroups = _TnPsdFaultGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 2, 2)
)
_TnPsdSysDiscovery_ObjectIdentity = ObjectIdentity
tnPsdSysDiscovery = _TnPsdSysDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10)
)
_TnPsdSysDiscoveryObjects_ObjectIdentity = ObjectIdentity
tnPsdSysDiscoveryObjects = _TnPsdSysDiscoveryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10, 1)
)


class _TnPsdSysDiscoveryServerAddrType_Type(InetAddressType):
    """Custom type tnPsdSysDiscoveryServerAddrType based on InetAddressType"""
    defaultValue = 0


_TnPsdSysDiscoveryServerAddrType_Type.__name__ = "InetAddressType"
_TnPsdSysDiscoveryServerAddrType_Object = MibScalar
tnPsdSysDiscoveryServerAddrType = _TnPsdSysDiscoveryServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10, 1, 1),
    _TnPsdSysDiscoveryServerAddrType_Type()
)
tnPsdSysDiscoveryServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdSysDiscoveryServerAddrType.setStatus("current")
_TnPsdSysDiscoveryServerAddr_Type = InetAddress
_TnPsdSysDiscoveryServerAddr_Object = MibScalar
tnPsdSysDiscoveryServerAddr = _TnPsdSysDiscoveryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10, 1, 2),
    _TnPsdSysDiscoveryServerAddr_Type()
)
tnPsdSysDiscoveryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdSysDiscoveryServerAddr.setStatus("current")
_TnPsdSysDiscoveryConformance_ObjectIdentity = ObjectIdentity
tnPsdSysDiscoveryConformance = _TnPsdSysDiscoveryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10, 2)
)
_TnPsdSysDiscoveryGroups_ObjectIdentity = ObjectIdentity
tnPsdSysDiscoveryGroups = _TnPsdSysDiscoveryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10, 2, 2)
)
_TnPsdOtn_ObjectIdentity = ObjectIdentity
tnPsdOtn = _TnPsdOtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11)
)
_TnPsdOtnNotifs_ObjectIdentity = ObjectIdentity
tnPsdOtnNotifs = _TnPsdOtnNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0)
)
_TnPsdOtnObjects_ObjectIdentity = ObjectIdentity
tnPsdOtnObjects = _TnPsdOtnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1)
)
_TnPsdOtukTable_Object = MibTable
tnPsdOtukTable = _TnPsdOtukTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1)
)
if mibBuilder.loadTexts:
    tnPsdOtukTable.setStatus("current")
_TnPsdOtukEntry_Object = MibTableRow
tnPsdOtukEntry = _TnPsdOtukEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnPsdOtukEntry.setStatus("current")
_TnPsdOtukSapiAccepted_Type = TropicPsdSapi
_TnPsdOtukSapiAccepted_Object = MibTableColumn
tnPsdOtukSapiAccepted = _TnPsdOtukSapiAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1, 1),
    _TnPsdOtukSapiAccepted_Type()
)
tnPsdOtukSapiAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOtukSapiAccepted.setStatus("current")
_TnPsdOtukSapiExpected_Type = TropicPsdSapi
_TnPsdOtukSapiExpected_Object = MibTableColumn
tnPsdOtukSapiExpected = _TnPsdOtukSapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1, 2),
    _TnPsdOtukSapiExpected_Type()
)
tnPsdOtukSapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOtukSapiExpected.setStatus("current")
_TnPsdOtukSapiTransmitted_Type = TropicPsdSapi
_TnPsdOtukSapiTransmitted_Object = MibTableColumn
tnPsdOtukSapiTransmitted = _TnPsdOtukSapiTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1, 3),
    _TnPsdOtukSapiTransmitted_Type()
)
tnPsdOtukSapiTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOtukSapiTransmitted.setStatus("current")
_TnPsdOtukDapiAccepted_Type = TropicPsdDapi
_TnPsdOtukDapiAccepted_Object = MibTableColumn
tnPsdOtukDapiAccepted = _TnPsdOtukDapiAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1, 4),
    _TnPsdOtukDapiAccepted_Type()
)
tnPsdOtukDapiAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOtukDapiAccepted.setStatus("current")
_TnPsdOtukDapiExpected_Type = TropicPsdDapi
_TnPsdOtukDapiExpected_Object = MibTableColumn
tnPsdOtukDapiExpected = _TnPsdOtukDapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1, 5),
    _TnPsdOtukDapiExpected_Type()
)
tnPsdOtukDapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOtukDapiExpected.setStatus("current")
_TnPsdOtukDapiTransmitted_Type = TropicPsdDapi
_TnPsdOtukDapiTransmitted_Object = MibTableColumn
tnPsdOtukDapiTransmitted = _TnPsdOtukDapiTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1, 6),
    _TnPsdOtukDapiTransmitted_Type()
)
tnPsdOtukDapiTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOtukDapiTransmitted.setStatus("current")
_TnPsdOdukNimTable_Object = MibTable
tnPsdOdukNimTable = _TnPsdOdukNimTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 2)
)
if mibBuilder.loadTexts:
    tnPsdOdukNimTable.setStatus("current")
_TnPsdOdukNimEntry_Object = MibTableRow
tnPsdOdukNimEntry = _TnPsdOdukNimEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnPsdOdukNimEntry.setStatus("current")
_TnPsdOdukNimSapiAccepted_Type = TropicPsdSapi
_TnPsdOdukNimSapiAccepted_Object = MibTableColumn
tnPsdOdukNimSapiAccepted = _TnPsdOdukNimSapiAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 2, 1, 1),
    _TnPsdOdukNimSapiAccepted_Type()
)
tnPsdOdukNimSapiAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOdukNimSapiAccepted.setStatus("current")
_TnPsdOdukNimSapiExpected_Type = TropicPsdSapi
_TnPsdOdukNimSapiExpected_Object = MibTableColumn
tnPsdOdukNimSapiExpected = _TnPsdOdukNimSapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 2, 1, 2),
    _TnPsdOdukNimSapiExpected_Type()
)
tnPsdOdukNimSapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOdukNimSapiExpected.setStatus("current")
_TnPsdOdukNimDapiAccepted_Type = TropicPsdDapi
_TnPsdOdukNimDapiAccepted_Object = MibTableColumn
tnPsdOdukNimDapiAccepted = _TnPsdOdukNimDapiAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 2, 1, 3),
    _TnPsdOdukNimDapiAccepted_Type()
)
tnPsdOdukNimDapiAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOdukNimDapiAccepted.setStatus("current")
_TnPsdOdukNimDapiExpected_Type = TropicPsdDapi
_TnPsdOdukNimDapiExpected_Object = MibTableColumn
tnPsdOdukNimDapiExpected = _TnPsdOdukNimDapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 2, 1, 4),
    _TnPsdOdukNimDapiExpected_Type()
)
tnPsdOdukNimDapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOdukNimDapiExpected.setStatus("current")
_TnPsdOdukTtpTable_Object = MibTable
tnPsdOdukTtpTable = _TnPsdOdukTtpTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3)
)
if mibBuilder.loadTexts:
    tnPsdOdukTtpTable.setStatus("current")
_TnPsdOdukTtpEntry_Object = MibTableRow
tnPsdOdukTtpEntry = _TnPsdOdukTtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnPsdOdukTtpEntry.setStatus("current")
_TnPsdOdukTtpSapiAccepted_Type = TropicPsdSapi
_TnPsdOdukTtpSapiAccepted_Object = MibTableColumn
tnPsdOdukTtpSapiAccepted = _TnPsdOdukTtpSapiAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1, 1),
    _TnPsdOdukTtpSapiAccepted_Type()
)
tnPsdOdukTtpSapiAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOdukTtpSapiAccepted.setStatus("current")
_TnPsdOdukTtpSapiExpected_Type = TropicPsdSapi
_TnPsdOdukTtpSapiExpected_Object = MibTableColumn
tnPsdOdukTtpSapiExpected = _TnPsdOdukTtpSapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1, 2),
    _TnPsdOdukTtpSapiExpected_Type()
)
tnPsdOdukTtpSapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOdukTtpSapiExpected.setStatus("current")
_TnPsdOdukTtpSapiTransmitted_Type = TropicPsdSapi
_TnPsdOdukTtpSapiTransmitted_Object = MibTableColumn
tnPsdOdukTtpSapiTransmitted = _TnPsdOdukTtpSapiTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1, 3),
    _TnPsdOdukTtpSapiTransmitted_Type()
)
tnPsdOdukTtpSapiTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOdukTtpSapiTransmitted.setStatus("current")
_TnPsdOdukTtpDapiAccepted_Type = TropicPsdDapi
_TnPsdOdukTtpDapiAccepted_Object = MibTableColumn
tnPsdOdukTtpDapiAccepted = _TnPsdOdukTtpDapiAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1, 4),
    _TnPsdOdukTtpDapiAccepted_Type()
)
tnPsdOdukTtpDapiAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOdukTtpDapiAccepted.setStatus("current")
_TnPsdOdukTtpDapiExpected_Type = TropicPsdDapi
_TnPsdOdukTtpDapiExpected_Object = MibTableColumn
tnPsdOdukTtpDapiExpected = _TnPsdOdukTtpDapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1, 5),
    _TnPsdOdukTtpDapiExpected_Type()
)
tnPsdOdukTtpDapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOdukTtpDapiExpected.setStatus("current")
_TnPsdOdukTtpDapiTransmitted_Type = TropicPsdDapi
_TnPsdOdukTtpDapiTransmitted_Object = MibTableColumn
tnPsdOdukTtpDapiTransmitted = _TnPsdOdukTtpDapiTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1, 6),
    _TnPsdOdukTtpDapiTransmitted_Type()
)
tnPsdOdukTtpDapiTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOdukTtpDapiTransmitted.setStatus("current")
_TnPsdOdukTTable_Object = MibTable
tnPsdOdukTTable = _TnPsdOdukTTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4)
)
if mibBuilder.loadTexts:
    tnPsdOdukTTable.setStatus("current")
_TnPsdOdukTEntry_Object = MibTableRow
tnPsdOdukTEntry = _TnPsdOdukTEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnPsdOdukTEntry.setStatus("current")
_TnPsdOdukTSapiAccepted_Type = TropicPsdSapi
_TnPsdOdukTSapiAccepted_Object = MibTableColumn
tnPsdOdukTSapiAccepted = _TnPsdOdukTSapiAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1, 1),
    _TnPsdOdukTSapiAccepted_Type()
)
tnPsdOdukTSapiAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOdukTSapiAccepted.setStatus("current")
_TnPsdOdukTSapiExpected_Type = TropicPsdSapi
_TnPsdOdukTSapiExpected_Object = MibTableColumn
tnPsdOdukTSapiExpected = _TnPsdOdukTSapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1, 2),
    _TnPsdOdukTSapiExpected_Type()
)
tnPsdOdukTSapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOdukTSapiExpected.setStatus("current")
_TnPsdOdukTSapiTransmitted_Type = TropicPsdSapi
_TnPsdOdukTSapiTransmitted_Object = MibTableColumn
tnPsdOdukTSapiTransmitted = _TnPsdOdukTSapiTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1, 3),
    _TnPsdOdukTSapiTransmitted_Type()
)
tnPsdOdukTSapiTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOdukTSapiTransmitted.setStatus("current")
_TnPsdOdukTDapiAccepted_Type = TropicPsdDapi
_TnPsdOdukTDapiAccepted_Object = MibTableColumn
tnPsdOdukTDapiAccepted = _TnPsdOdukTDapiAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1, 4),
    _TnPsdOdukTDapiAccepted_Type()
)
tnPsdOdukTDapiAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOdukTDapiAccepted.setStatus("current")
_TnPsdOdukTDapiExpected_Type = TropicPsdDapi
_TnPsdOdukTDapiExpected_Object = MibTableColumn
tnPsdOdukTDapiExpected = _TnPsdOdukTDapiExpected_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1, 5),
    _TnPsdOdukTDapiExpected_Type()
)
tnPsdOdukTDapiExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOdukTDapiExpected.setStatus("current")
_TnPsdOdukTDapiTransmitted_Type = TropicPsdDapi
_TnPsdOdukTDapiTransmitted_Object = MibTableColumn
tnPsdOdukTDapiTransmitted = _TnPsdOdukTDapiTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1, 6),
    _TnPsdOdukTDapiTransmitted_Type()
)
tnPsdOdukTDapiTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOdukTDapiTransmitted.setStatus("current")
_TnPsdOdukTtpDmTable_Object = MibTable
tnPsdOdukTtpDmTable = _TnPsdOdukTtpDmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 5)
)
if mibBuilder.loadTexts:
    tnPsdOdukTtpDmTable.setStatus("current")
_TnPsdOdukTtpDmEntry_Object = MibTableRow
tnPsdOdukTtpDmEntry = _TnPsdOdukTtpDmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 5, 1)
)
tnPsdOdukTtpDmEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnPsdOdukTtpDmEntry.setStatus("current")


class _TnPsdOdukTtpDmReflection_Type(Integer32):
    """Custom type tnPsdOdukTtpDmReflection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnPsdOdukTtpDmReflection_Type.__name__ = "Integer32"
_TnPsdOdukTtpDmReflection_Object = MibTableColumn
tnPsdOdukTtpDmReflection = _TnPsdOdukTtpDmReflection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 5, 1, 1),
    _TnPsdOdukTtpDmReflection_Type()
)
tnPsdOdukTtpDmReflection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdOdukTtpDmReflection.setStatus("current")


class _TnPsdOdukTtpDmSessionType_Type(Integer32):
    """Custom type tnPsdOdukTtpDmSessionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onDemand", 1),
          ("proActive", 2))
    )


_TnPsdOdukTtpDmSessionType_Type.__name__ = "Integer32"
_TnPsdOdukTtpDmSessionType_Object = MibTableColumn
tnPsdOdukTtpDmSessionType = _TnPsdOdukTtpDmSessionType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 5, 1, 2),
    _TnPsdOdukTtpDmSessionType_Type()
)
tnPsdOdukTtpDmSessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdOdukTtpDmSessionType.setStatus("current")


class _TnPsdOdukTtpDmStart_Type(TruthValue):
    """Custom type tnPsdOdukTtpDmStart based on TruthValue"""
    defaultValue = 2


_TnPsdOdukTtpDmStart_Type.__name__ = "TruthValue"
_TnPsdOdukTtpDmStart_Object = MibTableColumn
tnPsdOdukTtpDmStart = _TnPsdOdukTtpDmStart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 5, 1, 3),
    _TnPsdOdukTtpDmStart_Type()
)
tnPsdOdukTtpDmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdOdukTtpDmStart.setStatus("current")
_TnPsdOdukTtpDmOnDemandResultTable_Object = MibTable
tnPsdOdukTtpDmOnDemandResultTable = _TnPsdOdukTtpDmOnDemandResultTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 6)
)
if mibBuilder.loadTexts:
    tnPsdOdukTtpDmOnDemandResultTable.setStatus("current")
_TnPsdOdukTtpDmOnDemandResultEntry_Object = MibTableRow
tnPsdOdukTtpDmOnDemandResultEntry = _TnPsdOdukTtpDmOnDemandResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 6, 1)
)
tnPsdOdukTtpDmOnDemandResultEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnPsdOdukTtpDmOnDemandResultEntry.setStatus("current")


class _TnPsdOdukTtpDmOnDemandResultStatus_Type(Integer32):
    """Custom type tnPsdOdukTtpDmOnDemandResultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("terminated", 2),
          ("finished", 3))
    )


_TnPsdOdukTtpDmOnDemandResultStatus_Type.__name__ = "Integer32"
_TnPsdOdukTtpDmOnDemandResultStatus_Object = MibTableColumn
tnPsdOdukTtpDmOnDemandResultStatus = _TnPsdOdukTtpDmOnDemandResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 6, 1, 1),
    _TnPsdOdukTtpDmOnDemandResultStatus_Type()
)
tnPsdOdukTtpDmOnDemandResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOdukTtpDmOnDemandResultStatus.setStatus("current")
_TnPsdOdukTtpDmOnDemandResultRoundTrip_Type = Integer32
_TnPsdOdukTtpDmOnDemandResultRoundTrip_Object = MibTableColumn
tnPsdOdukTtpDmOnDemandResultRoundTrip = _TnPsdOdukTtpDmOnDemandResultRoundTrip_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 6, 1, 2),
    _TnPsdOdukTtpDmOnDemandResultRoundTrip_Type()
)
tnPsdOdukTtpDmOnDemandResultRoundTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOdukTtpDmOnDemandResultRoundTrip.setStatus("current")
if mibBuilder.loadTexts:
    tnPsdOdukTtpDmOnDemandResultRoundTrip.setUnits("microseconds")
_TnPsdOdukTtpPrbsTable_Object = MibTable
tnPsdOdukTtpPrbsTable = _TnPsdOdukTtpPrbsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7)
)
if mibBuilder.loadTexts:
    tnPsdOdukTtpPrbsTable.setStatus("current")
_TnPsdOdukTtpPrbsEntry_Object = MibTableRow
tnPsdOdukTtpPrbsEntry = _TnPsdOdukTtpPrbsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7, 1)
)
tnPsdOdukTtpPrbsEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnPsdOdukTtpPrbsEntry.setStatus("current")


class _TnPsdOdukTtpPrbsGenerator_Type(TmnxEnabledDisabled):
    """Custom type tnPsdOdukTtpPrbsGenerator based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnPsdOdukTtpPrbsGenerator_Type.__name__ = "TmnxEnabledDisabled"
_TnPsdOdukTtpPrbsGenerator_Object = MibTableColumn
tnPsdOdukTtpPrbsGenerator = _TnPsdOdukTtpPrbsGenerator_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7, 1, 1),
    _TnPsdOdukTtpPrbsGenerator_Type()
)
tnPsdOdukTtpPrbsGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdOdukTtpPrbsGenerator.setStatus("current")


class _TnPsdOdukTtpPrbsGeneratorInvert_Type(TruthValue):
    """Custom type tnPsdOdukTtpPrbsGeneratorInvert based on TruthValue"""
    defaultValue = 2


_TnPsdOdukTtpPrbsGeneratorInvert_Type.__name__ = "TruthValue"
_TnPsdOdukTtpPrbsGeneratorInvert_Object = MibTableColumn
tnPsdOdukTtpPrbsGeneratorInvert = _TnPsdOdukTtpPrbsGeneratorInvert_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7, 1, 2),
    _TnPsdOdukTtpPrbsGeneratorInvert_Type()
)
tnPsdOdukTtpPrbsGeneratorInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdOdukTtpPrbsGeneratorInvert.setStatus("current")


class _TnPsdOdukTtpPrbsMonitor_Type(TmnxEnabledDisabled):
    """Custom type tnPsdOdukTtpPrbsMonitor based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnPsdOdukTtpPrbsMonitor_Type.__name__ = "TmnxEnabledDisabled"
_TnPsdOdukTtpPrbsMonitor_Object = MibTableColumn
tnPsdOdukTtpPrbsMonitor = _TnPsdOdukTtpPrbsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7, 1, 3),
    _TnPsdOdukTtpPrbsMonitor_Type()
)
tnPsdOdukTtpPrbsMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdOdukTtpPrbsMonitor.setStatus("current")


class _TnPsdOdukTtpPrbsMonitorInvert_Type(TruthValue):
    """Custom type tnPsdOdukTtpPrbsMonitorInvert based on TruthValue"""
    defaultValue = 2


_TnPsdOdukTtpPrbsMonitorInvert_Type.__name__ = "TruthValue"
_TnPsdOdukTtpPrbsMonitorInvert_Object = MibTableColumn
tnPsdOdukTtpPrbsMonitorInvert = _TnPsdOdukTtpPrbsMonitorInvert_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7, 1, 4),
    _TnPsdOdukTtpPrbsMonitorInvert_Type()
)
tnPsdOdukTtpPrbsMonitorInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdOdukTtpPrbsMonitorInvert.setStatus("current")


class _TnPsdOdukTtpPrbsErrorPropagation_Type(TruthValue):
    """Custom type tnPsdOdukTtpPrbsErrorPropagation based on TruthValue"""
    defaultValue = 2


_TnPsdOdukTtpPrbsErrorPropagation_Type.__name__ = "TruthValue"
_TnPsdOdukTtpPrbsErrorPropagation_Object = MibTableColumn
tnPsdOdukTtpPrbsErrorPropagation = _TnPsdOdukTtpPrbsErrorPropagation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7, 1, 5),
    _TnPsdOdukTtpPrbsErrorPropagation_Type()
)
tnPsdOdukTtpPrbsErrorPropagation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdOdukTtpPrbsErrorPropagation.setStatus("current")
_TnPsdOdukTtpPrbsTestResultTable_Object = MibTable
tnPsdOdukTtpPrbsTestResultTable = _TnPsdOdukTtpPrbsTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 8)
)
if mibBuilder.loadTexts:
    tnPsdOdukTtpPrbsTestResultTable.setStatus("current")
_TnPsdOdukTtpPrbsTestResultEntry_Object = MibTableRow
tnPsdOdukTtpPrbsTestResultEntry = _TnPsdOdukTtpPrbsTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 8, 1)
)
tnPsdOdukTtpPrbsTestResultEntry.setIndexNames(
    (0, "TROPIC-OTH-MIB", "tnOthIfIndex"),
    (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"),
)
if mibBuilder.loadTexts:
    tnPsdOdukTtpPrbsTestResultEntry.setStatus("current")
_TnPsdOdukTtpPrbsLockTime_Type = Unsigned32
_TnPsdOdukTtpPrbsLockTime_Object = MibTableColumn
tnPsdOdukTtpPrbsLockTime = _TnPsdOdukTtpPrbsLockTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 8, 1, 1),
    _TnPsdOdukTtpPrbsLockTime_Type()
)
tnPsdOdukTtpPrbsLockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOdukTtpPrbsLockTime.setStatus("current")
_TnPsdOdukTtpPrbsTSE_Type = Counter32
_TnPsdOdukTtpPrbsTSE_Object = MibTableColumn
tnPsdOdukTtpPrbsTSE = _TnPsdOdukTtpPrbsTSE_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 8, 1, 2),
    _TnPsdOdukTtpPrbsTSE_Type()
)
tnPsdOdukTtpPrbsTSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOdukTtpPrbsTSE.setStatus("current")


class _TnPsdOdukTtpPrbsBitErrorRate_Type(SnmpAdminString):
    """Custom type tnPsdOdukTtpPrbsBitErrorRate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_TnPsdOdukTtpPrbsBitErrorRate_Type.__name__ = "SnmpAdminString"
_TnPsdOdukTtpPrbsBitErrorRate_Object = MibTableColumn
tnPsdOdukTtpPrbsBitErrorRate = _TnPsdOdukTtpPrbsBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 8, 1, 3),
    _TnPsdOdukTtpPrbsBitErrorRate_Type()
)
tnPsdOdukTtpPrbsBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOdukTtpPrbsBitErrorRate.setStatus("current")
_TnPsdOtnConformance_ObjectIdentity = ObjectIdentity
tnPsdOtnConformance = _TnPsdOtnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2)
)
_TnPsdOtnGroups_ObjectIdentity = ObjectIdentity
tnPsdOtnGroups = _TnPsdOtnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2)
)
_TnPsdCfm_ObjectIdentity = ObjectIdentity
tnPsdCfm = _TnPsdCfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12)
)
_TnPsdCfmNotifs_ObjectIdentity = ObjectIdentity
tnPsdCfmNotifs = _TnPsdCfmNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 0)
)
_TnPsdCfmObjects_ObjectIdentity = ObjectIdentity
tnPsdCfmObjects = _TnPsdCfmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1)
)


class _TnPsdCfmTransportIdentifier_Type(TropicPsdTransportIdentifier):
    """Custom type tnPsdCfmTransportIdentifier based on TropicPsdTransportIdentifier"""
    defaultValue = 33024


_TnPsdCfmTransportIdentifier_Type.__name__ = "TropicPsdTransportIdentifier"
_TnPsdCfmTransportIdentifier_Object = MibScalar
tnPsdCfmTransportIdentifier = _TnPsdCfmTransportIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 1),
    _TnPsdCfmTransportIdentifier_Type()
)
tnPsdCfmTransportIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdCfmTransportIdentifier.setStatus("current")
_TnPsdOamEthCfmPingCtlTable_Object = MibTable
tnPsdOamEthCfmPingCtlTable = _TnPsdOamEthCfmPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2)
)
if mibBuilder.loadTexts:
    tnPsdOamEthCfmPingCtlTable.setStatus("current")
_TnPsdOamEthCfmPingCtlEntry_Object = MibTableRow
tnPsdOamEthCfmPingCtlEntry = _TnPsdOamEthCfmPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnPsdOamEthCfmPingCtlEntry.setStatus("current")


class _TnPsdOamEthCfmPingCtlPriority_Type(TropicPsdPriorityValue):
    """Custom type tnPsdOamEthCfmPingCtlPriority based on TropicPsdPriorityValue"""
    defaultValue = 7


_TnPsdOamEthCfmPingCtlPriority_Type.__name__ = "TropicPsdPriorityValue"
_TnPsdOamEthCfmPingCtlPriority_Object = MibTableColumn
tnPsdOamEthCfmPingCtlPriority = _TnPsdOamEthCfmPingCtlPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2, 1, 1),
    _TnPsdOamEthCfmPingCtlPriority_Type()
)
tnPsdOamEthCfmPingCtlPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmPingCtlPriority.setStatus("current")


class _TnPsdOamEthCfmPingCtlAvailFlrThreshold_Type(Unsigned32):
    """Custom type tnPsdOamEthCfmPingCtlAvailFlrThreshold based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TnPsdOamEthCfmPingCtlAvailFlrThreshold_Type.__name__ = "Unsigned32"
_TnPsdOamEthCfmPingCtlAvailFlrThreshold_Object = MibTableColumn
tnPsdOamEthCfmPingCtlAvailFlrThreshold = _TnPsdOamEthCfmPingCtlAvailFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2, 1, 2),
    _TnPsdOamEthCfmPingCtlAvailFlrThreshold_Type()
)
tnPsdOamEthCfmPingCtlAvailFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmPingCtlAvailFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmPingCtlAvailFlrThreshold.setUnits("percent")


class _TnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals_Type(Unsigned32):
    """Custom type tnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals_Type.__name__ = "Unsigned32"
_TnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals_Object = MibTableColumn
tnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals = _TnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2, 1, 3),
    _TnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals_Type()
)
tnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals.setStatus("current")


class _TnPsdOamEthCfmPingCtlAvailFlrInterval15Min_Type(Unsigned32):
    """Custom type tnPsdOamEthCfmPingCtlAvailFlrInterval15Min based on Unsigned32"""
    defaultValue = 60


_TnPsdOamEthCfmPingCtlAvailFlrInterval15Min_Type.__name__ = "Unsigned32"
_TnPsdOamEthCfmPingCtlAvailFlrInterval15Min_Object = MibTableColumn
tnPsdOamEthCfmPingCtlAvailFlrInterval15Min = _TnPsdOamEthCfmPingCtlAvailFlrInterval15Min_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2, 1, 4),
    _TnPsdOamEthCfmPingCtlAvailFlrInterval15Min_Type()
)
tnPsdOamEthCfmPingCtlAvailFlrInterval15Min.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmPingCtlAvailFlrInterval15Min.setStatus("current")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmPingCtlAvailFlrInterval15Min.setUnits("seconds")


class _TnPsdOamEthCfmPingCtlAvailFlrInterval1Day_Type(Unsigned32):
    """Custom type tnPsdOamEthCfmPingCtlAvailFlrInterval1Day based on Unsigned32"""
    defaultValue = 60


_TnPsdOamEthCfmPingCtlAvailFlrInterval1Day_Type.__name__ = "Unsigned32"
_TnPsdOamEthCfmPingCtlAvailFlrInterval1Day_Object = MibTableColumn
tnPsdOamEthCfmPingCtlAvailFlrInterval1Day = _TnPsdOamEthCfmPingCtlAvailFlrInterval1Day_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2, 1, 5),
    _TnPsdOamEthCfmPingCtlAvailFlrInterval1Day_Type()
)
tnPsdOamEthCfmPingCtlAvailFlrInterval1Day.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmPingCtlAvailFlrInterval1Day.setStatus("current")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmPingCtlAvailFlrInterval1Day.setUnits("seconds")
_TnPsdOamEthCfmTestTable_Object = MibTable
tnPsdOamEthCfmTestTable = _TnPsdOamEthCfmTestTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3)
)
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestTable.setStatus("current")
_TnPsdOamEthCfmTestEntry_Object = MibTableRow
tnPsdOamEthCfmTestEntry = _TnPsdOamEthCfmTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1)
)
tnPsdOamEthCfmTestEntry.setIndexNames(
    (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestSwitchId"),
    (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestSrcMdIndex"),
    (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestSrcMaIndex"),
    (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestSrcMepId"),
    (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestMode"),
    (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestPriority"),
    (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestInterval"),
    (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestSize"),
    (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestTgtMacAddr"),
)
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestEntry.setStatus("current")


class _TnPsdOamEthCfmTestSwitchId_Type(TnSwitchID):
    """Custom type tnPsdOamEthCfmTestSwitchId based on TnSwitchID"""
    subtypeSpec = TnSwitchID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnPsdOamEthCfmTestSwitchId_Type.__name__ = "TnSwitchID"
_TnPsdOamEthCfmTestSwitchId_Object = MibTableColumn
tnPsdOamEthCfmTestSwitchId = _TnPsdOamEthCfmTestSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 1),
    _TnPsdOamEthCfmTestSwitchId_Type()
)
tnPsdOamEthCfmTestSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestSwitchId.setStatus("current")
_TnPsdOamEthCfmTestSrcMdIndex_Type = Unsigned32
_TnPsdOamEthCfmTestSrcMdIndex_Object = MibTableColumn
tnPsdOamEthCfmTestSrcMdIndex = _TnPsdOamEthCfmTestSrcMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 2),
    _TnPsdOamEthCfmTestSrcMdIndex_Type()
)
tnPsdOamEthCfmTestSrcMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestSrcMdIndex.setStatus("current")
_TnPsdOamEthCfmTestSrcMaIndex_Type = Unsigned32
_TnPsdOamEthCfmTestSrcMaIndex_Object = MibTableColumn
tnPsdOamEthCfmTestSrcMaIndex = _TnPsdOamEthCfmTestSrcMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 3),
    _TnPsdOamEthCfmTestSrcMaIndex_Type()
)
tnPsdOamEthCfmTestSrcMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestSrcMaIndex.setStatus("current")
_TnPsdOamEthCfmTestSrcMepId_Type = Dot1agCfmMepIdOrZero
_TnPsdOamEthCfmTestSrcMepId_Object = MibTableColumn
tnPsdOamEthCfmTestSrcMepId = _TnPsdOamEthCfmTestSrcMepId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 4),
    _TnPsdOamEthCfmTestSrcMepId_Type()
)
tnPsdOamEthCfmTestSrcMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestSrcMepId.setStatus("current")
_TnPsdOamEthCfmTestMode_Type = AluWdmPmonPolicyType
_TnPsdOamEthCfmTestMode_Object = MibTableColumn
tnPsdOamEthCfmTestMode = _TnPsdOamEthCfmTestMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 5),
    _TnPsdOamEthCfmTestMode_Type()
)
tnPsdOamEthCfmTestMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestMode.setStatus("current")
_TnPsdOamEthCfmTestPriority_Type = TropicPsdPriorityValue
_TnPsdOamEthCfmTestPriority_Object = MibTableColumn
tnPsdOamEthCfmTestPriority = _TnPsdOamEthCfmTestPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 6),
    _TnPsdOamEthCfmTestPriority_Type()
)
tnPsdOamEthCfmTestPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestPriority.setStatus("current")
_TnPsdOamEthCfmTestInterval_Type = Unsigned32
_TnPsdOamEthCfmTestInterval_Object = MibTableColumn
tnPsdOamEthCfmTestInterval = _TnPsdOamEthCfmTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 7),
    _TnPsdOamEthCfmTestInterval_Type()
)
tnPsdOamEthCfmTestInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestInterval.setUnits("milliseconds")
_TnPsdOamEthCfmTestSize_Type = Unsigned32
_TnPsdOamEthCfmTestSize_Object = MibTableColumn
tnPsdOamEthCfmTestSize = _TnPsdOamEthCfmTestSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 8),
    _TnPsdOamEthCfmTestSize_Type()
)
tnPsdOamEthCfmTestSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestSize.setStatus("current")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestSize.setUnits("octets")
_TnPsdOamEthCfmTestTgtMacAddr_Type = MacAddress
_TnPsdOamEthCfmTestTgtMacAddr_Object = MibTableColumn
tnPsdOamEthCfmTestTgtMacAddr = _TnPsdOamEthCfmTestTgtMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 9),
    _TnPsdOamEthCfmTestTgtMacAddr_Type()
)
tnPsdOamEthCfmTestTgtMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestTgtMacAddr.setStatus("current")


class _TnPsdOamEthCfmTestName_Type(SnmpAdminString):
    """Custom type tnPsdOamEthCfmTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TnPsdOamEthCfmTestName_Type.__name__ = "SnmpAdminString"
_TnPsdOamEthCfmTestName_Object = MibTableColumn
tnPsdOamEthCfmTestName = _TnPsdOamEthCfmTestName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 10),
    _TnPsdOamEthCfmTestName_Type()
)
tnPsdOamEthCfmTestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPsdOamEthCfmTestName.setStatus("current")
_TnPsdDot1agCfmMepDmTWTestTable_Object = MibTable
tnPsdDot1agCfmMepDmTWTestTable = _TnPsdDot1agCfmMepDmTWTestTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 4)
)
if mibBuilder.loadTexts:
    tnPsdDot1agCfmMepDmTWTestTable.setStatus("current")
_TnPsdDot1agCfmMepDmTWTestEntry_Object = MibTableRow
tnPsdDot1agCfmMepDmTWTestEntry = _TnPsdDot1agCfmMepDmTWTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnPsdDot1agCfmMepDmTWTestEntry.setStatus("current")


class _TnPsdDot1agCfmMepDmTWTestStatus_Type(TmnxEnabledDisabled):
    """Custom type tnPsdDot1agCfmMepDmTWTestStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnPsdDot1agCfmMepDmTWTestStatus_Type.__name__ = "TmnxEnabledDisabled"
_TnPsdDot1agCfmMepDmTWTestStatus_Object = MibTableColumn
tnPsdDot1agCfmMepDmTWTestStatus = _TnPsdDot1agCfmMepDmTWTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 4, 1, 1),
    _TnPsdDot1agCfmMepDmTWTestStatus_Type()
)
tnPsdDot1agCfmMepDmTWTestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdDot1agCfmMepDmTWTestStatus.setStatus("current")
_TnPsdDot1agCfmMepSlmTWTestTable_Object = MibTable
tnPsdDot1agCfmMepSlmTWTestTable = _TnPsdDot1agCfmMepSlmTWTestTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 5)
)
if mibBuilder.loadTexts:
    tnPsdDot1agCfmMepSlmTWTestTable.setStatus("current")
_TnPsdDot1agCfmMepSlmTWTestEntry_Object = MibTableRow
tnPsdDot1agCfmMepSlmTWTestEntry = _TnPsdDot1agCfmMepSlmTWTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tnPsdDot1agCfmMepSlmTWTestEntry.setStatus("current")


class _TnPsdDot1agCfmMepSlmTWInterval_Type(Dot1agCfmCcmInterval):
    """Custom type tnPsdDot1agCfmMepSlmTWInterval based on Dot1agCfmCcmInterval"""
    defaultValue = 4


_TnPsdDot1agCfmMepSlmTWInterval_Type.__name__ = "Dot1agCfmCcmInterval"
_TnPsdDot1agCfmMepSlmTWInterval_Object = MibTableColumn
tnPsdDot1agCfmMepSlmTWInterval = _TnPsdDot1agCfmMepSlmTWInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 5, 1, 1),
    _TnPsdDot1agCfmMepSlmTWInterval_Type()
)
tnPsdDot1agCfmMepSlmTWInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPsdDot1agCfmMepSlmTWInterval.setStatus("current")
_TnPsdSoamTable_Object = MibTable
tnPsdSoamTable = _TnPsdSoamTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 6)
)
if mibBuilder.loadTexts:
    tnPsdSoamTable.setStatus("current")
_TnPsdSoamEntry_Object = MibTableRow
tnPsdSoamEntry = _TnPsdSoamEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 6, 1)
)
tnPsdSoamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPsdSoamEntry.setStatus("current")


class _TnPsdSoamEnable_Type(TruthValue):
    """Custom type tnPsdSoamEnable based on TruthValue"""
    defaultValue = 2


_TnPsdSoamEnable_Type.__name__ = "TruthValue"
_TnPsdSoamEnable_Object = MibTableColumn
tnPsdSoamEnable = _TnPsdSoamEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 6, 1, 1),
    _TnPsdSoamEnable_Type()
)
tnPsdSoamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdSoamEnable.setStatus("current")
_TnPsdCfmConformance_ObjectIdentity = ObjectIdentity
tnPsdCfmConformance = _TnPsdCfmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 2)
)
_TnPsdCfmGroups_ObjectIdentity = ObjectIdentity
tnPsdCfmGroups = _TnPsdCfmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 2, 2)
)
_TnPsdPm_ObjectIdentity = ObjectIdentity
tnPsdPm = _TnPsdPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13)
)
_TnPsdPmNotifs_ObjectIdentity = ObjectIdentity
tnPsdPmNotifs = _TnPsdPmNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 0)
)
_TnPsdPmObjects_ObjectIdentity = ObjectIdentity
tnPsdPmObjects = _TnPsdPmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 1)
)


class _TnPsdPmTcaReportingMethod_Type(Integer32):
    """Custom type tnPsdPmTcaReportingMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transient", 1),
          ("standing", 2))
    )


_TnPsdPmTcaReportingMethod_Type.__name__ = "Integer32"
_TnPsdPmTcaReportingMethod_Object = MibScalar
tnPsdPmTcaReportingMethod = _TnPsdPmTcaReportingMethod_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 1, 1),
    _TnPsdPmTcaReportingMethod_Type()
)
tnPsdPmTcaReportingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdPmTcaReportingMethod.setStatus("current")
_TnPsdEthStatsPortConfigTable_Object = MibTable
tnPsdEthStatsPortConfigTable = _TnPsdEthStatsPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 1, 2)
)
if mibBuilder.loadTexts:
    tnPsdEthStatsPortConfigTable.setStatus("current")
_TnPsdEthStatsPortConfigEntry_Object = MibTableRow
tnPsdEthStatsPortConfigEntry = _TnPsdEthStatsPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 1, 2, 1)
)
tnPsdEthStatsPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"),
)
if mibBuilder.loadTexts:
    tnPsdEthStatsPortConfigEntry.setStatus("current")
_TnPsdEthStatsPortClear_Type = TnCommand
_TnPsdEthStatsPortClear_Object = MibTableColumn
tnPsdEthStatsPortClear = _TnPsdEthStatsPortClear_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 1, 2, 1, 1),
    _TnPsdEthStatsPortClear_Type()
)
tnPsdEthStatsPortClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdEthStatsPortClear.setStatus("current")
_TnPsdPmConformance_ObjectIdentity = ObjectIdentity
tnPsdPmConformance = _TnPsdPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 2)
)
_TnPsdPmGroups_ObjectIdentity = ObjectIdentity
tnPsdPmGroups = _TnPsdPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 2, 2)
)
_TnPsdPowerInput_ObjectIdentity = ObjectIdentity
tnPsdPowerInput = _TnPsdPowerInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 14)
)
_TnPsdPowerInputNotifs_ObjectIdentity = ObjectIdentity
tnPsdPowerInputNotifs = _TnPsdPowerInputNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 14, 0)
)
_TnPsdPowerInputObjects_ObjectIdentity = ObjectIdentity
tnPsdPowerInputObjects = _TnPsdPowerInputObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 14, 1)
)
_TnPsdPowerInputTable_Object = MibTable
tnPsdPowerInputTable = _TnPsdPowerInputTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 14, 1, 1)
)
if mibBuilder.loadTexts:
    tnPsdPowerInputTable.setStatus("current")
_TnPsdPowerInputEntry_Object = MibTableRow
tnPsdPowerInputEntry = _TnPsdPowerInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 14, 1, 1, 1)
)
tnPsdPowerInputEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-PSD-MIB", "tnPsdPowerInputIndex"),
)
if mibBuilder.loadTexts:
    tnPsdPowerInputEntry.setStatus("current")
_TnPsdPowerInputIndex_Type = Unsigned32
_TnPsdPowerInputIndex_Object = MibTableColumn
tnPsdPowerInputIndex = _TnPsdPowerInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 14, 1, 1, 1, 1),
    _TnPsdPowerInputIndex_Type()
)
tnPsdPowerInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPsdPowerInputIndex.setStatus("current")


class _TnPsdPowerInputMonitoring_Type(Integer32):
    """Custom type tnPsdPowerInputMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnPsdPowerInputMonitoring_Type.__name__ = "Integer32"
_TnPsdPowerInputMonitoring_Object = MibTableColumn
tnPsdPowerInputMonitoring = _TnPsdPowerInputMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 14, 1, 1, 1, 2),
    _TnPsdPowerInputMonitoring_Type()
)
tnPsdPowerInputMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPsdPowerInputMonitoring.setStatus("current")
_TnPsdPowerInputConformance_ObjectIdentity = ObjectIdentity
tnPsdPowerInputConformance = _TnPsdPowerInputConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 14, 2)
)
_TnPsdPowerInputGroups_ObjectIdentity = ObjectIdentity
tnPsdPowerInputGroups = _TnPsdPowerInputGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 14, 2, 2)
)
_TnPsdAgentCapability_ObjectIdentity = ObjectIdentity
tnPsdAgentCapability = _TnPsdAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 100)
)
_TnPsdMIBCompliance_ObjectIdentity = ObjectIdentity
tnPsdMIBCompliance = _TnPsdMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200)
)
tnLagCommandEntry.registerAugmentions(
    ("TROPIC-PSD-MIB",
     "tnPsdLagCommandEntry")
)
tnPsdLagCommandEntry.setIndexNames(*tnLagCommandEntry.getIndexNames())
tnNetIfEntry.registerAugmentions(
    ("TROPIC-PSD-MIB",
     "tnPsdNetIfEntry")
)
tnPsdNetIfEntry.setIndexNames(*tnNetIfEntry.getIndexNames())
tnOtukEntry.registerAugmentions(
    ("TROPIC-PSD-MIB",
     "tnPsdOtukEntry")
)
tnPsdOtukEntry.setIndexNames(*tnOtukEntry.getIndexNames())
tnOthOdukNimEntry.registerAugmentions(
    ("TROPIC-PSD-MIB",
     "tnPsdOdukNimEntry")
)
tnPsdOdukNimEntry.setIndexNames(*tnOthOdukNimEntry.getIndexNames())
tnOthOdukTtpEntry.registerAugmentions(
    ("TROPIC-PSD-MIB",
     "tnPsdOdukTtpEntry")
)
tnPsdOdukTtpEntry.setIndexNames(*tnOthOdukTtpEntry.getIndexNames())
tnOthOdukTEntry.registerAugmentions(
    ("TROPIC-PSD-MIB",
     "tnPsdOdukTEntry")
)
tnPsdOdukTEntry.setIndexNames(*tnOthOdukTEntry.getIndexNames())
tnOamPingCtlEntry.registerAugmentions(
    ("TROPIC-PSD-MIB",
     "tnPsdOamEthCfmPingCtlEntry")
)
tnPsdOamEthCfmPingCtlEntry.setIndexNames(*tnOamPingCtlEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("TROPIC-PSD-MIB",
     "tnPsdDot1agCfmMepDmTWTestEntry")
)
tnPsdDot1agCfmMepDmTWTestEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("TROPIC-PSD-MIB",
     "tnPsdDot1agCfmMepSlmTWTestEntry")
)
tnPsdDot1agCfmMepSlmTWTestEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups

tnPsdSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 2, 2, 1)
)
tnPsdSystemGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSystemMode"),
        ("TROPIC-PSD-MIB", "tnPsdSystemModeDescr"),
        ("TROPIC-PSD-MIB", "tnPsdSystemAbnormalState"),
        ("TROPIC-PSD-MIB", "tnPsdSystemSmartConnectLed"))
)
if mibBuilder.loadTexts:
    tnPsdSystemGroup.setStatus("current")

tnPsdShelfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2, 2, 1)
)
tnPsdShelfGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdShelfName"),
        ("TROPIC-PSD-MIB", "tnPsdShelfDescr"),
        ("TROPIC-PSD-MIB", "tnPsdShelfType"),
        ("TROPIC-PSD-MIB", "tnPsdShelfLocation"),
        ("TROPIC-PSD-MIB", "tnPsdShelfLatitude"),
        ("TROPIC-PSD-MIB", "tnPsdShelfLongitude"),
        ("TROPIC-PSD-MIB", "tnPsdShelfAltitude"),
        ("TROPIC-PSD-MIB", "tnPsdShelfRealTimePower"),
        ("TROPIC-PSD-MIB", "tnPsdShelfRestart"))
)
if mibBuilder.loadTexts:
    tnPsdShelfGroup.setStatus("current")

tnPsdSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2, 2, 2)
)
tnPsdSlotGroup.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdSlotType")
)
if mibBuilder.loadTexts:
    tnPsdSlotGroup.setStatus("current")

tnPsdCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2, 2, 3)
)
tnPsdCardGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdCardInvStatus"),
        ("TROPIC-PSD-MIB", "tnPsdCardCompanyID"),
        ("TROPIC-PSD-MIB", "tnPsdCardMnemonic"),
        ("TROPIC-PSD-MIB", "tnPsdCardCLEI"),
        ("TROPIC-PSD-MIB", "tnPsdCardUnitPartNumber"),
        ("TROPIC-PSD-MIB", "tnPsdCardSwPartNumber"),
        ("TROPIC-PSD-MIB", "tnPsdCardFactoryID"),
        ("TROPIC-PSD-MIB", "tnPsdCardSerialNumber"),
        ("TROPIC-PSD-MIB", "tnPsdCardDate"),
        ("TROPIC-PSD-MIB", "tnPsdCardCustInvField"))
)
if mibBuilder.loadTexts:
    tnPsdCardGroup.setStatus("current")

tnPsdSfpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 1)
)
tnPsdSfpGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSfpType"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoInvStatus"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoPhysicalIdentifier"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoClassOfWdm"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoConnectorType"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoTransceiverCode"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoBitRateNominal"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoLinkType"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoLinkMaxLength"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoLinkLengthOverrun"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoLinkLengthUnits"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoLinkLength"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoVendorName"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoVendorOUI"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoPartNumber"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoRevisionNumber"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoWavelength"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoBitRateMaximum"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoBitRateMinimum"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoVendorSerialNumber"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoVendorDate"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoVendorSpecific"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoCLEI"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoAluPartNumber"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoAluSerialNumber"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoIcs"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoNokiaPartNumber"))
)
if mibBuilder.loadTexts:
    tnPsdSfpGroup.setStatus("current")

tnPsdDdmDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 2)
)
tnPsdDdmDataGroup.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdDdmDataValue")
)
if mibBuilder.loadTexts:
    tnPsdDdmDataGroup.setStatus("current")

tnPsdLagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 4)
)
tnPsdLagGroup.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdLagCommandSubgroupSelected")
)
if mibBuilder.loadTexts:
    tnPsdLagGroup.setStatus("current")

tnPsdSfp2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 5)
)
tnPsdSfp2Group.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSfpProgrammedChannel"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoTunable"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoFrequency"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoFrequencyLow"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoFrequencyHigh"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoFrequencyGrid"),
        ("TROPIC-PSD-MIB", "tnPsdSfpInfoTuningStatus"))
)
if mibBuilder.loadTexts:
    tnPsdSfp2Group.setStatus("current")

tnPsdAlsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 8)
)
tnPsdAlsGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdAlsEnabled"),
        ("TROPIC-PSD-MIB", "tnPsdAlsWaitToRestart"),
        ("TROPIC-PSD-MIB", "tnPsdAlsTxTime"),
        ("TROPIC-PSD-MIB", "tnPsdAlsState"),
        ("TROPIC-PSD-MIB", "tnPsdAlsActiveCheck"),
        ("TROPIC-PSD-MIB", "tnPsdAlsActiveCheckForTest"))
)
if mibBuilder.loadTexts:
    tnPsdAlsGroup.setStatus("current")

tnPsdSnmpTrapDestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 2, 2, 1)
)
tnPsdSnmpTrapDestGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestAddrType"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestAddr"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestPort"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestCommunity"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestDyingGasp"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestRowStatus"))
)
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestGroup.setStatus("current")

tnPsdSnmpTrapDest2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 2, 2, 4)
)
tnPsdSnmpTrapDest2Group.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestAddrType"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestAddr"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestPort"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestCommunity"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestDyingGasp"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestRowStatus"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestSnmpVersion"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestUserName"))
)
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDest2Group.setStatus("current")

tnPsdDatabaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5, 2, 2, 1)
)
tnPsdDatabaseGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdDatabaseBackupAndRestoreRemoteHostAddrType"),
        ("TROPIC-PSD-MIB", "tnPsdDatabaseBackupAndRestoreRemoteHostAddr"))
)
if mibBuilder.loadTexts:
    tnPsdDatabaseGroup.setStatus("current")

tnPsdSoftwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 2, 2, 1)
)
tnPsdSoftwareGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSoftwareRemoteHostAddrType"),
        ("TROPIC-PSD-MIB", "tnPsdSoftwareRemoteHostAddr"),
        ("TROPIC-PSD-MIB", "tnPsdShelfIsdStatus"),
        ("TROPIC-PSD-MIB", "tnPsdShelfIsdBuildTime"),
        ("TROPIC-PSD-MIB", "tnPsdShelfIsdItemCode"),
        ("TROPIC-PSD-MIB", "tnPsdShelfIsdMaintenance"),
        ("TROPIC-PSD-MIB", "tnPsdShelfIsdCompatible"),
        ("TROPIC-PSD-MIB", "tnPsdShelfIsdSwRelease"))
)
if mibBuilder.loadTexts:
    tnPsdSoftwareGroup.setStatus("current")

tnPsdTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 2, 2, 1)
)
tnPsdTimeGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdShelfTime"),
        ("TROPIC-PSD-MIB", "tnPsdNtpState"),
        ("TROPIC-PSD-MIB", "tnPsdNtpStatus"),
        ("TROPIC-PSD-MIB", "tnPsdNtpStratum"),
        ("TROPIC-PSD-MIB", "tnPsdNtpAccuracy"),
        ("TROPIC-PSD-MIB", "tnPsdNtpServerAddrType"),
        ("TROPIC-PSD-MIB", "tnPsdNtpServerAddr"),
        ("TROPIC-PSD-MIB", "tnPsdNtpServerSystemServer"),
        ("TROPIC-PSD-MIB", "tnPsdNtpServerReachable"),
        ("TROPIC-PSD-MIB", "tnPsdNtpServerReachabilityData"),
        ("TROPIC-PSD-MIB", "tnPsdNtpServerPollTime"))
)
if mibBuilder.loadTexts:
    tnPsdTimeGroup.setStatus("current")

tnPsdIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 1)
)
tnPsdIpGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdEnforceSrcIpV4ToLoopbackIpV4"),
        ("TROPIC-PSD-MIB", "tnPsdEnforceSrcIpV6ToLoopbackIpV6"),
        ("TROPIC-PSD-MIB", "tnPsdManualIpv4AddressAddrType"),
        ("TROPIC-PSD-MIB", "tnPsdManualIpv4AddressAddr"),
        ("TROPIC-PSD-MIB", "tnPsdManualIpv4AddressPrefixLen"),
        ("TROPIC-PSD-MIB", "tnPsdManualIpv6AddressAddrType"),
        ("TROPIC-PSD-MIB", "tnPsdManualIpv6AddressAddr"),
        ("TROPIC-PSD-MIB", "tnPsdManualIpv6AddressPrefixLen"),
        ("TROPIC-PSD-MIB", "tnPsdActualIpAddressPrefixLen"),
        ("TROPIC-PSD-MIB", "tnPsdDhcpClientV4Enabled"),
        ("TROPIC-PSD-MIB", "tnPsdStaticRouteMetric"),
        ("TROPIC-PSD-MIB", "tnPsdStaticRouteRowStatus"),
        ("TROPIC-PSD-MIB", "tnPsdActualRouteMetric"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfIpAddrType"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfIpAddr"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfIpPrefixLen"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfOperStatus"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfRemoteIpAddrType"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfRemoteIpAddr"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfIp6AddrType"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfIp6Addr"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfIp6PrefixLen"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfRemoteIp6AddrType"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfRemoteIp6Addr"))
)
if mibBuilder.loadTexts:
    tnPsdIpGroup.setStatus("current")

tnPsdIp2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 5)
)
tnPsdIp2Group.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdNetIfMonitoring"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfMonitoring6"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityTypeOfOperation"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityPriorityEgress"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityDropEligibleEgress"))
)
if mibBuilder.loadTexts:
    tnPsdIp2Group.setStatus("current")

tnPsdIp3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 8)
)
tnPsdIp3Group.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdProxyArp")
)
if mibBuilder.loadTexts:
    tnPsdIp3Group.setStatus("current")

tnPsdFaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 2, 2, 1)
)
tnPsdFaultGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdAsapName"),
        ("TROPIC-PSD-MIB", "tnPsdAsapFaultProfileSeverity"),
        ("TROPIC-PSD-MIB", "tnPsdAsapFaultProfileReported"),
        ("TROPIC-PSD-MIB", "tnPsdAsapFaultProfileServiceAffecting"),
        ("TROPIC-PSD-MIB", "tnPsdAsapFaultProfileAlarmText"),
        ("TROPIC-PSD-MIB", "tnPsdFaultAlarmRaiseTime"),
        ("TROPIC-PSD-MIB", "tnPsdFaultAlarmClearTime"))
)
if mibBuilder.loadTexts:
    tnPsdFaultGroup.setStatus("current")

tnPsdSysDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10, 2, 2, 1)
)
tnPsdSysDiscoveryGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSysDiscoveryServerAddrType"),
        ("TROPIC-PSD-MIB", "tnPsdSysDiscoveryServerAddr"))
)
if mibBuilder.loadTexts:
    tnPsdSysDiscoveryGroup.setStatus("current")

tnPsdOtnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2, 1)
)
tnPsdOtnGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdOtukSapiAccepted"),
        ("TROPIC-PSD-MIB", "tnPsdOtukSapiExpected"),
        ("TROPIC-PSD-MIB", "tnPsdOtukSapiTransmitted"),
        ("TROPIC-PSD-MIB", "tnPsdOtukDapiAccepted"),
        ("TROPIC-PSD-MIB", "tnPsdOtukDapiExpected"),
        ("TROPIC-PSD-MIB", "tnPsdOtukDapiTransmitted"),
        ("TROPIC-PSD-MIB", "tnPsdOdukNimSapiAccepted"),
        ("TROPIC-PSD-MIB", "tnPsdOdukNimSapiExpected"),
        ("TROPIC-PSD-MIB", "tnPsdOdukNimDapiAccepted"),
        ("TROPIC-PSD-MIB", "tnPsdOdukNimDapiExpected"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpSapiAccepted"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpSapiExpected"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpSapiTransmitted"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpDapiAccepted"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpDapiExpected"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpDapiTransmitted"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTSapiAccepted"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTSapiExpected"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTSapiTransmitted"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTDapiAccepted"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTDapiExpected"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTDapiTransmitted"))
)
if mibBuilder.loadTexts:
    tnPsdOtnGroup.setStatus("current")

tnPsdOtn2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2, 3)
)
tnPsdOtn2Group.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdOdukTtpDmReflection"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpDmSessionType"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpDmStart"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpDmOnDemandResultStatus"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpDmOnDemandResultRoundTrip"))
)
if mibBuilder.loadTexts:
    tnPsdOtn2Group.setStatus("current")

tnPsdOtn3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2, 5)
)
tnPsdOtn3Group.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsGenerator"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsGeneratorInvert"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsMonitor"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsMonitorInvert"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsErrorPropagation"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsLockTime"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsTSE"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsBitErrorRate"))
)
if mibBuilder.loadTexts:
    tnPsdOtn3Group.setStatus("current")

tnPsdCfmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 2, 2, 1)
)
tnPsdCfmGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdCfmTransportIdentifier"),
        ("TROPIC-PSD-MIB", "tnPsdOamEthCfmPingCtlPriority"),
        ("TROPIC-PSD-MIB", "tnPsdOamEthCfmPingCtlAvailFlrThreshold"),
        ("TROPIC-PSD-MIB", "tnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals"),
        ("TROPIC-PSD-MIB", "tnPsdOamEthCfmPingCtlAvailFlrInterval15Min"),
        ("TROPIC-PSD-MIB", "tnPsdOamEthCfmPingCtlAvailFlrInterval1Day"),
        ("TROPIC-PSD-MIB", "tnPsdOamEthCfmTestName"),
        ("TROPIC-PSD-MIB", "tnPsdDot1agCfmMepDmTWTestStatus"),
        ("TROPIC-PSD-MIB", "tnPsdDot1agCfmMepSlmTWInterval"),
        ("TROPIC-PSD-MIB", "tnPsdSoamEnable"))
)
if mibBuilder.loadTexts:
    tnPsdCfmGroup.setStatus("current")

tnPsdPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 2, 2, 1)
)
tnPsdPmGroup.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdPmTcaReportingMethod")
)
if mibBuilder.loadTexts:
    tnPsdPmGroup.setStatus("current")

tnPsdPmEthStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 2, 2, 2)
)
tnPsdPmEthStatsGroup.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdEthStatsPortClear")
)
if mibBuilder.loadTexts:
    tnPsdPmEthStatsGroup.setStatus("current")

tnPsdPowerInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 14, 2, 2, 1)
)
tnPsdPowerInputGroup.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdPowerInputMonitoring")
)
if mibBuilder.loadTexts:
    tnPsdPowerInputGroup.setStatus("current")


# Notification objects

tnPsdDyingGaspNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 0, 1)
)
if mibBuilder.loadTexts:
    tnPsdDyingGaspNotif.setStatus(
        "current"
    )

tnPsdShelfConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 0, 2)
)
tnPsdShelfConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdShelfConfigChangeNotif.setStatus(
        "current"
    )

tnPsdShelfRestartConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 0, 3)
)
tnPsdShelfRestartConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdShelfRestartConfigChangeNotif.setStatus(
        "current"
    )

tnPsdSwRestartNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 0, 4)
)
tnPsdSwRestartNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnPsdSwRestartNotif.setStatus(
        "current"
    )

tnPsdSfpConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 0, 1)
)
tnPsdSfpConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdSfpConfigChangeNotif.setStatus(
        "current"
    )

tnPsdSfpInfoTuningStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 0, 2)
)
tnPsdSfpInfoTuningStatusChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnPsdSfpInfoTuningStatusChangeNotif.setStatus(
        "current"
    )

tnPsdSfpInfoTuningOkNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 0, 3)
)
tnPsdSfpInfoTuningOkNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnPsdSfpInfoTuningOkNotif.setStatus(
        "current"
    )

tnPsdAlsConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 0, 4)
)
tnPsdAlsConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdAlsConfigChangeNotif.setStatus(
        "current"
    )

tnPsdAlsChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 0, 5)
)
tnPsdAlsChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnPsdAlsChangeNotif.setStatus(
        "current"
    )

tnPsdSnmpTrapDestConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 0, 1)
)
tnPsdSnmpTrapDestConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestConfigChangeNotif.setStatus(
        "current"
    )

tnPsdSnmpTrapDestCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 0, 2)
)
tnPsdSnmpTrapDestCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestCreationNotif.setStatus(
        "current"
    )

tnPsdSnmpTrapDestDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 0, 3)
)
tnPsdSnmpTrapDestDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdSnmpTrapDestDeletionNotif.setStatus(
        "current"
    )

tnPsdSwActivateNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 0, 1)
)
tnPsdSwActivateNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnPsdSwActivateNotif.setStatus(
        "current"
    )

tnPsdSwCommitNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 0, 2)
)
tnPsdSwCommitNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
)
if mibBuilder.loadTexts:
    tnPsdSwCommitNotif.setStatus(
        "current"
    )

tnPsdShelfTimeConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 0, 1)
)
tnPsdShelfTimeConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdShelfTimeConfigChangeNotif.setStatus(
        "current"
    )

tnPsdNtpConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 0, 2)
)
tnPsdNtpConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdNtpConfigChangeNotif.setStatus(
        "current"
    )

tnPsdNtpServerConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 0, 3)
)
tnPsdNtpServerConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdNtpServerConfigChangeNotif.setStatus(
        "current"
    )

tnPsdManualIpv4AddressConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 1)
)
tnPsdManualIpv4AddressConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdManualIpv4AddressConfigChangeNotif.setStatus(
        "current"
    )

tnPsdManualIpv6AddressConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 2)
)
tnPsdManualIpv6AddressConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdManualIpv6AddressConfigChangeNotif.setStatus(
        "current"
    )

tnPsdDhcpClientConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 3)
)
tnPsdDhcpClientConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdDhcpClientConfigChangeNotif.setStatus(
        "current"
    )

tnPsdStaticRouteConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 4)
)
tnPsdStaticRouteConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdStaticRouteConfigChangeNotif.setStatus(
        "current"
    )

tnPsdStaticRouteCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 5)
)
tnPsdStaticRouteCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdStaticRouteCreationNotif.setStatus(
        "current"
    )

tnPsdStaticRouteDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 6)
)
tnPsdStaticRouteDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdStaticRouteDeletionNotif.setStatus(
        "current"
    )

tnPsdNetIfOperStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 7)
)
tnPsdNetIfOperStatusChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdNetIfOperStatusChangeNotif.setStatus(
        "current"
    )

tnPsdNetIfConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 8)
)
tnPsdNetIfConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdNetIfConfigChangeNotif.setStatus(
        "current"
    )

tnPsdNetIfEthFacilityConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 9)
)
tnPsdNetIfEthFacilityConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdNetIfEthFacilityConfigChangeNotif.setStatus(
        "current"
    )

tnPsdNetIfEthFacilityCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 10)
)
tnPsdNetIfEthFacilityCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdNetIfEthFacilityCreationNotif.setStatus(
        "current"
    )

tnPsdNetIfEthFacilityDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 11)
)
tnPsdNetIfEthFacilityDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdNetIfEthFacilityDeletionNotif.setStatus(
        "current"
    )

tnPsdProxyArpConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 12)
)
tnPsdProxyArpConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdProxyArpConfigChangeNotif.setStatus(
        "current"
    )

tnPsdAsapConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 0, 1)
)
tnPsdAsapConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdAsapConfigChangeNotif.setStatus(
        "current"
    )

tnPsdAsapFaultProfileConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 0, 2)
)
tnPsdAsapFaultProfileConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdAsapFaultProfileConfigChangeNotif.setStatus(
        "current"
    )

tnPsdFaultConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 0, 3)
)
tnPsdFaultConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdFaultConfigChangeNotif.setStatus(
        "current"
    )

tnPsdOtukConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0, 1)
)
tnPsdOtukConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdOtukConfigChangeNotif.setStatus(
        "current"
    )

tnPsdOdukNimConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0, 2)
)
tnPsdOdukNimConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdOdukNimConfigChangeNotif.setStatus(
        "current"
    )

tnPsdOdukTtpConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0, 3)
)
tnPsdOdukTtpConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdOdukTtpConfigChangeNotif.setStatus(
        "current"
    )

tnPsdOdukTConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0, 4)
)
tnPsdOdukTConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdOdukTConfigChangeNotif.setStatus(
        "current"
    )

tnPsdOdukTtpDmConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0, 5)
)
tnPsdOdukTtpDmConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdOdukTtpDmConfigChangeNotif.setStatus(
        "current"
    )

tnPsdOdukTtpPrbsConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0, 6)
)
tnPsdOdukTtpPrbsConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdOdukTtpPrbsConfigChangeNotif.setStatus(
        "current"
    )

tnPsdDot1agCfmMepDmTWTestConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 0, 2)
)
tnPsdDot1agCfmMepDmTWTestConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdDot1agCfmMepDmTWTestConfigChangeNotif.setStatus(
        "current"
    )

tnPsdDot1agCfmMepSlmTWTestConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 0, 3)
)
tnPsdDot1agCfmMepSlmTWTestConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdDot1agCfmMepSlmTWTestConfigChangeNotif.setStatus(
        "current"
    )

tnPsdSoamConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 0, 4)
)
tnPsdSoamConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdSoamConfigChangeNotif.setStatus(
        "current"
    )

tnPsdEthStatsPortConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 0, 1)
)
tnPsdEthStatsPortConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdEthStatsPortConfigChangeNotif.setStatus(
        "current"
    )

tnPsdPowerInputConfigChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 14, 0, 1)
)
tnPsdPowerInputConfigChangeNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnPsdPowerInputConfigChangeNotif.setStatus(
        "current"
    )


# Notifications groups

tnPsdEquipmentEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2, 2, 4)
)
tnPsdEquipmentEventGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdDyingGaspNotif"),
        ("TROPIC-PSD-MIB", "tnPsdSwRestartNotif"))
)
if mibBuilder.loadTexts:
    tnPsdEquipmentEventGroup.setStatus(
        "current"
    )

tnPsdEquipmentChangeGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2, 2, 5)
)
tnPsdEquipmentChangeGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdShelfConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdShelfRestartConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnPsdEquipmentChangeGroup.setStatus(
        "current"
    )

tnPsdInterfaceConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 3)
)
tnPsdInterfaceConfigChangeNotifGroup.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdSfpConfigChangeNotif")
)
if mibBuilder.loadTexts:
    tnPsdInterfaceConfigChangeNotifGroup.setStatus(
        "current"
    )

tnPsdInterfaceStateChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 6)
)
tnPsdInterfaceStateChangeNotifGroup.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdSfpInfoTuningStatusChangeNotif")
)
if mibBuilder.loadTexts:
    tnPsdInterfaceStateChangeNotifGroup.setStatus(
        "current"
    )

tnPsdInterfaceEventNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 7)
)
tnPsdInterfaceEventNotifGroup.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdSfpInfoTuningOkNotif")
)
if mibBuilder.loadTexts:
    tnPsdInterfaceEventNotifGroup.setStatus(
        "current"
    )

tnPsdAlsNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 9)
)
tnPsdAlsNotifGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdAlsConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdAlsChangeNotif"))
)
if mibBuilder.loadTexts:
    tnPsdAlsNotifGroup.setStatus(
        "current"
    )

tnPsdSnmpConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 2, 2, 2)
)
tnPsdSnmpConfigChangeNotifGroup.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestConfigChangeNotif")
)
if mibBuilder.loadTexts:
    tnPsdSnmpConfigChangeNotifGroup.setStatus(
        "current"
    )

tnPsdSnmpCreDelNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 2, 2, 3)
)
tnPsdSnmpCreDelNotifGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestCreationNotif"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestDeletionNotif"))
)
if mibBuilder.loadTexts:
    tnPsdSnmpCreDelNotifGroup.setStatus(
        "current"
    )

tnPsdSoftwareEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 2, 2, 2)
)
tnPsdSoftwareEventGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSwActivateNotif"),
        ("TROPIC-PSD-MIB", "tnPsdSwCommitNotif"))
)
if mibBuilder.loadTexts:
    tnPsdSoftwareEventGroup.setStatus(
        "current"
    )

tnPsdTimeConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 2, 2, 2)
)
tnPsdTimeConfigChangeNotifGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdShelfTimeConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdNtpConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdNtpServerConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnPsdTimeConfigChangeNotifGroup.setStatus(
        "current"
    )

tnPsdIpConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 2)
)
tnPsdIpConfigChangeNotifGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdManualIpv4AddressConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdManualIpv6AddressConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdDhcpClientConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdStaticRouteConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnPsdIpConfigChangeNotifGroup.setStatus(
        "current"
    )

tnPsdIpCreDelNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 3)
)
tnPsdIpCreDelNotifGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdStaticRouteCreationNotif"),
        ("TROPIC-PSD-MIB", "tnPsdStaticRouteDeletionNotif"))
)
if mibBuilder.loadTexts:
    tnPsdIpCreDelNotifGroup.setStatus(
        "current"
    )

tnPsdIpStateChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 4)
)
tnPsdIpStateChangeNotifGroup.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdNetIfOperStatusChangeNotif")
)
if mibBuilder.loadTexts:
    tnPsdIpStateChangeNotifGroup.setStatus(
        "current"
    )

tnPsdIpConfigChangeNotif2Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 6)
)
tnPsdIpConfigChangeNotif2Group.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdNetIfConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnPsdIpConfigChangeNotif2Group.setStatus(
        "current"
    )

tnPsdIpCreDelNotif2Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 7)
)
tnPsdIpCreDelNotif2Group.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityCreationNotif"),
        ("TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityDeletionNotif"))
)
if mibBuilder.loadTexts:
    tnPsdIpCreDelNotif2Group.setStatus(
        "current"
    )

tnPsdIpConfigChangeNotif3Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 9)
)
tnPsdIpConfigChangeNotif3Group.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdProxyArpConfigChangeNotif")
)
if mibBuilder.loadTexts:
    tnPsdIpConfigChangeNotif3Group.setStatus(
        "current"
    )

tnPsdFaultChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 2, 2, 2)
)
tnPsdFaultChangeNotifGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdAsapConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdAsapFaultProfileConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdFaultConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnPsdFaultChangeNotifGroup.setStatus(
        "current"
    )

tnPsdOtnConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2, 2)
)
tnPsdOtnConfigChangeNotifGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdOtukConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdOdukNimConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTtpConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdOdukTConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnPsdOtnConfigChangeNotifGroup.setStatus(
        "current"
    )

tnPsdOtnConfigChangeNotif2Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2, 4)
)
tnPsdOtnConfigChangeNotif2Group.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdOdukTtpDmConfigChangeNotif")
)
if mibBuilder.loadTexts:
    tnPsdOtnConfigChangeNotif2Group.setStatus(
        "current"
    )

tnPsdOtnConfigChangeNotif3Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2, 6)
)
tnPsdOtnConfigChangeNotif3Group.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsConfigChangeNotif")
)
if mibBuilder.loadTexts:
    tnPsdOtnConfigChangeNotif3Group.setStatus(
        "current"
    )

tnPsdCfmConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 2, 2, 2)
)
tnPsdCfmConfigChangeNotifGroup.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdDot1agCfmMepDmTWTestConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdDot1agCfmMepSlmTWTestConfigChangeNotif"),
        ("TROPIC-PSD-MIB", "tnPsdSoamConfigChangeNotif"))
)
if mibBuilder.loadTexts:
    tnPsdCfmConfigChangeNotifGroup.setStatus(
        "current"
    )

tnPsdPmEthStatsConfigChangeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 2, 2, 3)
)
tnPsdPmEthStatsConfigChangeNotifGroup.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdEthStatsPortConfigChangeNotif")
)
if mibBuilder.loadTexts:
    tnPsdPmEthStatsConfigChangeNotifGroup.setStatus(
        "current"
    )

tnPsdPowerInputNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 14, 2, 2, 2)
)
tnPsdPowerInputNotifGroup.setObjects(
    ("TROPIC-PSD-MIB", "tnPsdPowerInputConfigChangeNotif")
)
if mibBuilder.loadTexts:
    tnPsdPowerInputNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tnPsdR100Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200, 1)
)
tnPsdR100Compliance.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSystemGroup"),
        ("TROPIC-PSD-MIB", "tnPsdShelfGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSlotGroup"),
        ("TROPIC-PSD-MIB", "tnPsdCardGroup"),
        ("TROPIC-PSD-MIB", "tnPsdEquipmentEventGroup"),
        ("TROPIC-PSD-MIB", "tnPsdEquipmentChangeGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSfpGroup"),
        ("TROPIC-PSD-MIB", "tnPsdDdmDataGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpCreDelNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdDatabaseGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSoftwareGroup"),
        ("TROPIC-PSD-MIB", "tnPsdTimeGroup"),
        ("TROPIC-PSD-MIB", "tnPsdTimeConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpStateChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdFaultGroup"),
        ("TROPIC-PSD-MIB", "tnPsdFaultChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSysDiscoveryGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtnGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotifGroup"))
)
if mibBuilder.loadTexts:
    tnPsdR100Compliance.setStatus(
        "current"
    )

tnPsdR110Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200, 2)
)
tnPsdR110Compliance.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSystemGroup"),
        ("TROPIC-PSD-MIB", "tnPsdShelfGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSlotGroup"),
        ("TROPIC-PSD-MIB", "tnPsdCardGroup"),
        ("TROPIC-PSD-MIB", "tnPsdEquipmentEventGroup"),
        ("TROPIC-PSD-MIB", "tnPsdEquipmentChangeGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSfpGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSfp2Group"),
        ("TROPIC-PSD-MIB", "tnPsdDdmDataGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceStateChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceEventNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdLagGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpCreDelNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdDatabaseGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSoftwareGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSoftwareEventGroup"),
        ("TROPIC-PSD-MIB", "tnPsdTimeGroup"),
        ("TROPIC-PSD-MIB", "tnPsdTimeConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIp2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpStateChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdFaultGroup"),
        ("TROPIC-PSD-MIB", "tnPsdFaultChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSysDiscoveryGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtnGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtn2Group"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdCfmGroup"),
        ("TROPIC-PSD-MIB", "tnPsdCfmConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdPmGroup"))
)
if mibBuilder.loadTexts:
    tnPsdR110Compliance.setStatus(
        "current"
    )

tnPsdR200Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200, 3)
)
tnPsdR200Compliance.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSystemGroup"),
        ("TROPIC-PSD-MIB", "tnPsdShelfGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSlotGroup"),
        ("TROPIC-PSD-MIB", "tnPsdCardGroup"),
        ("TROPIC-PSD-MIB", "tnPsdEquipmentEventGroup"),
        ("TROPIC-PSD-MIB", "tnPsdEquipmentChangeGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSfpGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSfp2Group"),
        ("TROPIC-PSD-MIB", "tnPsdDdmDataGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceStateChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceEventNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdLagGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpCreDelNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdDatabaseGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSoftwareGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSoftwareEventGroup"),
        ("TROPIC-PSD-MIB", "tnPsdTimeGroup"),
        ("TROPIC-PSD-MIB", "tnPsdTimeConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIp2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIp3Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif3Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpStateChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdFaultGroup"),
        ("TROPIC-PSD-MIB", "tnPsdFaultChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSysDiscoveryGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtnGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtn2Group"),
        ("TROPIC-PSD-MIB", "tnPsdOtn3Group"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif3Group"),
        ("TROPIC-PSD-MIB", "tnPsdCfmGroup"),
        ("TROPIC-PSD-MIB", "tnPsdCfmConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdPmGroup"))
)
if mibBuilder.loadTexts:
    tnPsdR200Compliance.setStatus(
        "current"
    )

tnPsdR300Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200, 4)
)
tnPsdR300Compliance.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSystemGroup"),
        ("TROPIC-PSD-MIB", "tnPsdShelfGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSlotGroup"),
        ("TROPIC-PSD-MIB", "tnPsdCardGroup"),
        ("TROPIC-PSD-MIB", "tnPsdEquipmentEventGroup"),
        ("TROPIC-PSD-MIB", "tnPsdEquipmentChangeGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSfpGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSfp2Group"),
        ("TROPIC-PSD-MIB", "tnPsdDdmDataGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceStateChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceEventNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdLagGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDest2Group"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpCreDelNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdDatabaseGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSoftwareGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSoftwareEventGroup"),
        ("TROPIC-PSD-MIB", "tnPsdTimeGroup"),
        ("TROPIC-PSD-MIB", "tnPsdTimeConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIp2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIp3Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif3Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpStateChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdFaultGroup"),
        ("TROPIC-PSD-MIB", "tnPsdFaultChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSysDiscoveryGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtnGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtn2Group"),
        ("TROPIC-PSD-MIB", "tnPsdOtn3Group"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif3Group"),
        ("TROPIC-PSD-MIB", "tnPsdCfmGroup"),
        ("TROPIC-PSD-MIB", "tnPsdCfmConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdPmGroup"))
)
if mibBuilder.loadTexts:
    tnPsdR300Compliance.setStatus(
        "current"
    )

tnPsdR400Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200, 5)
)
tnPsdR400Compliance.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSystemGroup"),
        ("TROPIC-PSD-MIB", "tnPsdShelfGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSlotGroup"),
        ("TROPIC-PSD-MIB", "tnPsdCardGroup"),
        ("TROPIC-PSD-MIB", "tnPsdEquipmentEventGroup"),
        ("TROPIC-PSD-MIB", "tnPsdEquipmentChangeGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSfpGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSfp2Group"),
        ("TROPIC-PSD-MIB", "tnPsdDdmDataGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceStateChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceEventNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdLagGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDest2Group"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpCreDelNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdDatabaseGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSoftwareGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSoftwareEventGroup"),
        ("TROPIC-PSD-MIB", "tnPsdTimeGroup"),
        ("TROPIC-PSD-MIB", "tnPsdTimeConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIp2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIp3Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif3Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpStateChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdFaultGroup"),
        ("TROPIC-PSD-MIB", "tnPsdFaultChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSysDiscoveryGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtnGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtn2Group"),
        ("TROPIC-PSD-MIB", "tnPsdOtn3Group"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif3Group"),
        ("TROPIC-PSD-MIB", "tnPsdCfmGroup"),
        ("TROPIC-PSD-MIB", "tnPsdCfmConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdPmGroup"),
        ("TROPIC-PSD-MIB", "tnPsdPmEthStatsGroup"),
        ("TROPIC-PSD-MIB", "tnPsdPmEthStatsConfigChangeNotifGroup"))
)
if mibBuilder.loadTexts:
    tnPsdR400Compliance.setStatus(
        "current"
    )

tnPsdR500Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200, 6)
)
tnPsdR500Compliance.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdSystemGroup"),
        ("TROPIC-PSD-MIB", "tnPsdShelfGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSlotGroup"),
        ("TROPIC-PSD-MIB", "tnPsdCardGroup"),
        ("TROPIC-PSD-MIB", "tnPsdEquipmentEventGroup"),
        ("TROPIC-PSD-MIB", "tnPsdEquipmentChangeGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSfpGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSfp2Group"),
        ("TROPIC-PSD-MIB", "tnPsdDdmDataGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceStateChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdInterfaceEventNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdLagGroup"),
        ("TROPIC-PSD-MIB", "tnPsdAlsGroup"),
        ("TROPIC-PSD-MIB", "tnPsdAlsNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDest2Group"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSnmpCreDelNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdDatabaseGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSoftwareGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSoftwareEventGroup"),
        ("TROPIC-PSD-MIB", "tnPsdTimeGroup"),
        ("TROPIC-PSD-MIB", "tnPsdTimeConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIp2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIp3Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif3Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdIpStateChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdFaultGroup"),
        ("TROPIC-PSD-MIB", "tnPsdFaultChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdSysDiscoveryGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtnGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtn2Group"),
        ("TROPIC-PSD-MIB", "tnPsdOtn3Group"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif2Group"),
        ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif3Group"),
        ("TROPIC-PSD-MIB", "tnPsdCfmGroup"),
        ("TROPIC-PSD-MIB", "tnPsdCfmConfigChangeNotifGroup"),
        ("TROPIC-PSD-MIB", "tnPsdPmGroup"),
        ("TROPIC-PSD-MIB", "tnPsdPmEthStatsGroup"),
        ("TROPIC-PSD-MIB", "tnPsdPmEthStatsConfigChangeNotifGroup"))
)
if mibBuilder.loadTexts:
    tnPsdR500Compliance.setStatus(
        "current"
    )

tnPsd2R500Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200, 7)
)
tnPsd2R500Compliance.setObjects(
      *(("TROPIC-PSD-MIB", "tnPsdPowerInputGroup"),
        ("TROPIC-PSD-MIB", "tnPsdPowerInputNotifGroup"))
)
if mibBuilder.loadTexts:
    tnPsd2R500Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-PSD-MIB",
    **{"TropicPsdAsapIndexType": TropicPsdAsapIndexType,
       "TropicPsdAvailabilityStatus": TropicPsdAvailabilityStatus,
       "TropicPsdCardCLEICode": TropicPsdCardCLEICode,
       "TropicPsdCardCompanyIdentifier": TropicPsdCardCompanyIdentifier,
       "TropicPsdCardCustomerInvField": TropicPsdCardCustomerInvField,
       "TropicPsdCardDate": TropicPsdCardDate,
       "TropicPsdCardFactoryIdentifier": TropicPsdCardFactoryIdentifier,
       "TropicPsdCardMnemonic": TropicPsdCardMnemonic,
       "TropicPsdCardPartNumber": TropicPsdCardPartNumber,
       "TropicPsdCardSerialNumber": TropicPsdCardSerialNumber,
       "TropicPsdDdmDataType": TropicPsdDdmDataType,
       "TropicPsdDapi": TropicPsdDapi,
       "TropicPsdFaultAlarmTime": TropicPsdFaultAlarmTime,
       "TropicPsdFaultLocationType": TropicPsdFaultLocationType,
       "TropicPsdFaultSeverity": TropicPsdFaultSeverity,
       "TropicPsdIsdId": TropicPsdIsdId,
       "TropicPsdIsdStatus": TropicPsdIsdStatus,
       "TropicPsdNetIfIndexOrZero": TropicPsdNetIfIndexOrZero,
       "TropicPsdNtpServerIndexType": TropicPsdNtpServerIndexType,
       "TropicPsdPriorityValue": TropicPsdPriorityValue,
       "TropicPsdRestartType": TropicPsdRestartType,
       "TropicPsdSapi": TropicPsdSapi,
       "TropicPsdSfpAluPartNumber": TropicPsdSfpAluPartNumber,
       "TropicPsdSfpAluSerialNumber": TropicPsdSfpAluSerialNumber,
       "TropicPsdSfpBitRate": TropicPsdSfpBitRate,
       "TropicPsdSfpCLEICode": TropicPsdSfpCLEICode,
       "TropicPsdSfpConnectorType": TropicPsdSfpConnectorType,
       "TropicPsdSfpIcs": TropicPsdSfpIcs,
       "TropicPsdSfpIdentifier": TropicPsdSfpIdentifier,
       "TropicPsdSfpLinkLength": TropicPsdSfpLinkLength,
       "TropicPsdSfpNokiaPartNumber": TropicPsdSfpNokiaPartNumber,
       "TropicPsdSfpPartNumber": TropicPsdSfpPartNumber,
       "TropicPsdSfpRevisionNumber": TropicPsdSfpRevisionNumber,
       "TropicPsdSfpTransceiverCode": TropicPsdSfpTransceiverCode,
       "TropicPsdSfpVendorDate": TropicPsdSfpVendorDate,
       "TropicPsdSfpVendorName": TropicPsdSfpVendorName,
       "TropicPsdSfpVendorOUI": TropicPsdSfpVendorOUI,
       "TropicPsdSfpVendorSerialNumber": TropicPsdSfpVendorSerialNumber,
       "TropicPsdSfpVendorSpecific": TropicPsdSfpVendorSpecific,
       "TropicPsdSfpWavelength": TropicPsdSfpWavelength,
       "TropicPsdShelfRealTimePower": TropicPsdShelfRealTimePower,
       "TropicPsdSnmpPortNumberType": TropicPsdSnmpPortNumberType,
       "TropicPsdSystemMode": TropicPsdSystemMode,
       "TropicPsdTransportIdentifier": TropicPsdTransportIdentifier,
       "TropicPsdVlanId": TropicPsdVlanId,
       "tnPsdMibModule": tnPsdMibModule,
       "tnPsdSystem": tnPsdSystem,
       "tnPsdSystemObjects": tnPsdSystemObjects,
       "tnPsdSystemMode": tnPsdSystemMode,
       "tnPsdSystemModeDescr": tnPsdSystemModeDescr,
       "tnPsdSystemAbnormalState": tnPsdSystemAbnormalState,
       "tnPsdSystemSmartConnectLed": tnPsdSystemSmartConnectLed,
       "tnPsdSystemConformance": tnPsdSystemConformance,
       "tnPsdSystemGroups": tnPsdSystemGroups,
       "tnPsdSystemGroup": tnPsdSystemGroup,
       "tnPsdEquipment": tnPsdEquipment,
       "tnPsdEquipmentNotifs": tnPsdEquipmentNotifs,
       "tnPsdDyingGaspNotif": tnPsdDyingGaspNotif,
       "tnPsdShelfConfigChangeNotif": tnPsdShelfConfigChangeNotif,
       "tnPsdShelfRestartConfigChangeNotif": tnPsdShelfRestartConfigChangeNotif,
       "tnPsdSwRestartNotif": tnPsdSwRestartNotif,
       "tnPsdEquipmentObjects": tnPsdEquipmentObjects,
       "tnPsdShelfTable": tnPsdShelfTable,
       "tnPsdShelfEntry": tnPsdShelfEntry,
       "tnPsdShelfName": tnPsdShelfName,
       "tnPsdShelfDescr": tnPsdShelfDescr,
       "tnPsdShelfType": tnPsdShelfType,
       "tnPsdShelfLocation": tnPsdShelfLocation,
       "tnPsdShelfLatitude": tnPsdShelfLatitude,
       "tnPsdShelfLongitude": tnPsdShelfLongitude,
       "tnPsdShelfAltitude": tnPsdShelfAltitude,
       "tnPsdShelfRealTimePower": tnPsdShelfRealTimePower,
       "tnPsdSlotTable": tnPsdSlotTable,
       "tnPsdSlotEntry": tnPsdSlotEntry,
       "tnPsdSlotType": tnPsdSlotType,
       "tnPsdCardTable": tnPsdCardTable,
       "tnPsdCardEntry": tnPsdCardEntry,
       "tnPsdCardInvStatus": tnPsdCardInvStatus,
       "tnPsdCardCompanyID": tnPsdCardCompanyID,
       "tnPsdCardMnemonic": tnPsdCardMnemonic,
       "tnPsdCardCLEI": tnPsdCardCLEI,
       "tnPsdCardUnitPartNumber": tnPsdCardUnitPartNumber,
       "tnPsdCardSwPartNumber": tnPsdCardSwPartNumber,
       "tnPsdCardFactoryID": tnPsdCardFactoryID,
       "tnPsdCardSerialNumber": tnPsdCardSerialNumber,
       "tnPsdCardDate": tnPsdCardDate,
       "tnPsdCardCustInvField": tnPsdCardCustInvField,
       "tnPsdShelfRestartTable": tnPsdShelfRestartTable,
       "tnPsdShelfRestartEntry": tnPsdShelfRestartEntry,
       "tnPsdShelfRestart": tnPsdShelfRestart,
       "tnPsdEquipmentConformance": tnPsdEquipmentConformance,
       "tnPsdEquipmentGroups": tnPsdEquipmentGroups,
       "tnPsdShelfGroup": tnPsdShelfGroup,
       "tnPsdSlotGroup": tnPsdSlotGroup,
       "tnPsdCardGroup": tnPsdCardGroup,
       "tnPsdEquipmentEventGroup": tnPsdEquipmentEventGroup,
       "tnPsdEquipmentChangeGroup": tnPsdEquipmentChangeGroup,
       "tnPsdInterface": tnPsdInterface,
       "tnPsdInterfaceNotifs": tnPsdInterfaceNotifs,
       "tnPsdSfpConfigChangeNotif": tnPsdSfpConfigChangeNotif,
       "tnPsdSfpInfoTuningStatusChangeNotif": tnPsdSfpInfoTuningStatusChangeNotif,
       "tnPsdSfpInfoTuningOkNotif": tnPsdSfpInfoTuningOkNotif,
       "tnPsdAlsConfigChangeNotif": tnPsdAlsConfigChangeNotif,
       "tnPsdAlsChangeNotif": tnPsdAlsChangeNotif,
       "tnPsdInterfaceObjects": tnPsdInterfaceObjects,
       "tnPsdSfpConfigTable": tnPsdSfpConfigTable,
       "tnPsdSfpConfigEntry": tnPsdSfpConfigEntry,
       "tnPsdSfpType": tnPsdSfpType,
       "tnPsdSfpProgrammedChannel": tnPsdSfpProgrammedChannel,
       "tnPsdSfpInfoTable": tnPsdSfpInfoTable,
       "tnPsdSfpInfoEntry": tnPsdSfpInfoEntry,
       "tnPsdSfpInfoInvStatus": tnPsdSfpInfoInvStatus,
       "tnPsdSfpInfoPhysicalIdentifier": tnPsdSfpInfoPhysicalIdentifier,
       "tnPsdSfpInfoClassOfWdm": tnPsdSfpInfoClassOfWdm,
       "tnPsdSfpInfoConnectorType": tnPsdSfpInfoConnectorType,
       "tnPsdSfpInfoTransceiverCode": tnPsdSfpInfoTransceiverCode,
       "tnPsdSfpInfoBitRateNominal": tnPsdSfpInfoBitRateNominal,
       "tnPsdSfpInfoLinkType": tnPsdSfpInfoLinkType,
       "tnPsdSfpInfoLinkMaxLength": tnPsdSfpInfoLinkMaxLength,
       "tnPsdSfpInfoLinkLengthOverrun": tnPsdSfpInfoLinkLengthOverrun,
       "tnPsdSfpInfoLinkLengthUnits": tnPsdSfpInfoLinkLengthUnits,
       "tnPsdSfpInfoLinkLength": tnPsdSfpInfoLinkLength,
       "tnPsdSfpInfoVendorName": tnPsdSfpInfoVendorName,
       "tnPsdSfpInfoVendorOUI": tnPsdSfpInfoVendorOUI,
       "tnPsdSfpInfoPartNumber": tnPsdSfpInfoPartNumber,
       "tnPsdSfpInfoRevisionNumber": tnPsdSfpInfoRevisionNumber,
       "tnPsdSfpInfoWavelength": tnPsdSfpInfoWavelength,
       "tnPsdSfpInfoBitRateMaximum": tnPsdSfpInfoBitRateMaximum,
       "tnPsdSfpInfoBitRateMinimum": tnPsdSfpInfoBitRateMinimum,
       "tnPsdSfpInfoVendorSerialNumber": tnPsdSfpInfoVendorSerialNumber,
       "tnPsdSfpInfoVendorDate": tnPsdSfpInfoVendorDate,
       "tnPsdSfpInfoVendorSpecific": tnPsdSfpInfoVendorSpecific,
       "tnPsdSfpInfoCLEI": tnPsdSfpInfoCLEI,
       "tnPsdSfpInfoAluPartNumber": tnPsdSfpInfoAluPartNumber,
       "tnPsdSfpInfoAluSerialNumber": tnPsdSfpInfoAluSerialNumber,
       "tnPsdSfpInfoIcs": tnPsdSfpInfoIcs,
       "tnPsdSfpInfoNokiaPartNumber": tnPsdSfpInfoNokiaPartNumber,
       "tnPsdSfpInfoTunable": tnPsdSfpInfoTunable,
       "tnPsdSfpInfoFrequency": tnPsdSfpInfoFrequency,
       "tnPsdSfpInfoFrequencyLow": tnPsdSfpInfoFrequencyLow,
       "tnPsdSfpInfoFrequencyHigh": tnPsdSfpInfoFrequencyHigh,
       "tnPsdSfpInfoFrequencyGrid": tnPsdSfpInfoFrequencyGrid,
       "tnPsdSfpInfoTuningStatus": tnPsdSfpInfoTuningStatus,
       "tnPsdDdmDataTable": tnPsdDdmDataTable,
       "tnPsdDdmDataEntry": tnPsdDdmDataEntry,
       "tnPsdDdmDataType": tnPsdDdmDataType,
       "tnPsdDdmDataValue": tnPsdDdmDataValue,
       "tnPsdLagCommandTable": tnPsdLagCommandTable,
       "tnPsdLagCommandEntry": tnPsdLagCommandEntry,
       "tnPsdLagCommandSubgroupSelected": tnPsdLagCommandSubgroupSelected,
       "tnPsdAlsTable": tnPsdAlsTable,
       "tnPsdAlsEntry": tnPsdAlsEntry,
       "tnPsdAlsEnabled": tnPsdAlsEnabled,
       "tnPsdAlsWaitToRestart": tnPsdAlsWaitToRestart,
       "tnPsdAlsTxTime": tnPsdAlsTxTime,
       "tnPsdAlsState": tnPsdAlsState,
       "tnPsdAlsActiveCheck": tnPsdAlsActiveCheck,
       "tnPsdAlsActiveCheckForTest": tnPsdAlsActiveCheckForTest,
       "tnPsdInterfaceConformance": tnPsdInterfaceConformance,
       "tnPsdInterfaceGroups": tnPsdInterfaceGroups,
       "tnPsdSfpGroup": tnPsdSfpGroup,
       "tnPsdDdmDataGroup": tnPsdDdmDataGroup,
       "tnPsdInterfaceConfigChangeNotifGroup": tnPsdInterfaceConfigChangeNotifGroup,
       "tnPsdLagGroup": tnPsdLagGroup,
       "tnPsdSfp2Group": tnPsdSfp2Group,
       "tnPsdInterfaceStateChangeNotifGroup": tnPsdInterfaceStateChangeNotifGroup,
       "tnPsdInterfaceEventNotifGroup": tnPsdInterfaceEventNotifGroup,
       "tnPsdAlsGroup": tnPsdAlsGroup,
       "tnPsdAlsNotifGroup": tnPsdAlsNotifGroup,
       "tnPsdSnmp": tnPsdSnmp,
       "tnPsdSnmpNotifs": tnPsdSnmpNotifs,
       "tnPsdSnmpTrapDestConfigChangeNotif": tnPsdSnmpTrapDestConfigChangeNotif,
       "tnPsdSnmpTrapDestCreationNotif": tnPsdSnmpTrapDestCreationNotif,
       "tnPsdSnmpTrapDestDeletionNotif": tnPsdSnmpTrapDestDeletionNotif,
       "tnPsdSnmpObjects": tnPsdSnmpObjects,
       "tnPsdSnmpTrapDestTable": tnPsdSnmpTrapDestTable,
       "tnPsdSnmpTrapDestEntry": tnPsdSnmpTrapDestEntry,
       "tnPsdSnmpTrapDestServerId": tnPsdSnmpTrapDestServerId,
       "tnPsdSnmpTrapDestAddrType": tnPsdSnmpTrapDestAddrType,
       "tnPsdSnmpTrapDestAddr": tnPsdSnmpTrapDestAddr,
       "tnPsdSnmpTrapDestPort": tnPsdSnmpTrapDestPort,
       "tnPsdSnmpTrapDestCommunity": tnPsdSnmpTrapDestCommunity,
       "tnPsdSnmpTrapDestDyingGasp": tnPsdSnmpTrapDestDyingGasp,
       "tnPsdSnmpTrapDestRowStatus": tnPsdSnmpTrapDestRowStatus,
       "tnPsdSnmpTrapDestSnmpVersion": tnPsdSnmpTrapDestSnmpVersion,
       "tnPsdSnmpTrapDestUserName": tnPsdSnmpTrapDestUserName,
       "tnPsdSnmpConformance": tnPsdSnmpConformance,
       "tnPsdSnmpGroups": tnPsdSnmpGroups,
       "tnPsdSnmpTrapDestGroup": tnPsdSnmpTrapDestGroup,
       "tnPsdSnmpConfigChangeNotifGroup": tnPsdSnmpConfigChangeNotifGroup,
       "tnPsdSnmpCreDelNotifGroup": tnPsdSnmpCreDelNotifGroup,
       "tnPsdSnmpTrapDest2Group": tnPsdSnmpTrapDest2Group,
       "tnPsdDatabase": tnPsdDatabase,
       "tnPsdDatabaseObjects": tnPsdDatabaseObjects,
       "tnPsdDatabaseBackupAndRestoreRemoteHostAddrType": tnPsdDatabaseBackupAndRestoreRemoteHostAddrType,
       "tnPsdDatabaseBackupAndRestoreRemoteHostAddr": tnPsdDatabaseBackupAndRestoreRemoteHostAddr,
       "tnPsdDatabaseConformance": tnPsdDatabaseConformance,
       "tnPsdDatabaseGroups": tnPsdDatabaseGroups,
       "tnPsdDatabaseGroup": tnPsdDatabaseGroup,
       "tnPsdSoftware": tnPsdSoftware,
       "tnPsdSoftwareNotifs": tnPsdSoftwareNotifs,
       "tnPsdSwActivateNotif": tnPsdSwActivateNotif,
       "tnPsdSwCommitNotif": tnPsdSwCommitNotif,
       "tnPsdSoftwareObjects": tnPsdSoftwareObjects,
       "tnPsdSoftwareRemoteHostAddrType": tnPsdSoftwareRemoteHostAddrType,
       "tnPsdSoftwareRemoteHostAddr": tnPsdSoftwareRemoteHostAddr,
       "tnPsdShelfIsdTable": tnPsdShelfIsdTable,
       "tnPsdShelfIsdEntry": tnPsdShelfIsdEntry,
       "tnPsdShelfIsdId": tnPsdShelfIsdId,
       "tnPsdShelfIsdStatus": tnPsdShelfIsdStatus,
       "tnPsdShelfIsdBuildTime": tnPsdShelfIsdBuildTime,
       "tnPsdShelfIsdItemCode": tnPsdShelfIsdItemCode,
       "tnPsdShelfIsdMaintenance": tnPsdShelfIsdMaintenance,
       "tnPsdShelfIsdCompatible": tnPsdShelfIsdCompatible,
       "tnPsdShelfIsdSwRelease": tnPsdShelfIsdSwRelease,
       "tnPsdSoftwareConformance": tnPsdSoftwareConformance,
       "tnPsdSoftwareGroups": tnPsdSoftwareGroups,
       "tnPsdSoftwareGroup": tnPsdSoftwareGroup,
       "tnPsdSoftwareEventGroup": tnPsdSoftwareEventGroup,
       "tnPsdTime": tnPsdTime,
       "tnPsdTimeNotifs": tnPsdTimeNotifs,
       "tnPsdShelfTimeConfigChangeNotif": tnPsdShelfTimeConfigChangeNotif,
       "tnPsdNtpConfigChangeNotif": tnPsdNtpConfigChangeNotif,
       "tnPsdNtpServerConfigChangeNotif": tnPsdNtpServerConfigChangeNotif,
       "tnPsdTimeObjects": tnPsdTimeObjects,
       "tnPsdShelfTimeTable": tnPsdShelfTimeTable,
       "tnPsdShelfTimeEntry": tnPsdShelfTimeEntry,
       "tnPsdShelfTime": tnPsdShelfTime,
       "tnPsdNtpTable": tnPsdNtpTable,
       "tnPsdNtpEntry": tnPsdNtpEntry,
       "tnPsdNtpState": tnPsdNtpState,
       "tnPsdNtpStatus": tnPsdNtpStatus,
       "tnPsdNtpStratum": tnPsdNtpStratum,
       "tnPsdNtpAccuracy": tnPsdNtpAccuracy,
       "tnPsdNtpServerTable": tnPsdNtpServerTable,
       "tnPsdNtpServerEntry": tnPsdNtpServerEntry,
       "tnPsdNtpServerIndex": tnPsdNtpServerIndex,
       "tnPsdNtpServerAddrType": tnPsdNtpServerAddrType,
       "tnPsdNtpServerAddr": tnPsdNtpServerAddr,
       "tnPsdNtpServerSystemServer": tnPsdNtpServerSystemServer,
       "tnPsdNtpServerReachable": tnPsdNtpServerReachable,
       "tnPsdNtpServerReachabilityData": tnPsdNtpServerReachabilityData,
       "tnPsdNtpServerPollTime": tnPsdNtpServerPollTime,
       "tnPsdTimeConformance": tnPsdTimeConformance,
       "tnPsdTimeGroups": tnPsdTimeGroups,
       "tnPsdTimeGroup": tnPsdTimeGroup,
       "tnPsdTimeConfigChangeNotifGroup": tnPsdTimeConfigChangeNotifGroup,
       "tnPsdIp": tnPsdIp,
       "tnPsdIpNotifs": tnPsdIpNotifs,
       "tnPsdManualIpv4AddressConfigChangeNotif": tnPsdManualIpv4AddressConfigChangeNotif,
       "tnPsdManualIpv6AddressConfigChangeNotif": tnPsdManualIpv6AddressConfigChangeNotif,
       "tnPsdDhcpClientConfigChangeNotif": tnPsdDhcpClientConfigChangeNotif,
       "tnPsdStaticRouteConfigChangeNotif": tnPsdStaticRouteConfigChangeNotif,
       "tnPsdStaticRouteCreationNotif": tnPsdStaticRouteCreationNotif,
       "tnPsdStaticRouteDeletionNotif": tnPsdStaticRouteDeletionNotif,
       "tnPsdNetIfOperStatusChangeNotif": tnPsdNetIfOperStatusChangeNotif,
       "tnPsdNetIfConfigChangeNotif": tnPsdNetIfConfigChangeNotif,
       "tnPsdNetIfEthFacilityConfigChangeNotif": tnPsdNetIfEthFacilityConfigChangeNotif,
       "tnPsdNetIfEthFacilityCreationNotif": tnPsdNetIfEthFacilityCreationNotif,
       "tnPsdNetIfEthFacilityDeletionNotif": tnPsdNetIfEthFacilityDeletionNotif,
       "tnPsdProxyArpConfigChangeNotif": tnPsdProxyArpConfigChangeNotif,
       "tnPsdIpObjects": tnPsdIpObjects,
       "tnPsdEnforceSrcIpV4ToLoopbackIpV4": tnPsdEnforceSrcIpV4ToLoopbackIpV4,
       "tnPsdEnforceSrcIpV6ToLoopbackIpV6": tnPsdEnforceSrcIpV6ToLoopbackIpV6,
       "tnPsdManualIpv4AddressTable": tnPsdManualIpv4AddressTable,
       "tnPsdManualIpv4AddressEntry": tnPsdManualIpv4AddressEntry,
       "tnPsdManualIpv4AddressAddrType": tnPsdManualIpv4AddressAddrType,
       "tnPsdManualIpv4AddressAddr": tnPsdManualIpv4AddressAddr,
       "tnPsdManualIpv4AddressPrefixLen": tnPsdManualIpv4AddressPrefixLen,
       "tnPsdManualIpv6AddressTable": tnPsdManualIpv6AddressTable,
       "tnPsdManualIpv6AddressEntry": tnPsdManualIpv6AddressEntry,
       "tnPsdManualIpv6AddressAddrType": tnPsdManualIpv6AddressAddrType,
       "tnPsdManualIpv6AddressAddr": tnPsdManualIpv6AddressAddr,
       "tnPsdManualIpv6AddressPrefixLen": tnPsdManualIpv6AddressPrefixLen,
       "tnPsdActualIpAddressTable": tnPsdActualIpAddressTable,
       "tnPsdActualIpAddressEntry": tnPsdActualIpAddressEntry,
       "tnPsdActualIpAddressAddrType": tnPsdActualIpAddressAddrType,
       "tnPsdActualIpAddressAddr": tnPsdActualIpAddressAddr,
       "tnPsdActualIpAddressPrefixLen": tnPsdActualIpAddressPrefixLen,
       "tnPsdDhcpClientTable": tnPsdDhcpClientTable,
       "tnPsdDhcpClientEntry": tnPsdDhcpClientEntry,
       "tnPsdDhcpClientV4Enabled": tnPsdDhcpClientV4Enabled,
       "tnPsdStaticRouteTable": tnPsdStaticRouteTable,
       "tnPsdStaticRouteEntry": tnPsdStaticRouteEntry,
       "tnPsdStaticRouteDestType": tnPsdStaticRouteDestType,
       "tnPsdStaticRouteDest": tnPsdStaticRouteDest,
       "tnPsdStaticRoutePrefixLen": tnPsdStaticRoutePrefixLen,
       "tnPsdStaticRouteGatewayType": tnPsdStaticRouteGatewayType,
       "tnPsdStaticRouteGateway": tnPsdStaticRouteGateway,
       "tnPsdStaticRouteIfIndex": tnPsdStaticRouteIfIndex,
       "tnPsdStaticRouteNetIfIndex": tnPsdStaticRouteNetIfIndex,
       "tnPsdStaticRouteMetric": tnPsdStaticRouteMetric,
       "tnPsdStaticRouteRowStatus": tnPsdStaticRouteRowStatus,
       "tnPsdActualRouteTable": tnPsdActualRouteTable,
       "tnPsdActualRouteEntry": tnPsdActualRouteEntry,
       "tnPsdActualRouteDestType": tnPsdActualRouteDestType,
       "tnPsdActualRouteDest": tnPsdActualRouteDest,
       "tnPsdActualRoutePrefixLen": tnPsdActualRoutePrefixLen,
       "tnPsdActualRouteGatewayType": tnPsdActualRouteGatewayType,
       "tnPsdActualRouteGateway": tnPsdActualRouteGateway,
       "tnPsdActualRouteIfIndex": tnPsdActualRouteIfIndex,
       "tnPsdActualRouteNetIfIndex": tnPsdActualRouteNetIfIndex,
       "tnPsdActualRouteMetric": tnPsdActualRouteMetric,
       "tnPsdNetIfTable": tnPsdNetIfTable,
       "tnPsdNetIfEntry": tnPsdNetIfEntry,
       "tnPsdNetIfIpAddrType": tnPsdNetIfIpAddrType,
       "tnPsdNetIfIpAddr": tnPsdNetIfIpAddr,
       "tnPsdNetIfIpPrefixLen": tnPsdNetIfIpPrefixLen,
       "tnPsdNetIfOperStatus": tnPsdNetIfOperStatus,
       "tnPsdNetIfRemoteIpAddrType": tnPsdNetIfRemoteIpAddrType,
       "tnPsdNetIfRemoteIpAddr": tnPsdNetIfRemoteIpAddr,
       "tnPsdNetIfMonitoring": tnPsdNetIfMonitoring,
       "tnPsdNetIfIp6AddrType": tnPsdNetIfIp6AddrType,
       "tnPsdNetIfIp6Addr": tnPsdNetIfIp6Addr,
       "tnPsdNetIfIp6PrefixLen": tnPsdNetIfIp6PrefixLen,
       "tnPsdNetIfRemoteIp6AddrType": tnPsdNetIfRemoteIp6AddrType,
       "tnPsdNetIfRemoteIp6Addr": tnPsdNetIfRemoteIp6Addr,
       "tnPsdNetIfMonitoring6": tnPsdNetIfMonitoring6,
       "tnPsdNetIfEthFacilityTable": tnPsdNetIfEthFacilityTable,
       "tnPsdNetIfEthFacilityEntry": tnPsdNetIfEthFacilityEntry,
       "tnPsdNetIfEthFacilityTpid": tnPsdNetIfEthFacilityTpid,
       "tnPsdNetIfEthFacilityVlanId": tnPsdNetIfEthFacilityVlanId,
       "tnPsdNetIfEthFacilityTypeOfOperation": tnPsdNetIfEthFacilityTypeOfOperation,
       "tnPsdNetIfEthFacilityPriorityEgress": tnPsdNetIfEthFacilityPriorityEgress,
       "tnPsdNetIfEthFacilityDropEligibleEgress": tnPsdNetIfEthFacilityDropEligibleEgress,
       "tnPsdProxyArpTable": tnPsdProxyArpTable,
       "tnPsdProxyArpEntry": tnPsdProxyArpEntry,
       "tnPsdProxyArp": tnPsdProxyArp,
       "tnPsdIpConformance": tnPsdIpConformance,
       "tnPsdIpGroups": tnPsdIpGroups,
       "tnPsdIpGroup": tnPsdIpGroup,
       "tnPsdIpConfigChangeNotifGroup": tnPsdIpConfigChangeNotifGroup,
       "tnPsdIpCreDelNotifGroup": tnPsdIpCreDelNotifGroup,
       "tnPsdIpStateChangeNotifGroup": tnPsdIpStateChangeNotifGroup,
       "tnPsdIp2Group": tnPsdIp2Group,
       "tnPsdIpConfigChangeNotif2Group": tnPsdIpConfigChangeNotif2Group,
       "tnPsdIpCreDelNotif2Group": tnPsdIpCreDelNotif2Group,
       "tnPsdIp3Group": tnPsdIp3Group,
       "tnPsdIpConfigChangeNotif3Group": tnPsdIpConfigChangeNotif3Group,
       "tnPsdFault": tnPsdFault,
       "tnPsdFaultNotifs": tnPsdFaultNotifs,
       "tnPsdAsapConfigChangeNotif": tnPsdAsapConfigChangeNotif,
       "tnPsdAsapFaultProfileConfigChangeNotif": tnPsdAsapFaultProfileConfigChangeNotif,
       "tnPsdFaultConfigChangeNotif": tnPsdFaultConfigChangeNotif,
       "tnPsdFaultObjects": tnPsdFaultObjects,
       "tnPsdAsapTable": tnPsdAsapTable,
       "tnPsdAsapEntry": tnPsdAsapEntry,
       "tnPsdAsapIndex": tnPsdAsapIndex,
       "tnPsdAsapName": tnPsdAsapName,
       "tnPsdAsapFaultProfileTable": tnPsdAsapFaultProfileTable,
       "tnPsdAsapFaultProfileEntry": tnPsdAsapFaultProfileEntry,
       "tnPsdAsapFaultProfileCondition": tnPsdAsapFaultProfileCondition,
       "tnPsdAsapFaultProfileLocationType": tnPsdAsapFaultProfileLocationType,
       "tnPsdAsapFaultProfileSeverity": tnPsdAsapFaultProfileSeverity,
       "tnPsdAsapFaultProfileReported": tnPsdAsapFaultProfileReported,
       "tnPsdAsapFaultProfileServiceAffecting": tnPsdAsapFaultProfileServiceAffecting,
       "tnPsdAsapFaultProfileAlarmText": tnPsdAsapFaultProfileAlarmText,
       "tnPsdFaultTable": tnPsdFaultTable,
       "tnPsdFaultEntry": tnPsdFaultEntry,
       "tnPsdFaultAlarmRaiseTime": tnPsdFaultAlarmRaiseTime,
       "tnPsdFaultAlarmClearTime": tnPsdFaultAlarmClearTime,
       "tnPsdFaultConformance": tnPsdFaultConformance,
       "tnPsdFaultGroups": tnPsdFaultGroups,
       "tnPsdFaultGroup": tnPsdFaultGroup,
       "tnPsdFaultChangeNotifGroup": tnPsdFaultChangeNotifGroup,
       "tnPsdSysDiscovery": tnPsdSysDiscovery,
       "tnPsdSysDiscoveryObjects": tnPsdSysDiscoveryObjects,
       "tnPsdSysDiscoveryServerAddrType": tnPsdSysDiscoveryServerAddrType,
       "tnPsdSysDiscoveryServerAddr": tnPsdSysDiscoveryServerAddr,
       "tnPsdSysDiscoveryConformance": tnPsdSysDiscoveryConformance,
       "tnPsdSysDiscoveryGroups": tnPsdSysDiscoveryGroups,
       "tnPsdSysDiscoveryGroup": tnPsdSysDiscoveryGroup,
       "tnPsdOtn": tnPsdOtn,
       "tnPsdOtnNotifs": tnPsdOtnNotifs,
       "tnPsdOtukConfigChangeNotif": tnPsdOtukConfigChangeNotif,
       "tnPsdOdukNimConfigChangeNotif": tnPsdOdukNimConfigChangeNotif,
       "tnPsdOdukTtpConfigChangeNotif": tnPsdOdukTtpConfigChangeNotif,
       "tnPsdOdukTConfigChangeNotif": tnPsdOdukTConfigChangeNotif,
       "tnPsdOdukTtpDmConfigChangeNotif": tnPsdOdukTtpDmConfigChangeNotif,
       "tnPsdOdukTtpPrbsConfigChangeNotif": tnPsdOdukTtpPrbsConfigChangeNotif,
       "tnPsdOtnObjects": tnPsdOtnObjects,
       "tnPsdOtukTable": tnPsdOtukTable,
       "tnPsdOtukEntry": tnPsdOtukEntry,
       "tnPsdOtukSapiAccepted": tnPsdOtukSapiAccepted,
       "tnPsdOtukSapiExpected": tnPsdOtukSapiExpected,
       "tnPsdOtukSapiTransmitted": tnPsdOtukSapiTransmitted,
       "tnPsdOtukDapiAccepted": tnPsdOtukDapiAccepted,
       "tnPsdOtukDapiExpected": tnPsdOtukDapiExpected,
       "tnPsdOtukDapiTransmitted": tnPsdOtukDapiTransmitted,
       "tnPsdOdukNimTable": tnPsdOdukNimTable,
       "tnPsdOdukNimEntry": tnPsdOdukNimEntry,
       "tnPsdOdukNimSapiAccepted": tnPsdOdukNimSapiAccepted,
       "tnPsdOdukNimSapiExpected": tnPsdOdukNimSapiExpected,
       "tnPsdOdukNimDapiAccepted": tnPsdOdukNimDapiAccepted,
       "tnPsdOdukNimDapiExpected": tnPsdOdukNimDapiExpected,
       "tnPsdOdukTtpTable": tnPsdOdukTtpTable,
       "tnPsdOdukTtpEntry": tnPsdOdukTtpEntry,
       "tnPsdOdukTtpSapiAccepted": tnPsdOdukTtpSapiAccepted,
       "tnPsdOdukTtpSapiExpected": tnPsdOdukTtpSapiExpected,
       "tnPsdOdukTtpSapiTransmitted": tnPsdOdukTtpSapiTransmitted,
       "tnPsdOdukTtpDapiAccepted": tnPsdOdukTtpDapiAccepted,
       "tnPsdOdukTtpDapiExpected": tnPsdOdukTtpDapiExpected,
       "tnPsdOdukTtpDapiTransmitted": tnPsdOdukTtpDapiTransmitted,
       "tnPsdOdukTTable": tnPsdOdukTTable,
       "tnPsdOdukTEntry": tnPsdOdukTEntry,
       "tnPsdOdukTSapiAccepted": tnPsdOdukTSapiAccepted,
       "tnPsdOdukTSapiExpected": tnPsdOdukTSapiExpected,
       "tnPsdOdukTSapiTransmitted": tnPsdOdukTSapiTransmitted,
       "tnPsdOdukTDapiAccepted": tnPsdOdukTDapiAccepted,
       "tnPsdOdukTDapiExpected": tnPsdOdukTDapiExpected,
       "tnPsdOdukTDapiTransmitted": tnPsdOdukTDapiTransmitted,
       "tnPsdOdukTtpDmTable": tnPsdOdukTtpDmTable,
       "tnPsdOdukTtpDmEntry": tnPsdOdukTtpDmEntry,
       "tnPsdOdukTtpDmReflection": tnPsdOdukTtpDmReflection,
       "tnPsdOdukTtpDmSessionType": tnPsdOdukTtpDmSessionType,
       "tnPsdOdukTtpDmStart": tnPsdOdukTtpDmStart,
       "tnPsdOdukTtpDmOnDemandResultTable": tnPsdOdukTtpDmOnDemandResultTable,
       "tnPsdOdukTtpDmOnDemandResultEntry": tnPsdOdukTtpDmOnDemandResultEntry,
       "tnPsdOdukTtpDmOnDemandResultStatus": tnPsdOdukTtpDmOnDemandResultStatus,
       "tnPsdOdukTtpDmOnDemandResultRoundTrip": tnPsdOdukTtpDmOnDemandResultRoundTrip,
       "tnPsdOdukTtpPrbsTable": tnPsdOdukTtpPrbsTable,
       "tnPsdOdukTtpPrbsEntry": tnPsdOdukTtpPrbsEntry,
       "tnPsdOdukTtpPrbsGenerator": tnPsdOdukTtpPrbsGenerator,
       "tnPsdOdukTtpPrbsGeneratorInvert": tnPsdOdukTtpPrbsGeneratorInvert,
       "tnPsdOdukTtpPrbsMonitor": tnPsdOdukTtpPrbsMonitor,
       "tnPsdOdukTtpPrbsMonitorInvert": tnPsdOdukTtpPrbsMonitorInvert,
       "tnPsdOdukTtpPrbsErrorPropagation": tnPsdOdukTtpPrbsErrorPropagation,
       "tnPsdOdukTtpPrbsTestResultTable": tnPsdOdukTtpPrbsTestResultTable,
       "tnPsdOdukTtpPrbsTestResultEntry": tnPsdOdukTtpPrbsTestResultEntry,
       "tnPsdOdukTtpPrbsLockTime": tnPsdOdukTtpPrbsLockTime,
       "tnPsdOdukTtpPrbsTSE": tnPsdOdukTtpPrbsTSE,
       "tnPsdOdukTtpPrbsBitErrorRate": tnPsdOdukTtpPrbsBitErrorRate,
       "tnPsdOtnConformance": tnPsdOtnConformance,
       "tnPsdOtnGroups": tnPsdOtnGroups,
       "tnPsdOtnGroup": tnPsdOtnGroup,
       "tnPsdOtnConfigChangeNotifGroup": tnPsdOtnConfigChangeNotifGroup,
       "tnPsdOtn2Group": tnPsdOtn2Group,
       "tnPsdOtnConfigChangeNotif2Group": tnPsdOtnConfigChangeNotif2Group,
       "tnPsdOtn3Group": tnPsdOtn3Group,
       "tnPsdOtnConfigChangeNotif3Group": tnPsdOtnConfigChangeNotif3Group,
       "tnPsdCfm": tnPsdCfm,
       "tnPsdCfmNotifs": tnPsdCfmNotifs,
       "tnPsdDot1agCfmMepDmTWTestConfigChangeNotif": tnPsdDot1agCfmMepDmTWTestConfigChangeNotif,
       "tnPsdDot1agCfmMepSlmTWTestConfigChangeNotif": tnPsdDot1agCfmMepSlmTWTestConfigChangeNotif,
       "tnPsdSoamConfigChangeNotif": tnPsdSoamConfigChangeNotif,
       "tnPsdCfmObjects": tnPsdCfmObjects,
       "tnPsdCfmTransportIdentifier": tnPsdCfmTransportIdentifier,
       "tnPsdOamEthCfmPingCtlTable": tnPsdOamEthCfmPingCtlTable,
       "tnPsdOamEthCfmPingCtlEntry": tnPsdOamEthCfmPingCtlEntry,
       "tnPsdOamEthCfmPingCtlPriority": tnPsdOamEthCfmPingCtlPriority,
       "tnPsdOamEthCfmPingCtlAvailFlrThreshold": tnPsdOamEthCfmPingCtlAvailFlrThreshold,
       "tnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals": tnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals,
       "tnPsdOamEthCfmPingCtlAvailFlrInterval15Min": tnPsdOamEthCfmPingCtlAvailFlrInterval15Min,
       "tnPsdOamEthCfmPingCtlAvailFlrInterval1Day": tnPsdOamEthCfmPingCtlAvailFlrInterval1Day,
       "tnPsdOamEthCfmTestTable": tnPsdOamEthCfmTestTable,
       "tnPsdOamEthCfmTestEntry": tnPsdOamEthCfmTestEntry,
       "tnPsdOamEthCfmTestSwitchId": tnPsdOamEthCfmTestSwitchId,
       "tnPsdOamEthCfmTestSrcMdIndex": tnPsdOamEthCfmTestSrcMdIndex,
       "tnPsdOamEthCfmTestSrcMaIndex": tnPsdOamEthCfmTestSrcMaIndex,
       "tnPsdOamEthCfmTestSrcMepId": tnPsdOamEthCfmTestSrcMepId,
       "tnPsdOamEthCfmTestMode": tnPsdOamEthCfmTestMode,
       "tnPsdOamEthCfmTestPriority": tnPsdOamEthCfmTestPriority,
       "tnPsdOamEthCfmTestInterval": tnPsdOamEthCfmTestInterval,
       "tnPsdOamEthCfmTestSize": tnPsdOamEthCfmTestSize,
       "tnPsdOamEthCfmTestTgtMacAddr": tnPsdOamEthCfmTestTgtMacAddr,
       "tnPsdOamEthCfmTestName": tnPsdOamEthCfmTestName,
       "tnPsdDot1agCfmMepDmTWTestTable": tnPsdDot1agCfmMepDmTWTestTable,
       "tnPsdDot1agCfmMepDmTWTestEntry": tnPsdDot1agCfmMepDmTWTestEntry,
       "tnPsdDot1agCfmMepDmTWTestStatus": tnPsdDot1agCfmMepDmTWTestStatus,
       "tnPsdDot1agCfmMepSlmTWTestTable": tnPsdDot1agCfmMepSlmTWTestTable,
       "tnPsdDot1agCfmMepSlmTWTestEntry": tnPsdDot1agCfmMepSlmTWTestEntry,
       "tnPsdDot1agCfmMepSlmTWInterval": tnPsdDot1agCfmMepSlmTWInterval,
       "tnPsdSoamTable": tnPsdSoamTable,
       "tnPsdSoamEntry": tnPsdSoamEntry,
       "tnPsdSoamEnable": tnPsdSoamEnable,
       "tnPsdCfmConformance": tnPsdCfmConformance,
       "tnPsdCfmGroups": tnPsdCfmGroups,
       "tnPsdCfmGroup": tnPsdCfmGroup,
       "tnPsdCfmConfigChangeNotifGroup": tnPsdCfmConfigChangeNotifGroup,
       "tnPsdPm": tnPsdPm,
       "tnPsdPmNotifs": tnPsdPmNotifs,
       "tnPsdEthStatsPortConfigChangeNotif": tnPsdEthStatsPortConfigChangeNotif,
       "tnPsdPmObjects": tnPsdPmObjects,
       "tnPsdPmTcaReportingMethod": tnPsdPmTcaReportingMethod,
       "tnPsdEthStatsPortConfigTable": tnPsdEthStatsPortConfigTable,
       "tnPsdEthStatsPortConfigEntry": tnPsdEthStatsPortConfigEntry,
       "tnPsdEthStatsPortClear": tnPsdEthStatsPortClear,
       "tnPsdPmConformance": tnPsdPmConformance,
       "tnPsdPmGroups": tnPsdPmGroups,
       "tnPsdPmGroup": tnPsdPmGroup,
       "tnPsdPmEthStatsGroup": tnPsdPmEthStatsGroup,
       "tnPsdPmEthStatsConfigChangeNotifGroup": tnPsdPmEthStatsConfigChangeNotifGroup,
       "tnPsdPowerInput": tnPsdPowerInput,
       "tnPsdPowerInputNotifs": tnPsdPowerInputNotifs,
       "tnPsdPowerInputConfigChangeNotif": tnPsdPowerInputConfigChangeNotif,
       "tnPsdPowerInputObjects": tnPsdPowerInputObjects,
       "tnPsdPowerInputTable": tnPsdPowerInputTable,
       "tnPsdPowerInputEntry": tnPsdPowerInputEntry,
       "tnPsdPowerInputIndex": tnPsdPowerInputIndex,
       "tnPsdPowerInputMonitoring": tnPsdPowerInputMonitoring,
       "tnPsdPowerInputConformance": tnPsdPowerInputConformance,
       "tnPsdPowerInputGroups": tnPsdPowerInputGroups,
       "tnPsdPowerInputGroup": tnPsdPowerInputGroup,
       "tnPsdPowerInputNotifGroup": tnPsdPowerInputNotifGroup,
       "tnPsdAgentCapability": tnPsdAgentCapability,
       "tnPsdMIBCompliance": tnPsdMIBCompliance,
       "tnPsdR100Compliance": tnPsdR100Compliance,
       "tnPsdR110Compliance": tnPsdR110Compliance,
       "tnPsdR200Compliance": tnPsdR200Compliance,
       "tnPsdR300Compliance": tnPsdR300Compliance,
       "tnPsdR400Compliance": tnPsdR400Compliance,
       "tnPsdR500Compliance": tnPsdR500Compliance,
       "tnPsd2R500Compliance": tnPsd2R500Compliance}
)
