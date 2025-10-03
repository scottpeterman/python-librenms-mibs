# SNMP MIB module (MDS-IF-LW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gemds\MDS-IF-LW-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:29 2025
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

mdsIfLwMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6)
)
if mibBuilder.loadTexts:
    mdsIfLwMIB.setRevisions(
        ("2018-09-13 00:00",)
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
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("qpsk25", 2),
          ("qpsk50", 3),
          ("qpsk75", 4),
          ("qam16r50", 5),
          ("qam16r75", 6))
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

_MIfLwMIBObjects_ObjectIdentity = ObjectIdentity
mIfLwMIBObjects = _MIfLwMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1)
)
_MIfLwConfig_ObjectIdentity = ObjectIdentity
mIfLwConfig = _MIfLwConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 1)
)
_MIfLwStatus_ObjectIdentity = ObjectIdentity
mIfLwStatus = _MIfLwStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2)
)
_MIfLwStatusTable_Object = MibTable
mIfLwStatusTable = _MIfLwStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mIfLwStatusTable.setStatus("current")
_MIfLwStatusEntry_Object = MibTableRow
mIfLwStatusEntry = _MIfLwStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1)
)
mIfLwStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mIfLwStatusEntry.setStatus("current")
_MIfLwLinkStatus_Type = LinkStatus
_MIfLwLinkStatus_Object = MibTableColumn
mIfLwLinkStatus = _MIfLwLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 1),
    _MIfLwLinkStatus_Type()
)
mIfLwLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwLinkStatus.setStatus("current")
_MIfLwInitStatus_Type = InitStatus
_MIfLwInitStatus_Object = MibTableColumn
mIfLwInitStatus = _MIfLwInitStatus_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 2),
    _MIfLwInitStatus_Type()
)
mIfLwInitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwInitStatus.setStatus("current")
_MIfLwCurrentDeviceMode_Type = DeviceModeType
_MIfLwCurrentDeviceMode_Object = MibTableColumn
mIfLwCurrentDeviceMode = _MIfLwCurrentDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 3),
    _MIfLwCurrentDeviceMode_Type()
)
mIfLwCurrentDeviceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwCurrentDeviceMode.setStatus("current")
_MIfLwAlarms_Type = AlarmFlags
_MIfLwAlarms_Object = MibTableColumn
mIfLwAlarms = _MIfLwAlarms_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 4),
    _MIfLwAlarms_Type()
)
mIfLwAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwAlarms.setStatus("current")
_MIfLwSerialNumber_Type = Unsigned32
_MIfLwSerialNumber_Object = MibTableColumn
mIfLwSerialNumber = _MIfLwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 5),
    _MIfLwSerialNumber_Type()
)
mIfLwSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwSerialNumber.setStatus("current")
_MIfLwFirmwareRevision_Type = FirmwareRevision
_MIfLwFirmwareRevision_Object = MibTableColumn
mIfLwFirmwareRevision = _MIfLwFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 6),
    _MIfLwFirmwareRevision_Type()
)
mIfLwFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwFirmwareRevision.setStatus("current")
_MIfLwHardwareId_Type = UnsignedByte
_MIfLwHardwareId_Object = MibTableColumn
mIfLwHardwareId = _MIfLwHardwareId_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 7),
    _MIfLwHardwareId_Type()
)
mIfLwHardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwHardwareId.setStatus("current")
_MIfLwHardwareRevision_Type = UnsignedByte
_MIfLwHardwareRevision_Object = MibTableColumn
mIfLwHardwareRevision = _MIfLwHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 8),
    _MIfLwHardwareRevision_Type()
)
mIfLwHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwHardwareRevision.setStatus("current")
_MIfLwTemperature_Type = Integer32
_MIfLwTemperature_Object = MibTableColumn
mIfLwTemperature = _MIfLwTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 9),
    _MIfLwTemperature_Type()
)
mIfLwTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwTemperature.setStatus("current")
_MIfLwApInfoApAddress_Type = MacAddress
_MIfLwApInfoApAddress_Object = MibTableColumn
mIfLwApInfoApAddress = _MIfLwApInfoApAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 10),
    _MIfLwApInfoApAddress_Type()
)
mIfLwApInfoApAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwApInfoApAddress.setStatus("current")
_MIfLwApInfoIpAddress_Type = InetIpAddress
_MIfLwApInfoIpAddress_Object = MibTableColumn
mIfLwApInfoIpAddress = _MIfLwApInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 11),
    _MIfLwApInfoIpAddress_Type()
)
mIfLwApInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwApInfoIpAddress.setStatus("current")
_MIfLwApInfoConnectedTime_Type = Integer32
_MIfLwApInfoConnectedTime_Object = MibTableColumn
mIfLwApInfoConnectedTime = _MIfLwApInfoConnectedTime_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 12),
    _MIfLwApInfoConnectedTime_Type()
)
mIfLwApInfoConnectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwApInfoConnectedTime.setStatus("current")
_MIfLwApInfoRssi_Type = Integer32
_MIfLwApInfoRssi_Object = MibTableColumn
mIfLwApInfoRssi = _MIfLwApInfoRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 13),
    _MIfLwApInfoRssi_Type()
)
mIfLwApInfoRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwApInfoRssi.setStatus("current")
_MIfLwApInfoSnr_Type = Unsigned32
_MIfLwApInfoSnr_Object = MibTableColumn
mIfLwApInfoSnr = _MIfLwApInfoSnr_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 14),
    _MIfLwApInfoSnr_Type()
)
mIfLwApInfoSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwApInfoSnr.setStatus("current")
_MIfLwApInfoMod_Type = ModulationModeType
_MIfLwApInfoMod_Object = MibTableColumn
mIfLwApInfoMod = _MIfLwApInfoMod_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 15),
    _MIfLwApInfoMod_Type()
)
mIfLwApInfoMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwApInfoMod.setStatus("current")
_MIfLwMacStatsTxSuccess_Type = Unsigned32
_MIfLwMacStatsTxSuccess_Object = MibTableColumn
mIfLwMacStatsTxSuccess = _MIfLwMacStatsTxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 16),
    _MIfLwMacStatsTxSuccess_Type()
)
mIfLwMacStatsTxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwMacStatsTxSuccess.setStatus("current")
_MIfLwMacStatsTxQueueFull_Type = Unsigned32
_MIfLwMacStatsTxQueueFull_Object = MibTableColumn
mIfLwMacStatsTxQueueFull = _MIfLwMacStatsTxQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 17),
    _MIfLwMacStatsTxQueueFull_Type()
)
mIfLwMacStatsTxQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwMacStatsTxQueueFull.setStatus("current")
_MIfLwMacStatsTxError_Type = Unsigned32
_MIfLwMacStatsTxError_Object = MibTableColumn
mIfLwMacStatsTxError = _MIfLwMacStatsTxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 18),
    _MIfLwMacStatsTxError_Type()
)
mIfLwMacStatsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwMacStatsTxError.setStatus("current")
_MIfLwMacStatsTxRetry_Type = Unsigned32
_MIfLwMacStatsTxRetry_Object = MibTableColumn
mIfLwMacStatsTxRetry = _MIfLwMacStatsTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 19),
    _MIfLwMacStatsTxRetry_Type()
)
mIfLwMacStatsTxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwMacStatsTxRetry.setStatus("current")
_MIfLwMacStatsRxSuccess_Type = Unsigned32
_MIfLwMacStatsRxSuccess_Object = MibTableColumn
mIfLwMacStatsRxSuccess = _MIfLwMacStatsRxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 20),
    _MIfLwMacStatsRxSuccess_Type()
)
mIfLwMacStatsRxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwMacStatsRxSuccess.setStatus("current")
_MIfLwMacStatsRxError_Type = Unsigned32
_MIfLwMacStatsRxError_Object = MibTableColumn
mIfLwMacStatsRxError = _MIfLwMacStatsRxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 21),
    _MIfLwMacStatsRxError_Type()
)
mIfLwMacStatsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwMacStatsRxError.setStatus("current")
_MIfLwModemStatsTxSuccess_Type = Unsigned32
_MIfLwModemStatsTxSuccess_Object = MibTableColumn
mIfLwModemStatsTxSuccess = _MIfLwModemStatsTxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 22),
    _MIfLwModemStatsTxSuccess_Type()
)
mIfLwModemStatsTxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwModemStatsTxSuccess.setStatus("current")
_MIfLwModemStatsTxError_Type = Unsigned32
_MIfLwModemStatsTxError_Object = MibTableColumn
mIfLwModemStatsTxError = _MIfLwModemStatsTxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 23),
    _MIfLwModemStatsTxError_Type()
)
mIfLwModemStatsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwModemStatsTxError.setStatus("current")
_MIfLwModemStatsRxSuccess_Type = Unsigned32
_MIfLwModemStatsRxSuccess_Object = MibTableColumn
mIfLwModemStatsRxSuccess = _MIfLwModemStatsRxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 24),
    _MIfLwModemStatsRxSuccess_Type()
)
mIfLwModemStatsRxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwModemStatsRxSuccess.setStatus("current")
_MIfLwModemStatsRxError_Type = Unsigned32
_MIfLwModemStatsRxError_Object = MibTableColumn
mIfLwModemStatsRxError = _MIfLwModemStatsRxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 25),
    _MIfLwModemStatsRxError_Type()
)
mIfLwModemStatsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwModemStatsRxError.setStatus("current")
_MIfLwLastRssi_Type = Integer32
_MIfLwLastRssi_Object = MibTableColumn
mIfLwLastRssi = _MIfLwLastRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 26),
    _MIfLwLastRssi_Type()
)
mIfLwLastRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwLastRssi.setStatus("current")
_MIfLwLastSnr_Type = Unsigned32
_MIfLwLastSnr_Object = MibTableColumn
mIfLwLastSnr = _MIfLwLastSnr_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 27),
    _MIfLwLastSnr_Type()
)
mIfLwLastSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwLastSnr.setStatus("current")
_MIfLwLastMod_Type = ModulationModeType
_MIfLwLastMod_Object = MibTableColumn
mIfLwLastMod = _MIfLwLastMod_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 28),
    _MIfLwLastMod_Type()
)
mIfLwLastMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwLastMod.setStatus("current")
_MIfLwLastRate_Type = RateType
_MIfLwLastRate_Object = MibTableColumn
mIfLwLastRate = _MIfLwLastRate_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 29),
    _MIfLwLastRate_Type()
)
mIfLwLastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwLastRate.setStatus("current")
_MIfLwActiveNic_Type = TruthValue
_MIfLwActiveNic_Object = MibTableColumn
mIfLwActiveNic = _MIfLwActiveNic_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 30),
    _MIfLwActiveNic_Type()
)
mIfLwActiveNic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwActiveNic.setStatus("current")
_MIfLwStatusConnRemTable_Object = MibTable
mIfLwStatusConnRemTable = _MIfLwStatusConnRemTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mIfLwStatusConnRemTable.setStatus("current")
_MIfLwStatusConnRemEntry_Object = MibTableRow
mIfLwStatusConnRemEntry = _MIfLwStatusConnRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1)
)
mIfLwStatusConnRemEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MDS-IF-LW-MIB", "mIfLwStatusConnRemAddress"),
)
if mibBuilder.loadTexts:
    mIfLwStatusConnRemEntry.setStatus("current")
_MIfLwStatusConnRemAddress_Type = MacAddress
_MIfLwStatusConnRemAddress_Object = MibTableColumn
mIfLwStatusConnRemAddress = _MIfLwStatusConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 1),
    _MIfLwStatusConnRemAddress_Type()
)
mIfLwStatusConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemAddress.setStatus("current")
_MIfLwStatusConnRemIpAddress_Type = InetIpAddress
_MIfLwStatusConnRemIpAddress_Object = MibTableColumn
mIfLwStatusConnRemIpAddress = _MIfLwStatusConnRemIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 2),
    _MIfLwStatusConnRemIpAddress_Type()
)
mIfLwStatusConnRemIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemIpAddress.setStatus("current")
_MIfLwStatusConnRemTimeToLive_Type = Unsigned32
_MIfLwStatusConnRemTimeToLive_Object = MibTableColumn
mIfLwStatusConnRemTimeToLive = _MIfLwStatusConnRemTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 3),
    _MIfLwStatusConnRemTimeToLive_Type()
)
mIfLwStatusConnRemTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemTimeToLive.setStatus("current")
_MIfLwStatusConnRemLinkStatus_Type = LinkStatus
_MIfLwStatusConnRemLinkStatus_Object = MibTableColumn
mIfLwStatusConnRemLinkStatus = _MIfLwStatusConnRemLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 4),
    _MIfLwStatusConnRemLinkStatus_Type()
)
mIfLwStatusConnRemLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemLinkStatus.setStatus("current")
_MIfLwStatusConnRemNicId_Type = UnsignedShort
_MIfLwStatusConnRemNicId_Object = MibTableColumn
mIfLwStatusConnRemNicId = _MIfLwStatusConnRemNicId_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 5),
    _MIfLwStatusConnRemNicId_Type()
)
mIfLwStatusConnRemNicId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemNicId.setStatus("current")
_MIfLwStatusConnRemRssi_Type = Integer32
_MIfLwStatusConnRemRssi_Object = MibTableColumn
mIfLwStatusConnRemRssi = _MIfLwStatusConnRemRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 6),
    _MIfLwStatusConnRemRssi_Type()
)
mIfLwStatusConnRemRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemRssi.setStatus("current")
_MIfLwStatusConnRemSnr_Type = Unsigned32
_MIfLwStatusConnRemSnr_Object = MibTableColumn
mIfLwStatusConnRemSnr = _MIfLwStatusConnRemSnr_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 7),
    _MIfLwStatusConnRemSnr_Type()
)
mIfLwStatusConnRemSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemSnr.setStatus("current")
_MIfLwStatusConnRemMod_Type = ModulationModeType
_MIfLwStatusConnRemMod_Object = MibTableColumn
mIfLwStatusConnRemMod = _MIfLwStatusConnRemMod_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 8),
    _MIfLwStatusConnRemMod_Type()
)
mIfLwStatusConnRemMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemMod.setStatus("current")
_MIfLwStatusConnRemStatsTxPackets_Type = Unsigned32
_MIfLwStatusConnRemStatsTxPackets_Object = MibTableColumn
mIfLwStatusConnRemStatsTxPackets = _MIfLwStatusConnRemStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 9),
    _MIfLwStatusConnRemStatsTxPackets_Type()
)
mIfLwStatusConnRemStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsTxPackets.setStatus("current")
_MIfLwStatusConnRemStatsTxBytes_Type = Unsigned32
_MIfLwStatusConnRemStatsTxBytes_Object = MibTableColumn
mIfLwStatusConnRemStatsTxBytes = _MIfLwStatusConnRemStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 10),
    _MIfLwStatusConnRemStatsTxBytes_Type()
)
mIfLwStatusConnRemStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsTxBytes.setStatus("current")
_MIfLwStatusConnRemStatsRxPackets_Type = Unsigned32
_MIfLwStatusConnRemStatsRxPackets_Object = MibTableColumn
mIfLwStatusConnRemStatsRxPackets = _MIfLwStatusConnRemStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 11),
    _MIfLwStatusConnRemStatsRxPackets_Type()
)
mIfLwStatusConnRemStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsRxPackets.setStatus("current")
_MIfLwStatusConnRemStatsRxBytes_Type = Unsigned32
_MIfLwStatusConnRemStatsRxBytes_Object = MibTableColumn
mIfLwStatusConnRemStatsRxBytes = _MIfLwStatusConnRemStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 12),
    _MIfLwStatusConnRemStatsRxBytes_Type()
)
mIfLwStatusConnRemStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsRxBytes.setStatus("current")
_MIfLwStatusConnRemStatsTxError_Type = Unsigned32
_MIfLwStatusConnRemStatsTxError_Object = MibTableColumn
mIfLwStatusConnRemStatsTxError = _MIfLwStatusConnRemStatsTxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 13),
    _MIfLwStatusConnRemStatsTxError_Type()
)
mIfLwStatusConnRemStatsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsTxError.setStatus("current")
_MIfLwStatusConnRemStatsRxError_Type = Unsigned32
_MIfLwStatusConnRemStatsRxError_Object = MibTableColumn
mIfLwStatusConnRemStatsRxError = _MIfLwStatusConnRemStatsRxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 14),
    _MIfLwStatusConnRemStatsRxError_Type()
)
mIfLwStatusConnRemStatsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsRxError.setStatus("current")
_MIfLwStatusConnRemStatsTxDrop_Type = Unsigned32
_MIfLwStatusConnRemStatsTxDrop_Object = MibTableColumn
mIfLwStatusConnRemStatsTxDrop = _MIfLwStatusConnRemStatsTxDrop_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 15),
    _MIfLwStatusConnRemStatsTxDrop_Type()
)
mIfLwStatusConnRemStatsTxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsTxDrop.setStatus("current")
_MIfLwStatusConnRemStatsRxDrop_Type = Unsigned32
_MIfLwStatusConnRemStatsRxDrop_Object = MibTableColumn
mIfLwStatusConnRemStatsRxDrop = _MIfLwStatusConnRemStatsRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 16),
    _MIfLwStatusConnRemStatsRxDrop_Type()
)
mIfLwStatusConnRemStatsRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsRxDrop.setStatus("current")
_MIfLwStatusConnRemStatsGateway_Type = MacAddress
_MIfLwStatusConnRemStatsGateway_Object = MibTableColumn
mIfLwStatusConnRemStatsGateway = _MIfLwStatusConnRemStatsGateway_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 17),
    _MIfLwStatusConnRemStatsGateway_Type()
)
mIfLwStatusConnRemStatsGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsGateway.setStatus("current")
_MIfLwStatusConnRemStatsAllIp_Type = OctetString
_MIfLwStatusConnRemStatsAllIp_Object = MibTableColumn
mIfLwStatusConnRemStatsAllIp = _MIfLwStatusConnRemStatsAllIp_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 18),
    _MIfLwStatusConnRemStatsAllIp_Type()
)
mIfLwStatusConnRemStatsAllIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsAllIp.setStatus("current")
_MIfLwStatusConnRemStatsName_Type = OctetString
_MIfLwStatusConnRemStatsName_Object = MibTableColumn
mIfLwStatusConnRemStatsName = _MIfLwStatusConnRemStatsName_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 19),
    _MIfLwStatusConnRemStatsName_Type()
)
mIfLwStatusConnRemStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsName.setStatus("current")
_MIfLwStatusConnRemStatsAlarmed_Type = TruthValue
_MIfLwStatusConnRemStatsAlarmed_Object = MibTableColumn
mIfLwStatusConnRemStatsAlarmed = _MIfLwStatusConnRemStatsAlarmed_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 20),
    _MIfLwStatusConnRemStatsAlarmed_Type()
)
mIfLwStatusConnRemStatsAlarmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsAlarmed.setStatus("current")
_MIfLwStatusConnRemStatsVersion_Type = OctetString
_MIfLwStatusConnRemStatsVersion_Object = MibTableColumn
mIfLwStatusConnRemStatsVersion = _MIfLwStatusConnRemStatsVersion_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 21),
    _MIfLwStatusConnRemStatsVersion_Type()
)
mIfLwStatusConnRemStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsVersion.setStatus("current")


class _MIfLwStatusConnRemStatsTemp_Type(Integer32):
    """Custom type mIfLwStatusConnRemStatsTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MIfLwStatusConnRemStatsTemp_Type.__name__ = "Integer32"
_MIfLwStatusConnRemStatsTemp_Object = MibTableColumn
mIfLwStatusConnRemStatsTemp = _MIfLwStatusConnRemStatsTemp_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 22),
    _MIfLwStatusConnRemStatsTemp_Type()
)
mIfLwStatusConnRemStatsTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsTemp.setStatus("current")
_MIfLwStatusConnRemStatsDwnRssi_Type = Integer32
_MIfLwStatusConnRemStatsDwnRssi_Object = MibTableColumn
mIfLwStatusConnRemStatsDwnRssi = _MIfLwStatusConnRemStatsDwnRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 23),
    _MIfLwStatusConnRemStatsDwnRssi_Type()
)
mIfLwStatusConnRemStatsDwnRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsDwnRssi.setStatus("current")
_MIfLwStatusConnRemStatsDwnSnr_Type = Unsigned32
_MIfLwStatusConnRemStatsDwnSnr_Object = MibTableColumn
mIfLwStatusConnRemStatsDwnSnr = _MIfLwStatusConnRemStatsDwnSnr_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 24),
    _MIfLwStatusConnRemStatsDwnSnr_Type()
)
mIfLwStatusConnRemStatsDwnSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsDwnSnr.setStatus("current")
_MIfLwStatusConnRemStatsDwnMod_Type = ModulationModeType
_MIfLwStatusConnRemStatsDwnMod_Object = MibTableColumn
mIfLwStatusConnRemStatsDwnMod = _MIfLwStatusConnRemStatsDwnMod_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 25),
    _MIfLwStatusConnRemStatsDwnMod_Type()
)
mIfLwStatusConnRemStatsDwnMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusConnRemStatsDwnMod.setStatus("current")
_MIfLwStatusEndpointTable_Object = MibTable
mIfLwStatusEndpointTable = _MIfLwStatusEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mIfLwStatusEndpointTable.setStatus("current")
_MIfLwStatusEndpointEntry_Object = MibTableRow
mIfLwStatusEndpointEntry = _MIfLwStatusEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1)
)
mIfLwStatusEndpointEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MDS-IF-LW-MIB", "mIfLwStatusEndpointAddress"),
)
if mibBuilder.loadTexts:
    mIfLwStatusEndpointEntry.setStatus("current")
_MIfLwStatusEndpointAddress_Type = MacAddress
_MIfLwStatusEndpointAddress_Object = MibTableColumn
mIfLwStatusEndpointAddress = _MIfLwStatusEndpointAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 1),
    _MIfLwStatusEndpointAddress_Type()
)
mIfLwStatusEndpointAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusEndpointAddress.setStatus("current")
_MIfLwStatusEndpointIpAddress_Type = InetIpAddress
_MIfLwStatusEndpointIpAddress_Object = MibTableColumn
mIfLwStatusEndpointIpAddress = _MIfLwStatusEndpointIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 2),
    _MIfLwStatusEndpointIpAddress_Type()
)
mIfLwStatusEndpointIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusEndpointIpAddress.setStatus("current")
_MIfLwStatusEndpointTimeToLive_Type = Unsigned32
_MIfLwStatusEndpointTimeToLive_Object = MibTableColumn
mIfLwStatusEndpointTimeToLive = _MIfLwStatusEndpointTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 3),
    _MIfLwStatusEndpointTimeToLive_Type()
)
mIfLwStatusEndpointTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusEndpointTimeToLive.setStatus("current")
_MIfLwStatusEndpointRemAddress_Type = MacAddress
_MIfLwStatusEndpointRemAddress_Object = MibTableColumn
mIfLwStatusEndpointRemAddress = _MIfLwStatusEndpointRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 4),
    _MIfLwStatusEndpointRemAddress_Type()
)
mIfLwStatusEndpointRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusEndpointRemAddress.setStatus("current")
_MIfLwStatusEndpointStatsTxPackets_Type = Unsigned32
_MIfLwStatusEndpointStatsTxPackets_Object = MibTableColumn
mIfLwStatusEndpointStatsTxPackets = _MIfLwStatusEndpointStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 5),
    _MIfLwStatusEndpointStatsTxPackets_Type()
)
mIfLwStatusEndpointStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusEndpointStatsTxPackets.setStatus("current")
_MIfLwStatusEndpointStatsTxBytes_Type = Unsigned32
_MIfLwStatusEndpointStatsTxBytes_Object = MibTableColumn
mIfLwStatusEndpointStatsTxBytes = _MIfLwStatusEndpointStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 6),
    _MIfLwStatusEndpointStatsTxBytes_Type()
)
mIfLwStatusEndpointStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusEndpointStatsTxBytes.setStatus("current")
_MIfLwStatusEndpointStatsRxPackets_Type = Unsigned32
_MIfLwStatusEndpointStatsRxPackets_Object = MibTableColumn
mIfLwStatusEndpointStatsRxPackets = _MIfLwStatusEndpointStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 7),
    _MIfLwStatusEndpointStatsRxPackets_Type()
)
mIfLwStatusEndpointStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusEndpointStatsRxPackets.setStatus("current")
_MIfLwStatusEndpointStatsRxBytes_Type = Unsigned32
_MIfLwStatusEndpointStatsRxBytes_Object = MibTableColumn
mIfLwStatusEndpointStatsRxBytes = _MIfLwStatusEndpointStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 8),
    _MIfLwStatusEndpointStatsRxBytes_Type()
)
mIfLwStatusEndpointStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusEndpointStatsRxBytes.setStatus("current")
_MIfLwStatusEndpointStatsTxError_Type = Unsigned32
_MIfLwStatusEndpointStatsTxError_Object = MibTableColumn
mIfLwStatusEndpointStatsTxError = _MIfLwStatusEndpointStatsTxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 9),
    _MIfLwStatusEndpointStatsTxError_Type()
)
mIfLwStatusEndpointStatsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusEndpointStatsTxError.setStatus("current")
_MIfLwStatusEndpointStatsRxError_Type = Unsigned32
_MIfLwStatusEndpointStatsRxError_Object = MibTableColumn
mIfLwStatusEndpointStatsRxError = _MIfLwStatusEndpointStatsRxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 10),
    _MIfLwStatusEndpointStatsRxError_Type()
)
mIfLwStatusEndpointStatsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusEndpointStatsRxError.setStatus("current")
_MIfLwStatusEndpointStatsTxDrop_Type = Unsigned32
_MIfLwStatusEndpointStatsTxDrop_Object = MibTableColumn
mIfLwStatusEndpointStatsTxDrop = _MIfLwStatusEndpointStatsTxDrop_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 11),
    _MIfLwStatusEndpointStatsTxDrop_Type()
)
mIfLwStatusEndpointStatsTxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusEndpointStatsTxDrop.setStatus("current")
_MIfLwStatusEndpointStatsRxDrop_Type = Unsigned32
_MIfLwStatusEndpointStatsRxDrop_Object = MibTableColumn
mIfLwStatusEndpointStatsRxDrop = _MIfLwStatusEndpointStatsRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 12),
    _MIfLwStatusEndpointStatsRxDrop_Type()
)
mIfLwStatusEndpointStatsRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfLwStatusEndpointStatsRxDrop.setStatus("current")
_MdsIfLwMIBConformance_ObjectIdentity = ObjectIdentity
mdsIfLwMIBConformance = _MdsIfLwMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3)
)
_MdsIfLwMIBCompliances_ObjectIdentity = ObjectIdentity
mdsIfLwMIBCompliances = _MdsIfLwMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 1)
)
_MdsIfLwMIBGroups_ObjectIdentity = ObjectIdentity
mdsIfLwMIBGroups = _MdsIfLwMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 2)
)

# Managed Objects groups

mIfLwStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 2, 1)
)
mIfLwStatusGroup.setObjects(
      *(("MDS-IF-LW-MIB", "mIfLwLinkStatus"),
        ("MDS-IF-LW-MIB", "mIfLwInitStatus"),
        ("MDS-IF-LW-MIB", "mIfLwCurrentDeviceMode"),
        ("MDS-IF-LW-MIB", "mIfLwAlarms"),
        ("MDS-IF-LW-MIB", "mIfLwSerialNumber"),
        ("MDS-IF-LW-MIB", "mIfLwFirmwareRevision"),
        ("MDS-IF-LW-MIB", "mIfLwHardwareId"),
        ("MDS-IF-LW-MIB", "mIfLwHardwareRevision"),
        ("MDS-IF-LW-MIB", "mIfLwTemperature"),
        ("MDS-IF-LW-MIB", "mIfLwApInfoApAddress"),
        ("MDS-IF-LW-MIB", "mIfLwApInfoIpAddress"),
        ("MDS-IF-LW-MIB", "mIfLwApInfoConnectedTime"),
        ("MDS-IF-LW-MIB", "mIfLwApInfoRssi"),
        ("MDS-IF-LW-MIB", "mIfLwApInfoSnr"),
        ("MDS-IF-LW-MIB", "mIfLwApInfoMod"),
        ("MDS-IF-LW-MIB", "mIfLwMacStatsTxSuccess"),
        ("MDS-IF-LW-MIB", "mIfLwMacStatsTxQueueFull"),
        ("MDS-IF-LW-MIB", "mIfLwMacStatsTxError"),
        ("MDS-IF-LW-MIB", "mIfLwMacStatsTxRetry"),
        ("MDS-IF-LW-MIB", "mIfLwMacStatsRxSuccess"),
        ("MDS-IF-LW-MIB", "mIfLwMacStatsRxError"),
        ("MDS-IF-LW-MIB", "mIfLwModemStatsTxSuccess"),
        ("MDS-IF-LW-MIB", "mIfLwModemStatsTxError"),
        ("MDS-IF-LW-MIB", "mIfLwModemStatsRxSuccess"),
        ("MDS-IF-LW-MIB", "mIfLwModemStatsRxError"),
        ("MDS-IF-LW-MIB", "mIfLwLastRssi"),
        ("MDS-IF-LW-MIB", "mIfLwLastSnr"),
        ("MDS-IF-LW-MIB", "mIfLwLastMod"),
        ("MDS-IF-LW-MIB", "mIfLwLastRate"),
        ("MDS-IF-LW-MIB", "mIfLwActiveNic"))
)
if mibBuilder.loadTexts:
    mIfLwStatusGroup.setStatus("current")

mIfLwStatusConnRemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 2, 2)
)
mIfLwStatusConnRemGroup.setObjects(
      *(("MDS-IF-LW-MIB", "mIfLwStatusConnRemAddress"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemIpAddress"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemTimeToLive"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemLinkStatus"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemNicId"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemRssi"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemSnr"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemMod"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTxPackets"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTxBytes"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsRxPackets"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsRxBytes"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTxError"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsRxError"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTxDrop"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsRxDrop"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsGateway"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsAllIp"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsName"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsAlarmed"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsVersion"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTemp"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsDwnRssi"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsDwnSnr"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsDwnMod"))
)
if mibBuilder.loadTexts:
    mIfLwStatusConnRemGroup.setStatus("current")

mIfLwStatusEndpointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 2, 3)
)
mIfLwStatusEndpointGroup.setObjects(
      *(("MDS-IF-LW-MIB", "mIfLwStatusEndpointAddress"),
        ("MDS-IF-LW-MIB", "mIfLwStatusEndpointIpAddress"),
        ("MDS-IF-LW-MIB", "mIfLwStatusEndpointTimeToLive"),
        ("MDS-IF-LW-MIB", "mIfLwStatusEndpointRemAddress"),
        ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsTxPackets"),
        ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsTxBytes"),
        ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsRxPackets"),
        ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsRxBytes"),
        ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsTxError"),
        ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsRxError"),
        ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsTxDrop"),
        ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsRxDrop"))
)
if mibBuilder.loadTexts:
    mIfLwStatusEndpointGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mIfLwCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 1, 1)
)
mIfLwCompliance.setObjects(
      *(("MDS-IF-LW-MIB", "mIfLwStatusGroup"),
        ("MDS-IF-LW-MIB", "mIfLwStatusConnRemGroup"),
        ("MDS-IF-LW-MIB", "mIfLwStatusEndpointGroup"))
)
if mibBuilder.loadTexts:
    mIfLwCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MDS-IF-LW-MIB",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "LinkStatus": LinkStatus,
       "InitStatus": InitStatus,
       "DeviceModeType": DeviceModeType,
       "ModulationModeType": ModulationModeType,
       "AlarmFlags": AlarmFlags,
       "FirmwareRevision": FirmwareRevision,
       "InetIpAddress": InetIpAddress,
       "FrequencyType": FrequencyType,
       "ChannelType": ChannelType,
       "FecType": FecType,
       "RateType": RateType,
       "mdsIfLwMIB": mdsIfLwMIB,
       "mIfLwMIBObjects": mIfLwMIBObjects,
       "mIfLwConfig": mIfLwConfig,
       "mIfLwStatus": mIfLwStatus,
       "mIfLwStatusTable": mIfLwStatusTable,
       "mIfLwStatusEntry": mIfLwStatusEntry,
       "mIfLwLinkStatus": mIfLwLinkStatus,
       "mIfLwInitStatus": mIfLwInitStatus,
       "mIfLwCurrentDeviceMode": mIfLwCurrentDeviceMode,
       "mIfLwAlarms": mIfLwAlarms,
       "mIfLwSerialNumber": mIfLwSerialNumber,
       "mIfLwFirmwareRevision": mIfLwFirmwareRevision,
       "mIfLwHardwareId": mIfLwHardwareId,
       "mIfLwHardwareRevision": mIfLwHardwareRevision,
       "mIfLwTemperature": mIfLwTemperature,
       "mIfLwApInfoApAddress": mIfLwApInfoApAddress,
       "mIfLwApInfoIpAddress": mIfLwApInfoIpAddress,
       "mIfLwApInfoConnectedTime": mIfLwApInfoConnectedTime,
       "mIfLwApInfoRssi": mIfLwApInfoRssi,
       "mIfLwApInfoSnr": mIfLwApInfoSnr,
       "mIfLwApInfoMod": mIfLwApInfoMod,
       "mIfLwMacStatsTxSuccess": mIfLwMacStatsTxSuccess,
       "mIfLwMacStatsTxQueueFull": mIfLwMacStatsTxQueueFull,
       "mIfLwMacStatsTxError": mIfLwMacStatsTxError,
       "mIfLwMacStatsTxRetry": mIfLwMacStatsTxRetry,
       "mIfLwMacStatsRxSuccess": mIfLwMacStatsRxSuccess,
       "mIfLwMacStatsRxError": mIfLwMacStatsRxError,
       "mIfLwModemStatsTxSuccess": mIfLwModemStatsTxSuccess,
       "mIfLwModemStatsTxError": mIfLwModemStatsTxError,
       "mIfLwModemStatsRxSuccess": mIfLwModemStatsRxSuccess,
       "mIfLwModemStatsRxError": mIfLwModemStatsRxError,
       "mIfLwLastRssi": mIfLwLastRssi,
       "mIfLwLastSnr": mIfLwLastSnr,
       "mIfLwLastMod": mIfLwLastMod,
       "mIfLwLastRate": mIfLwLastRate,
       "mIfLwActiveNic": mIfLwActiveNic,
       "mIfLwStatusConnRemTable": mIfLwStatusConnRemTable,
       "mIfLwStatusConnRemEntry": mIfLwStatusConnRemEntry,
       "mIfLwStatusConnRemAddress": mIfLwStatusConnRemAddress,
       "mIfLwStatusConnRemIpAddress": mIfLwStatusConnRemIpAddress,
       "mIfLwStatusConnRemTimeToLive": mIfLwStatusConnRemTimeToLive,
       "mIfLwStatusConnRemLinkStatus": mIfLwStatusConnRemLinkStatus,
       "mIfLwStatusConnRemNicId": mIfLwStatusConnRemNicId,
       "mIfLwStatusConnRemRssi": mIfLwStatusConnRemRssi,
       "mIfLwStatusConnRemSnr": mIfLwStatusConnRemSnr,
       "mIfLwStatusConnRemMod": mIfLwStatusConnRemMod,
       "mIfLwStatusConnRemStatsTxPackets": mIfLwStatusConnRemStatsTxPackets,
       "mIfLwStatusConnRemStatsTxBytes": mIfLwStatusConnRemStatsTxBytes,
       "mIfLwStatusConnRemStatsRxPackets": mIfLwStatusConnRemStatsRxPackets,
       "mIfLwStatusConnRemStatsRxBytes": mIfLwStatusConnRemStatsRxBytes,
       "mIfLwStatusConnRemStatsTxError": mIfLwStatusConnRemStatsTxError,
       "mIfLwStatusConnRemStatsRxError": mIfLwStatusConnRemStatsRxError,
       "mIfLwStatusConnRemStatsTxDrop": mIfLwStatusConnRemStatsTxDrop,
       "mIfLwStatusConnRemStatsRxDrop": mIfLwStatusConnRemStatsRxDrop,
       "mIfLwStatusConnRemStatsGateway": mIfLwStatusConnRemStatsGateway,
       "mIfLwStatusConnRemStatsAllIp": mIfLwStatusConnRemStatsAllIp,
       "mIfLwStatusConnRemStatsName": mIfLwStatusConnRemStatsName,
       "mIfLwStatusConnRemStatsAlarmed": mIfLwStatusConnRemStatsAlarmed,
       "mIfLwStatusConnRemStatsVersion": mIfLwStatusConnRemStatsVersion,
       "mIfLwStatusConnRemStatsTemp": mIfLwStatusConnRemStatsTemp,
       "mIfLwStatusConnRemStatsDwnRssi": mIfLwStatusConnRemStatsDwnRssi,
       "mIfLwStatusConnRemStatsDwnSnr": mIfLwStatusConnRemStatsDwnSnr,
       "mIfLwStatusConnRemStatsDwnMod": mIfLwStatusConnRemStatsDwnMod,
       "mIfLwStatusEndpointTable": mIfLwStatusEndpointTable,
       "mIfLwStatusEndpointEntry": mIfLwStatusEndpointEntry,
       "mIfLwStatusEndpointAddress": mIfLwStatusEndpointAddress,
       "mIfLwStatusEndpointIpAddress": mIfLwStatusEndpointIpAddress,
       "mIfLwStatusEndpointTimeToLive": mIfLwStatusEndpointTimeToLive,
       "mIfLwStatusEndpointRemAddress": mIfLwStatusEndpointRemAddress,
       "mIfLwStatusEndpointStatsTxPackets": mIfLwStatusEndpointStatsTxPackets,
       "mIfLwStatusEndpointStatsTxBytes": mIfLwStatusEndpointStatsTxBytes,
       "mIfLwStatusEndpointStatsRxPackets": mIfLwStatusEndpointStatsRxPackets,
       "mIfLwStatusEndpointStatsRxBytes": mIfLwStatusEndpointStatsRxBytes,
       "mIfLwStatusEndpointStatsTxError": mIfLwStatusEndpointStatsTxError,
       "mIfLwStatusEndpointStatsRxError": mIfLwStatusEndpointStatsRxError,
       "mIfLwStatusEndpointStatsTxDrop": mIfLwStatusEndpointStatsTxDrop,
       "mIfLwStatusEndpointStatsRxDrop": mIfLwStatusEndpointStatsRxDrop,
       "mdsIfLwMIBConformance": mdsIfLwMIBConformance,
       "mdsIfLwMIBCompliances": mdsIfLwMIBCompliances,
       "mIfLwCompliance": mIfLwCompliance,
       "mdsIfLwMIBGroups": mdsIfLwMIBGroups,
       "mIfLwStatusGroup": mIfLwStatusGroup,
       "mIfLwStatusConnRemGroup": mIfLwStatusConnRemGroup,
       "mIfLwStatusEndpointGroup": mIfLwStatusEndpointGroup}
)
