# SNMP MIB module (MDS-IF-LN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gemds\MDS-IF-LN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:27 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(mdsInterfaces,) = mibBuilder.importSymbols(
    "MDS-ORBIT-SMI-MIB",
    "mdsInterfaces")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mdsIfLnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5)
)
if mibBuilder.loadTexts:
    mdsIfLnMIB.setRevisions(
        ("2018-05-16 00:00",
         "2017-11-15 00:00",
         "2016-09-21 00:00",
         "2015-09-14 00:00",
         "2015-09-09 00:00",
         "2015-08-21 00:00",
         "2015-08-03 00:00",
         "2015-06-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class LinkStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("initializing", 0),
          ("scanning", 1),
          ("negotiating", 2),
          ("authenticating", 3),
          ("associated", 4),
          ("disassociated", 5))
    )



class InitStatus(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("initializing", 1),
          ("discovering", 2),
          ("reprogramming", 3),
          ("configuring", 4),
          ("complete", 5),
          ("error", 6))
    )



class DeviceModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("remote", 0),
          ("accessPoint", 1),
          ("storeAndForward", 2),
          ("test", 3))
    )



class ModulationModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              16,
              32,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("qpsk", 4),
          ("qam16", 16),
          ("qam32", 32),
          ("qam64", 64),
          ("fsk9600", 65),
          ("fsk9600m", 66),
          ("fsk19200", 67),
          ("fsk19200m", 68),
          ("fsk3200", 69),
          ("fsk19200e", 70),
          ("fsk19200n", 71),
          ("fsk38400n", 72),
          ("fsk38400e", 73))
    )



class ModulationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qpsk", 0),
          ("qam16", 1),
          ("qam64", 2),
          ("automatic", 3))
    )



class SerialModulationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fsk9600", 3),
          ("fsk9600m", 4),
          ("fsk19200", 5))
    )



class AlarmFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("temperature", 0),
          ("notCalibrated", 23))
    )


class FirmwareRevision(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"


class InetIpAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class FrequencyType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class ChannelType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class FecType(TextualConvention, Integer32):
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
        *(("disabled", 0),
          ("adaptiveGain", 1),
          ("lowGain", 2))
    )



class RateType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_MIfLnMIBObjects_ObjectIdentity = ObjectIdentity
mIfLnMIBObjects = _MIfLnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1)
)
_MIfLnConfig_ObjectIdentity = ObjectIdentity
mIfLnConfig = _MIfLnConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 1)
)
_MIfLnStatus_ObjectIdentity = ObjectIdentity
mIfLnStatus = _MIfLnStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2)
)
_MIfLnStatusTable_Object = MibTable
mIfLnStatusTable = _MIfLnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mIfLnStatusTable.setStatus("current")
_MIfLnStatusEntry_Object = MibTableRow
mIfLnStatusEntry = _MIfLnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1)
)
mIfLnStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mIfLnStatusEntry.setStatus("current")
_MIfLnLinkStatus_Type = LinkStatus
_MIfLnLinkStatus_Object = MibTableColumn
mIfLnLinkStatus = _MIfLnLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 1),
    _MIfLnLinkStatus_Type()
)
mIfLnLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnLinkStatus.setStatus("current")
_MIfLnInitStatus_Type = InitStatus
_MIfLnInitStatus_Object = MibTableColumn
mIfLnInitStatus = _MIfLnInitStatus_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 2),
    _MIfLnInitStatus_Type()
)
mIfLnInitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnInitStatus.setStatus("current")
_MIfLnCurrentDeviceMode_Type = DeviceModeType
_MIfLnCurrentDeviceMode_Object = MibTableColumn
mIfLnCurrentDeviceMode = _MIfLnCurrentDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 3),
    _MIfLnCurrentDeviceMode_Type()
)
mIfLnCurrentDeviceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnCurrentDeviceMode.setStatus("current")
_MIfLnAlarms_Type = AlarmFlags
_MIfLnAlarms_Object = MibTableColumn
mIfLnAlarms = _MIfLnAlarms_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 4),
    _MIfLnAlarms_Type()
)
mIfLnAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnAlarms.setStatus("current")
_MIfLnSerialNumber_Type = Unsigned32
_MIfLnSerialNumber_Object = MibTableColumn
mIfLnSerialNumber = _MIfLnSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 5),
    _MIfLnSerialNumber_Type()
)
mIfLnSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnSerialNumber.setStatus("current")
_MIfLnFirmwareRevision_Type = FirmwareRevision
_MIfLnFirmwareRevision_Object = MibTableColumn
mIfLnFirmwareRevision = _MIfLnFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 6),
    _MIfLnFirmwareRevision_Type()
)
mIfLnFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnFirmwareRevision.setStatus("current")
_MIfLnHardwareId_Type = UnsignedByte
_MIfLnHardwareId_Object = MibTableColumn
mIfLnHardwareId = _MIfLnHardwareId_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 7),
    _MIfLnHardwareId_Type()
)
mIfLnHardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnHardwareId.setStatus("current")
_MIfLnHardwareRevision_Type = UnsignedByte
_MIfLnHardwareRevision_Object = MibTableColumn
mIfLnHardwareRevision = _MIfLnHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 8),
    _MIfLnHardwareRevision_Type()
)
mIfLnHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnHardwareRevision.setStatus("current")
_MIfLnTemperature_Type = Integer32
_MIfLnTemperature_Object = MibTableColumn
mIfLnTemperature = _MIfLnTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 9),
    _MIfLnTemperature_Type()
)
mIfLnTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnTemperature.setStatus("current")
_MIfLnApInfoApAddress_Type = MacAddress
_MIfLnApInfoApAddress_Object = MibTableColumn
mIfLnApInfoApAddress = _MIfLnApInfoApAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 10),
    _MIfLnApInfoApAddress_Type()
)
mIfLnApInfoApAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnApInfoApAddress.setStatus("current")
_MIfLnApInfoIpAddress_Type = InetIpAddress
_MIfLnApInfoIpAddress_Object = MibTableColumn
mIfLnApInfoIpAddress = _MIfLnApInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 11),
    _MIfLnApInfoIpAddress_Type()
)
mIfLnApInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnApInfoIpAddress.setStatus("current")
_MIfLnApInfoConnectedTime_Type = Integer32
_MIfLnApInfoConnectedTime_Object = MibTableColumn
mIfLnApInfoConnectedTime = _MIfLnApInfoConnectedTime_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 12),
    _MIfLnApInfoConnectedTime_Type()
)
mIfLnApInfoConnectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnApInfoConnectedTime.setStatus("current")
_MIfLnApInfoRssi_Type = Integer32
_MIfLnApInfoRssi_Object = MibTableColumn
mIfLnApInfoRssi = _MIfLnApInfoRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 13),
    _MIfLnApInfoRssi_Type()
)
mIfLnApInfoRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnApInfoRssi.setStatus("current")
_MIfLnApInfoEvm_Type = Unsigned32
_MIfLnApInfoEvm_Object = MibTableColumn
mIfLnApInfoEvm = _MIfLnApInfoEvm_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 14),
    _MIfLnApInfoEvm_Type()
)
mIfLnApInfoEvm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnApInfoEvm.setStatus("current")
_MIfLnApInfoMod_Type = ModulationModeType
_MIfLnApInfoMod_Object = MibTableColumn
mIfLnApInfoMod = _MIfLnApInfoMod_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 15),
    _MIfLnApInfoMod_Type()
)
mIfLnApInfoMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnApInfoMod.setStatus("current")
_MIfLnMacStatsTxSuccess_Type = Unsigned32
_MIfLnMacStatsTxSuccess_Object = MibTableColumn
mIfLnMacStatsTxSuccess = _MIfLnMacStatsTxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 16),
    _MIfLnMacStatsTxSuccess_Type()
)
mIfLnMacStatsTxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnMacStatsTxSuccess.setStatus("current")
_MIfLnMacStatsTxQueueFull_Type = Unsigned32
_MIfLnMacStatsTxQueueFull_Object = MibTableColumn
mIfLnMacStatsTxQueueFull = _MIfLnMacStatsTxQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 17),
    _MIfLnMacStatsTxQueueFull_Type()
)
mIfLnMacStatsTxQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnMacStatsTxQueueFull.setStatus("current")
_MIfLnMacStatsTxError_Type = Unsigned32
_MIfLnMacStatsTxError_Object = MibTableColumn
mIfLnMacStatsTxError = _MIfLnMacStatsTxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 18),
    _MIfLnMacStatsTxError_Type()
)
mIfLnMacStatsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnMacStatsTxError.setStatus("current")
_MIfLnMacStatsTxRetry_Type = Unsigned32
_MIfLnMacStatsTxRetry_Object = MibTableColumn
mIfLnMacStatsTxRetry = _MIfLnMacStatsTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 19),
    _MIfLnMacStatsTxRetry_Type()
)
mIfLnMacStatsTxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnMacStatsTxRetry.setStatus("current")
_MIfLnMacStatsRxSuccess_Type = Unsigned32
_MIfLnMacStatsRxSuccess_Object = MibTableColumn
mIfLnMacStatsRxSuccess = _MIfLnMacStatsRxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 20),
    _MIfLnMacStatsRxSuccess_Type()
)
mIfLnMacStatsRxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnMacStatsRxSuccess.setStatus("current")
_MIfLnModemStatsTxSuccess_Type = Unsigned32
_MIfLnModemStatsTxSuccess_Object = MibTableColumn
mIfLnModemStatsTxSuccess = _MIfLnModemStatsTxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 21),
    _MIfLnModemStatsTxSuccess_Type()
)
mIfLnModemStatsTxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnModemStatsTxSuccess.setStatus("current")
_MIfLnModemStatsTxError_Type = Unsigned32
_MIfLnModemStatsTxError_Object = MibTableColumn
mIfLnModemStatsTxError = _MIfLnModemStatsTxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 22),
    _MIfLnModemStatsTxError_Type()
)
mIfLnModemStatsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnModemStatsTxError.setStatus("current")
_MIfLnModemStatsRxSuccess_Type = Unsigned32
_MIfLnModemStatsRxSuccess_Object = MibTableColumn
mIfLnModemStatsRxSuccess = _MIfLnModemStatsRxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 23),
    _MIfLnModemStatsRxSuccess_Type()
)
mIfLnModemStatsRxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnModemStatsRxSuccess.setStatus("current")
_MIfLnModemStatsRxError_Type = Unsigned32
_MIfLnModemStatsRxError_Object = MibTableColumn
mIfLnModemStatsRxError = _MIfLnModemStatsRxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 24),
    _MIfLnModemStatsRxError_Type()
)
mIfLnModemStatsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnModemStatsRxError.setStatus("current")
_MIfLnActiveTxFrequency_Type = FrequencyType
_MIfLnActiveTxFrequency_Object = MibTableColumn
mIfLnActiveTxFrequency = _MIfLnActiveTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 25),
    _MIfLnActiveTxFrequency_Type()
)
mIfLnActiveTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnActiveTxFrequency.setStatus("current")
_MIfLnActiveRxFrequency_Type = FrequencyType
_MIfLnActiveRxFrequency_Object = MibTableColumn
mIfLnActiveRxFrequency = _MIfLnActiveRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 26),
    _MIfLnActiveRxFrequency_Type()
)
mIfLnActiveRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnActiveRxFrequency.setStatus("current")
_MIfLnActiveChannel_Type = ChannelType
_MIfLnActiveChannel_Object = MibTableColumn
mIfLnActiveChannel = _MIfLnActiveChannel_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 27),
    _MIfLnActiveChannel_Type()
)
mIfLnActiveChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnActiveChannel.setStatus("current")
_MIfLnActiveModulation_Type = ModulationType
_MIfLnActiveModulation_Object = MibTableColumn
mIfLnActiveModulation = _MIfLnActiveModulation_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 28),
    _MIfLnActiveModulation_Type()
)
mIfLnActiveModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnActiveModulation.setStatus("current")
_MIfLnActiveFec_Type = FecType
_MIfLnActiveFec_Object = MibTableColumn
mIfLnActiveFec = _MIfLnActiveFec_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 29),
    _MIfLnActiveFec_Type()
)
mIfLnActiveFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnActiveFec.setStatus("current")
_MIfLnLastRssi_Type = Integer32
_MIfLnLastRssi_Object = MibTableColumn
mIfLnLastRssi = _MIfLnLastRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 30),
    _MIfLnLastRssi_Type()
)
mIfLnLastRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnLastRssi.setStatus("current")
_MIfLnLastEvm_Type = Unsigned32
_MIfLnLastEvm_Object = MibTableColumn
mIfLnLastEvm = _MIfLnLastEvm_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 31),
    _MIfLnLastEvm_Type()
)
mIfLnLastEvm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnLastEvm.setStatus("current")
_MIfLnLastMod_Type = ModulationModeType
_MIfLnLastMod_Object = MibTableColumn
mIfLnLastMod = _MIfLnLastMod_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 32),
    _MIfLnLastMod_Type()
)
mIfLnLastMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnLastMod.setStatus("current")
_MIfLnLastRate_Type = RateType
_MIfLnLastRate_Object = MibTableColumn
mIfLnLastRate = _MIfLnLastRate_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 33),
    _MIfLnLastRate_Type()
)
mIfLnLastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnLastRate.setStatus("current")
_MIfLnActiveNic_Type = TruthValue
_MIfLnActiveNic_Object = MibTableColumn
mIfLnActiveNic = _MIfLnActiveNic_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 34),
    _MIfLnActiveNic_Type()
)
mIfLnActiveNic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnActiveNic.setStatus("current")
_MIfLnStatusConnRemTable_Object = MibTable
mIfLnStatusConnRemTable = _MIfLnStatusConnRemTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mIfLnStatusConnRemTable.setStatus("current")
_MIfLnStatusConnRemEntry_Object = MibTableRow
mIfLnStatusConnRemEntry = _MIfLnStatusConnRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1)
)
mIfLnStatusConnRemEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MDS-IF-LN-MIB", "mIfLnStatusConnRemAddress"),
)
if mibBuilder.loadTexts:
    mIfLnStatusConnRemEntry.setStatus("current")
_MIfLnStatusConnRemAddress_Type = MacAddress
_MIfLnStatusConnRemAddress_Object = MibTableColumn
mIfLnStatusConnRemAddress = _MIfLnStatusConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 1),
    _MIfLnStatusConnRemAddress_Type()
)
mIfLnStatusConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemAddress.setStatus("current")
_MIfLnStatusConnRemIpAddress_Type = InetIpAddress
_MIfLnStatusConnRemIpAddress_Object = MibTableColumn
mIfLnStatusConnRemIpAddress = _MIfLnStatusConnRemIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 2),
    _MIfLnStatusConnRemIpAddress_Type()
)
mIfLnStatusConnRemIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemIpAddress.setStatus("current")
_MIfLnStatusConnRemTimeToLive_Type = Unsigned32
_MIfLnStatusConnRemTimeToLive_Object = MibTableColumn
mIfLnStatusConnRemTimeToLive = _MIfLnStatusConnRemTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 3),
    _MIfLnStatusConnRemTimeToLive_Type()
)
mIfLnStatusConnRemTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemTimeToLive.setStatus("current")
_MIfLnStatusConnRemLinkStatus_Type = LinkStatus
_MIfLnStatusConnRemLinkStatus_Object = MibTableColumn
mIfLnStatusConnRemLinkStatus = _MIfLnStatusConnRemLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 4),
    _MIfLnStatusConnRemLinkStatus_Type()
)
mIfLnStatusConnRemLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemLinkStatus.setStatus("current")
_MIfLnStatusConnRemNicId_Type = UnsignedShort
_MIfLnStatusConnRemNicId_Object = MibTableColumn
mIfLnStatusConnRemNicId = _MIfLnStatusConnRemNicId_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 5),
    _MIfLnStatusConnRemNicId_Type()
)
mIfLnStatusConnRemNicId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemNicId.setStatus("current")
_MIfLnStatusConnRemRssi_Type = Integer32
_MIfLnStatusConnRemRssi_Object = MibTableColumn
mIfLnStatusConnRemRssi = _MIfLnStatusConnRemRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 6),
    _MIfLnStatusConnRemRssi_Type()
)
mIfLnStatusConnRemRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemRssi.setStatus("current")
_MIfLnStatusConnRemEvm_Type = Unsigned32
_MIfLnStatusConnRemEvm_Object = MibTableColumn
mIfLnStatusConnRemEvm = _MIfLnStatusConnRemEvm_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 7),
    _MIfLnStatusConnRemEvm_Type()
)
mIfLnStatusConnRemEvm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemEvm.setStatus("current")
_MIfLnStatusConnRemMod_Type = ModulationModeType
_MIfLnStatusConnRemMod_Object = MibTableColumn
mIfLnStatusConnRemMod = _MIfLnStatusConnRemMod_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 8),
    _MIfLnStatusConnRemMod_Type()
)
mIfLnStatusConnRemMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemMod.setStatus("current")
_MIfLnStatusConnRemStatsTxPackets_Type = Unsigned32
_MIfLnStatusConnRemStatsTxPackets_Object = MibTableColumn
mIfLnStatusConnRemStatsTxPackets = _MIfLnStatusConnRemStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 9),
    _MIfLnStatusConnRemStatsTxPackets_Type()
)
mIfLnStatusConnRemStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsTxPackets.setStatus("current")
_MIfLnStatusConnRemStatsTxBytes_Type = Unsigned32
_MIfLnStatusConnRemStatsTxBytes_Object = MibTableColumn
mIfLnStatusConnRemStatsTxBytes = _MIfLnStatusConnRemStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 10),
    _MIfLnStatusConnRemStatsTxBytes_Type()
)
mIfLnStatusConnRemStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsTxBytes.setStatus("current")
_MIfLnStatusConnRemStatsRxPackets_Type = Unsigned32
_MIfLnStatusConnRemStatsRxPackets_Object = MibTableColumn
mIfLnStatusConnRemStatsRxPackets = _MIfLnStatusConnRemStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 11),
    _MIfLnStatusConnRemStatsRxPackets_Type()
)
mIfLnStatusConnRemStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsRxPackets.setStatus("current")
_MIfLnStatusConnRemStatsRxBytes_Type = Unsigned32
_MIfLnStatusConnRemStatsRxBytes_Object = MibTableColumn
mIfLnStatusConnRemStatsRxBytes = _MIfLnStatusConnRemStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 12),
    _MIfLnStatusConnRemStatsRxBytes_Type()
)
mIfLnStatusConnRemStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsRxBytes.setStatus("current")
_MIfLnStatusConnRemStatsTxError_Type = Unsigned32
_MIfLnStatusConnRemStatsTxError_Object = MibTableColumn
mIfLnStatusConnRemStatsTxError = _MIfLnStatusConnRemStatsTxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 13),
    _MIfLnStatusConnRemStatsTxError_Type()
)
mIfLnStatusConnRemStatsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsTxError.setStatus("current")
_MIfLnStatusConnRemStatsRxError_Type = Unsigned32
_MIfLnStatusConnRemStatsRxError_Object = MibTableColumn
mIfLnStatusConnRemStatsRxError = _MIfLnStatusConnRemStatsRxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 14),
    _MIfLnStatusConnRemStatsRxError_Type()
)
mIfLnStatusConnRemStatsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsRxError.setStatus("current")
_MIfLnStatusConnRemStatsTxDrop_Type = Unsigned32
_MIfLnStatusConnRemStatsTxDrop_Object = MibTableColumn
mIfLnStatusConnRemStatsTxDrop = _MIfLnStatusConnRemStatsTxDrop_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 15),
    _MIfLnStatusConnRemStatsTxDrop_Type()
)
mIfLnStatusConnRemStatsTxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsTxDrop.setStatus("current")
_MIfLnStatusConnRemStatsRxDrop_Type = Unsigned32
_MIfLnStatusConnRemStatsRxDrop_Object = MibTableColumn
mIfLnStatusConnRemStatsRxDrop = _MIfLnStatusConnRemStatsRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 16),
    _MIfLnStatusConnRemStatsRxDrop_Type()
)
mIfLnStatusConnRemStatsRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsRxDrop.setStatus("current")
_MIfLnStatusConnRemStatsGateway_Type = MacAddress
_MIfLnStatusConnRemStatsGateway_Object = MibTableColumn
mIfLnStatusConnRemStatsGateway = _MIfLnStatusConnRemStatsGateway_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 17),
    _MIfLnStatusConnRemStatsGateway_Type()
)
mIfLnStatusConnRemStatsGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsGateway.setStatus("current")
_MIfLnStatusConnRemStatsAllIp_Type = OctetString
_MIfLnStatusConnRemStatsAllIp_Object = MibTableColumn
mIfLnStatusConnRemStatsAllIp = _MIfLnStatusConnRemStatsAllIp_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 18),
    _MIfLnStatusConnRemStatsAllIp_Type()
)
mIfLnStatusConnRemStatsAllIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsAllIp.setStatus("current")
_MIfLnStatusConnRemStatsName_Type = OctetString
_MIfLnStatusConnRemStatsName_Object = MibTableColumn
mIfLnStatusConnRemStatsName = _MIfLnStatusConnRemStatsName_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 19),
    _MIfLnStatusConnRemStatsName_Type()
)
mIfLnStatusConnRemStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsName.setStatus("current")
_MIfLnStatusConnRemStatsAlarmed_Type = TruthValue
_MIfLnStatusConnRemStatsAlarmed_Object = MibTableColumn
mIfLnStatusConnRemStatsAlarmed = _MIfLnStatusConnRemStatsAlarmed_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 20),
    _MIfLnStatusConnRemStatsAlarmed_Type()
)
mIfLnStatusConnRemStatsAlarmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsAlarmed.setStatus("current")
_MIfLnStatusConnRemStatsVersion_Type = OctetString
_MIfLnStatusConnRemStatsVersion_Object = MibTableColumn
mIfLnStatusConnRemStatsVersion = _MIfLnStatusConnRemStatsVersion_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 21),
    _MIfLnStatusConnRemStatsVersion_Type()
)
mIfLnStatusConnRemStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsVersion.setStatus("current")


class _MIfLnStatusConnRemStatsTemp_Type(Integer32):
    """Custom type mIfLnStatusConnRemStatsTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MIfLnStatusConnRemStatsTemp_Type.__name__ = "Integer32"
_MIfLnStatusConnRemStatsTemp_Object = MibTableColumn
mIfLnStatusConnRemStatsTemp = _MIfLnStatusConnRemStatsTemp_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 22),
    _MIfLnStatusConnRemStatsTemp_Type()
)
mIfLnStatusConnRemStatsTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsTemp.setStatus("current")
_MIfLnStatusConnRemStatsDwnRssi_Type = Integer32
_MIfLnStatusConnRemStatsDwnRssi_Object = MibTableColumn
mIfLnStatusConnRemStatsDwnRssi = _MIfLnStatusConnRemStatsDwnRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 23),
    _MIfLnStatusConnRemStatsDwnRssi_Type()
)
mIfLnStatusConnRemStatsDwnRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsDwnRssi.setStatus("current")
_MIfLnStatusConnRemStatsDwnEvm_Type = Unsigned32
_MIfLnStatusConnRemStatsDwnEvm_Object = MibTableColumn
mIfLnStatusConnRemStatsDwnEvm = _MIfLnStatusConnRemStatsDwnEvm_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 24),
    _MIfLnStatusConnRemStatsDwnEvm_Type()
)
mIfLnStatusConnRemStatsDwnEvm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsDwnEvm.setStatus("current")
_MIfLnStatusConnRemStatsDwnMod_Type = ModulationModeType
_MIfLnStatusConnRemStatsDwnMod_Object = MibTableColumn
mIfLnStatusConnRemStatsDwnMod = _MIfLnStatusConnRemStatsDwnMod_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 25),
    _MIfLnStatusConnRemStatsDwnMod_Type()
)
mIfLnStatusConnRemStatsDwnMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusConnRemStatsDwnMod.setStatus("current")
_MIfLnStatusEndpointTable_Object = MibTable
mIfLnStatusEndpointTable = _MIfLnStatusEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mIfLnStatusEndpointTable.setStatus("current")
_MIfLnStatusEndpointEntry_Object = MibTableRow
mIfLnStatusEndpointEntry = _MIfLnStatusEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1)
)
mIfLnStatusEndpointEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MDS-IF-LN-MIB", "mIfLnStatusEndpointAddress"),
)
if mibBuilder.loadTexts:
    mIfLnStatusEndpointEntry.setStatus("current")
_MIfLnStatusEndpointAddress_Type = MacAddress
_MIfLnStatusEndpointAddress_Object = MibTableColumn
mIfLnStatusEndpointAddress = _MIfLnStatusEndpointAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 1),
    _MIfLnStatusEndpointAddress_Type()
)
mIfLnStatusEndpointAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusEndpointAddress.setStatus("current")
_MIfLnStatusEndpointIpAddress_Type = InetIpAddress
_MIfLnStatusEndpointIpAddress_Object = MibTableColumn
mIfLnStatusEndpointIpAddress = _MIfLnStatusEndpointIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 2),
    _MIfLnStatusEndpointIpAddress_Type()
)
mIfLnStatusEndpointIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusEndpointIpAddress.setStatus("current")
_MIfLnStatusEndpointTimeToLive_Type = Unsigned32
_MIfLnStatusEndpointTimeToLive_Object = MibTableColumn
mIfLnStatusEndpointTimeToLive = _MIfLnStatusEndpointTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 3),
    _MIfLnStatusEndpointTimeToLive_Type()
)
mIfLnStatusEndpointTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusEndpointTimeToLive.setStatus("current")
_MIfLnStatusEndpointRemAddress_Type = MacAddress
_MIfLnStatusEndpointRemAddress_Object = MibTableColumn
mIfLnStatusEndpointRemAddress = _MIfLnStatusEndpointRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 4),
    _MIfLnStatusEndpointRemAddress_Type()
)
mIfLnStatusEndpointRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusEndpointRemAddress.setStatus("current")
_MIfLnStatusEndpointStatsTxPackets_Type = Unsigned32
_MIfLnStatusEndpointStatsTxPackets_Object = MibTableColumn
mIfLnStatusEndpointStatsTxPackets = _MIfLnStatusEndpointStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 5),
    _MIfLnStatusEndpointStatsTxPackets_Type()
)
mIfLnStatusEndpointStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusEndpointStatsTxPackets.setStatus("current")
_MIfLnStatusEndpointStatsTxBytes_Type = Unsigned32
_MIfLnStatusEndpointStatsTxBytes_Object = MibTableColumn
mIfLnStatusEndpointStatsTxBytes = _MIfLnStatusEndpointStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 6),
    _MIfLnStatusEndpointStatsTxBytes_Type()
)
mIfLnStatusEndpointStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusEndpointStatsTxBytes.setStatus("current")
_MIfLnStatusEndpointStatsRxPackets_Type = Unsigned32
_MIfLnStatusEndpointStatsRxPackets_Object = MibTableColumn
mIfLnStatusEndpointStatsRxPackets = _MIfLnStatusEndpointStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 7),
    _MIfLnStatusEndpointStatsRxPackets_Type()
)
mIfLnStatusEndpointStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusEndpointStatsRxPackets.setStatus("current")
_MIfLnStatusEndpointStatsRxBytes_Type = Unsigned32
_MIfLnStatusEndpointStatsRxBytes_Object = MibTableColumn
mIfLnStatusEndpointStatsRxBytes = _MIfLnStatusEndpointStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 8),
    _MIfLnStatusEndpointStatsRxBytes_Type()
)
mIfLnStatusEndpointStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusEndpointStatsRxBytes.setStatus("current")
_MIfLnStatusEndpointStatsTxError_Type = Unsigned32
_MIfLnStatusEndpointStatsTxError_Object = MibTableColumn
mIfLnStatusEndpointStatsTxError = _MIfLnStatusEndpointStatsTxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 9),
    _MIfLnStatusEndpointStatsTxError_Type()
)
mIfLnStatusEndpointStatsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusEndpointStatsTxError.setStatus("current")
_MIfLnStatusEndpointStatsRxError_Type = Unsigned32
_MIfLnStatusEndpointStatsRxError_Object = MibTableColumn
mIfLnStatusEndpointStatsRxError = _MIfLnStatusEndpointStatsRxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 10),
    _MIfLnStatusEndpointStatsRxError_Type()
)
mIfLnStatusEndpointStatsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusEndpointStatsRxError.setStatus("current")
_MIfLnStatusEndpointStatsTxDrop_Type = Unsigned32
_MIfLnStatusEndpointStatsTxDrop_Object = MibTableColumn
mIfLnStatusEndpointStatsTxDrop = _MIfLnStatusEndpointStatsTxDrop_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 11),
    _MIfLnStatusEndpointStatsTxDrop_Type()
)
mIfLnStatusEndpointStatsTxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusEndpointStatsTxDrop.setStatus("current")
_MIfLnStatusEndpointStatsRxDrop_Type = Unsigned32
_MIfLnStatusEndpointStatsRxDrop_Object = MibTableColumn
mIfLnStatusEndpointStatsRxDrop = _MIfLnStatusEndpointStatsRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 12),
    _MIfLnStatusEndpointStatsRxDrop_Type()
)
mIfLnStatusEndpointStatsRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLnStatusEndpointStatsRxDrop.setStatus("current")
_MdsIfLnMIBConformance_ObjectIdentity = ObjectIdentity
mdsIfLnMIBConformance = _MdsIfLnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3)
)
_MdsIfLnMIBCompliances_ObjectIdentity = ObjectIdentity
mdsIfLnMIBCompliances = _MdsIfLnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 1)
)
_MdsIfLnMIBGroups_ObjectIdentity = ObjectIdentity
mdsIfLnMIBGroups = _MdsIfLnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 2)
)

# Managed Objects groups

mIfLnStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 2, 1)
)
mIfLnStatusGroup.setObjects(
      *(("MDS-IF-LN-MIB", "mIfLnLinkStatus"),
        ("MDS-IF-LN-MIB", "mIfLnInitStatus"),
        ("MDS-IF-LN-MIB", "mIfLnCurrentDeviceMode"),
        ("MDS-IF-LN-MIB", "mIfLnAlarms"),
        ("MDS-IF-LN-MIB", "mIfLnSerialNumber"),
        ("MDS-IF-LN-MIB", "mIfLnFirmwareRevision"),
        ("MDS-IF-LN-MIB", "mIfLnHardwareId"),
        ("MDS-IF-LN-MIB", "mIfLnHardwareRevision"),
        ("MDS-IF-LN-MIB", "mIfLnTemperature"),
        ("MDS-IF-LN-MIB", "mIfLnApInfoApAddress"),
        ("MDS-IF-LN-MIB", "mIfLnApInfoIpAddress"),
        ("MDS-IF-LN-MIB", "mIfLnApInfoConnectedTime"),
        ("MDS-IF-LN-MIB", "mIfLnApInfoRssi"),
        ("MDS-IF-LN-MIB", "mIfLnApInfoEvm"),
        ("MDS-IF-LN-MIB", "mIfLnApInfoMod"),
        ("MDS-IF-LN-MIB", "mIfLnMacStatsTxSuccess"),
        ("MDS-IF-LN-MIB", "mIfLnMacStatsTxQueueFull"),
        ("MDS-IF-LN-MIB", "mIfLnMacStatsTxError"),
        ("MDS-IF-LN-MIB", "mIfLnMacStatsTxRetry"),
        ("MDS-IF-LN-MIB", "mIfLnMacStatsRxSuccess"),
        ("MDS-IF-LN-MIB", "mIfLnModemStatsTxSuccess"),
        ("MDS-IF-LN-MIB", "mIfLnModemStatsTxError"),
        ("MDS-IF-LN-MIB", "mIfLnModemStatsRxSuccess"),
        ("MDS-IF-LN-MIB", "mIfLnModemStatsRxError"),
        ("MDS-IF-LN-MIB", "mIfLnActiveTxFrequency"),
        ("MDS-IF-LN-MIB", "mIfLnActiveRxFrequency"),
        ("MDS-IF-LN-MIB", "mIfLnActiveChannel"),
        ("MDS-IF-LN-MIB", "mIfLnActiveModulation"),
        ("MDS-IF-LN-MIB", "mIfLnActiveFec"),
        ("MDS-IF-LN-MIB", "mIfLnLastRssi"),
        ("MDS-IF-LN-MIB", "mIfLnLastEvm"),
        ("MDS-IF-LN-MIB", "mIfLnLastMod"),
        ("MDS-IF-LN-MIB", "mIfLnLastRate"),
        ("MDS-IF-LN-MIB", "mIfLnActiveNic"))
)
if mibBuilder.loadTexts:
    mIfLnStatusGroup.setStatus("current")

mIfLnStatusConnRemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 2, 2)
)
mIfLnStatusConnRemGroup.setObjects(
      *(("MDS-IF-LN-MIB", "mIfLnStatusConnRemAddress"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemIpAddress"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemTimeToLive"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemLinkStatus"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemNicId"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemRssi"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemEvm"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemMod"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTxPackets"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTxBytes"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsRxPackets"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsRxBytes"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTxError"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsRxError"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTxDrop"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsRxDrop"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsGateway"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsAllIp"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsName"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsAlarmed"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsVersion"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTemp"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsDwnRssi"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsDwnEvm"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsDwnMod"))
)
if mibBuilder.loadTexts:
    mIfLnStatusConnRemGroup.setStatus("current")

mIfLnStatusEndpointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 2, 3)
)
mIfLnStatusEndpointGroup.setObjects(
      *(("MDS-IF-LN-MIB", "mIfLnStatusEndpointAddress"),
        ("MDS-IF-LN-MIB", "mIfLnStatusEndpointIpAddress"),
        ("MDS-IF-LN-MIB", "mIfLnStatusEndpointTimeToLive"),
        ("MDS-IF-LN-MIB", "mIfLnStatusEndpointRemAddress"),
        ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsTxPackets"),
        ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsTxBytes"),
        ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsRxPackets"),
        ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsRxBytes"),
        ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsTxError"),
        ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsRxError"),
        ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsTxDrop"),
        ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsRxDrop"))
)
if mibBuilder.loadTexts:
    mIfLnStatusEndpointGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mIfLnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 1, 1)
)
mIfLnCompliance.setObjects(
      *(("MDS-IF-LN-MIB", "mIfLnStatusGroup"),
        ("MDS-IF-LN-MIB", "mIfLnStatusConnRemGroup"),
        ("MDS-IF-LN-MIB", "mIfLnStatusEndpointGroup"))
)
if mibBuilder.loadTexts:
    mIfLnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MDS-IF-LN-MIB",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "LinkStatus": LinkStatus,
       "InitStatus": InitStatus,
       "DeviceModeType": DeviceModeType,
       "ModulationModeType": ModulationModeType,
       "ModulationType": ModulationType,
       "SerialModulationType": SerialModulationType,
       "AlarmFlags": AlarmFlags,
       "FirmwareRevision": FirmwareRevision,
       "InetIpAddress": InetIpAddress,
       "FrequencyType": FrequencyType,
       "ChannelType": ChannelType,
       "FecType": FecType,
       "RateType": RateType,
       "mdsIfLnMIB": mdsIfLnMIB,
       "mIfLnMIBObjects": mIfLnMIBObjects,
       "mIfLnConfig": mIfLnConfig,
       "mIfLnStatus": mIfLnStatus,
       "mIfLnStatusTable": mIfLnStatusTable,
       "mIfLnStatusEntry": mIfLnStatusEntry,
       "mIfLnLinkStatus": mIfLnLinkStatus,
       "mIfLnInitStatus": mIfLnInitStatus,
       "mIfLnCurrentDeviceMode": mIfLnCurrentDeviceMode,
       "mIfLnAlarms": mIfLnAlarms,
       "mIfLnSerialNumber": mIfLnSerialNumber,
       "mIfLnFirmwareRevision": mIfLnFirmwareRevision,
       "mIfLnHardwareId": mIfLnHardwareId,
       "mIfLnHardwareRevision": mIfLnHardwareRevision,
       "mIfLnTemperature": mIfLnTemperature,
       "mIfLnApInfoApAddress": mIfLnApInfoApAddress,
       "mIfLnApInfoIpAddress": mIfLnApInfoIpAddress,
       "mIfLnApInfoConnectedTime": mIfLnApInfoConnectedTime,
       "mIfLnApInfoRssi": mIfLnApInfoRssi,
       "mIfLnApInfoEvm": mIfLnApInfoEvm,
       "mIfLnApInfoMod": mIfLnApInfoMod,
       "mIfLnMacStatsTxSuccess": mIfLnMacStatsTxSuccess,
       "mIfLnMacStatsTxQueueFull": mIfLnMacStatsTxQueueFull,
       "mIfLnMacStatsTxError": mIfLnMacStatsTxError,
       "mIfLnMacStatsTxRetry": mIfLnMacStatsTxRetry,
       "mIfLnMacStatsRxSuccess": mIfLnMacStatsRxSuccess,
       "mIfLnModemStatsTxSuccess": mIfLnModemStatsTxSuccess,
       "mIfLnModemStatsTxError": mIfLnModemStatsTxError,
       "mIfLnModemStatsRxSuccess": mIfLnModemStatsRxSuccess,
       "mIfLnModemStatsRxError": mIfLnModemStatsRxError,
       "mIfLnActiveTxFrequency": mIfLnActiveTxFrequency,
       "mIfLnActiveRxFrequency": mIfLnActiveRxFrequency,
       "mIfLnActiveChannel": mIfLnActiveChannel,
       "mIfLnActiveModulation": mIfLnActiveModulation,
       "mIfLnActiveFec": mIfLnActiveFec,
       "mIfLnLastRssi": mIfLnLastRssi,
       "mIfLnLastEvm": mIfLnLastEvm,
       "mIfLnLastMod": mIfLnLastMod,
       "mIfLnLastRate": mIfLnLastRate,
       "mIfLnActiveNic": mIfLnActiveNic,
       "mIfLnStatusConnRemTable": mIfLnStatusConnRemTable,
       "mIfLnStatusConnRemEntry": mIfLnStatusConnRemEntry,
       "mIfLnStatusConnRemAddress": mIfLnStatusConnRemAddress,
       "mIfLnStatusConnRemIpAddress": mIfLnStatusConnRemIpAddress,
       "mIfLnStatusConnRemTimeToLive": mIfLnStatusConnRemTimeToLive,
       "mIfLnStatusConnRemLinkStatus": mIfLnStatusConnRemLinkStatus,
       "mIfLnStatusConnRemNicId": mIfLnStatusConnRemNicId,
       "mIfLnStatusConnRemRssi": mIfLnStatusConnRemRssi,
       "mIfLnStatusConnRemEvm": mIfLnStatusConnRemEvm,
       "mIfLnStatusConnRemMod": mIfLnStatusConnRemMod,
       "mIfLnStatusConnRemStatsTxPackets": mIfLnStatusConnRemStatsTxPackets,
       "mIfLnStatusConnRemStatsTxBytes": mIfLnStatusConnRemStatsTxBytes,
       "mIfLnStatusConnRemStatsRxPackets": mIfLnStatusConnRemStatsRxPackets,
       "mIfLnStatusConnRemStatsRxBytes": mIfLnStatusConnRemStatsRxBytes,
       "mIfLnStatusConnRemStatsTxError": mIfLnStatusConnRemStatsTxError,
       "mIfLnStatusConnRemStatsRxError": mIfLnStatusConnRemStatsRxError,
       "mIfLnStatusConnRemStatsTxDrop": mIfLnStatusConnRemStatsTxDrop,
       "mIfLnStatusConnRemStatsRxDrop": mIfLnStatusConnRemStatsRxDrop,
       "mIfLnStatusConnRemStatsGateway": mIfLnStatusConnRemStatsGateway,
       "mIfLnStatusConnRemStatsAllIp": mIfLnStatusConnRemStatsAllIp,
       "mIfLnStatusConnRemStatsName": mIfLnStatusConnRemStatsName,
       "mIfLnStatusConnRemStatsAlarmed": mIfLnStatusConnRemStatsAlarmed,
       "mIfLnStatusConnRemStatsVersion": mIfLnStatusConnRemStatsVersion,
       "mIfLnStatusConnRemStatsTemp": mIfLnStatusConnRemStatsTemp,
       "mIfLnStatusConnRemStatsDwnRssi": mIfLnStatusConnRemStatsDwnRssi,
       "mIfLnStatusConnRemStatsDwnEvm": mIfLnStatusConnRemStatsDwnEvm,
       "mIfLnStatusConnRemStatsDwnMod": mIfLnStatusConnRemStatsDwnMod,
       "mIfLnStatusEndpointTable": mIfLnStatusEndpointTable,
       "mIfLnStatusEndpointEntry": mIfLnStatusEndpointEntry,
       "mIfLnStatusEndpointAddress": mIfLnStatusEndpointAddress,
       "mIfLnStatusEndpointIpAddress": mIfLnStatusEndpointIpAddress,
       "mIfLnStatusEndpointTimeToLive": mIfLnStatusEndpointTimeToLive,
       "mIfLnStatusEndpointRemAddress": mIfLnStatusEndpointRemAddress,
       "mIfLnStatusEndpointStatsTxPackets": mIfLnStatusEndpointStatsTxPackets,
       "mIfLnStatusEndpointStatsTxBytes": mIfLnStatusEndpointStatsTxBytes,
       "mIfLnStatusEndpointStatsRxPackets": mIfLnStatusEndpointStatsRxPackets,
       "mIfLnStatusEndpointStatsRxBytes": mIfLnStatusEndpointStatsRxBytes,
       "mIfLnStatusEndpointStatsTxError": mIfLnStatusEndpointStatsTxError,
       "mIfLnStatusEndpointStatsRxError": mIfLnStatusEndpointStatsRxError,
       "mIfLnStatusEndpointStatsTxDrop": mIfLnStatusEndpointStatsTxDrop,
       "mIfLnStatusEndpointStatsRxDrop": mIfLnStatusEndpointStatsRxDrop,
       "mdsIfLnMIBConformance": mdsIfLnMIBConformance,
       "mdsIfLnMIBCompliances": mdsIfLnMIBCompliances,
       "mIfLnCompliance": mIfLnCompliance,
       "mdsIfLnMIBGroups": mdsIfLnMIBGroups,
       "mIfLnStatusGroup": mIfLnStatusGroup,
       "mIfLnStatusConnRemGroup": mIfLnStatusConnRemGroup,
       "mIfLnStatusEndpointGroup": mIfLnStatusEndpointGroup}
)
