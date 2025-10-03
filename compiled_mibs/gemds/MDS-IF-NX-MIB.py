# SNMP MIB module (MDS-IF-NX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gemds\MDS-IF-NX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:31 2025
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

mdsIfNxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3)
)
if mibBuilder.loadTexts:
    mdsIfNxMIB.setRevisions(
        ("2018-05-16 00:00",
         "2016-09-21 00:00",
         "2015-08-21 00:00",
         "2015-06-12 00:00",
         "2015-03-27 00:00",
         "2014-10-20 00:00",
         "2014-05-13 00:00")
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



class ModemType(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("e125kbps", 0),
          ("e250kbps", 1),
          ("e500kbps", 2),
          ("e1000kbps", 3),
          ("e1000Wkbps", 4),
          ("e1250kbps", 5),
          ("auto", 10))
    )



class AlarmFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("temperature", 0),
          ("vswrFault", 16),
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



# MIB Managed Objects in the order of their OIDs

_MIfNxMIBObjects_ObjectIdentity = ObjectIdentity
mIfNxMIBObjects = _MIfNxMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1)
)
_MIfNxConfig_ObjectIdentity = ObjectIdentity
mIfNxConfig = _MIfNxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 1)
)
_MIfNxStatus_ObjectIdentity = ObjectIdentity
mIfNxStatus = _MIfNxStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2)
)
_MIfNxStatusTable_Object = MibTable
mIfNxStatusTable = _MIfNxStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mIfNxStatusTable.setStatus("current")
_MIfNxStatusEntry_Object = MibTableRow
mIfNxStatusEntry = _MIfNxStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1)
)
mIfNxStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mIfNxStatusEntry.setStatus("current")
_MIfNxLinkStatus_Type = LinkStatus
_MIfNxLinkStatus_Object = MibTableColumn
mIfNxLinkStatus = _MIfNxLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 1),
    _MIfNxLinkStatus_Type()
)
mIfNxLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxLinkStatus.setStatus("current")
_MIfNxInitStatus_Type = InitStatus
_MIfNxInitStatus_Object = MibTableColumn
mIfNxInitStatus = _MIfNxInitStatus_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 2),
    _MIfNxInitStatus_Type()
)
mIfNxInitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxInitStatus.setStatus("current")
_MIfNxCurrentModem_Type = ModemType
_MIfNxCurrentModem_Object = MibTableColumn
mIfNxCurrentModem = _MIfNxCurrentModem_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 3),
    _MIfNxCurrentModem_Type()
)
mIfNxCurrentModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxCurrentModem.setStatus("current")
_MIfNxAlarms_Type = AlarmFlags
_MIfNxAlarms_Object = MibTableColumn
mIfNxAlarms = _MIfNxAlarms_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 4),
    _MIfNxAlarms_Type()
)
mIfNxAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxAlarms.setStatus("current")
_MIfNxSerialNumber_Type = Unsigned32
_MIfNxSerialNumber_Object = MibTableColumn
mIfNxSerialNumber = _MIfNxSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 5),
    _MIfNxSerialNumber_Type()
)
mIfNxSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxSerialNumber.setStatus("current")
_MIfNxFirmwareRevision_Type = FirmwareRevision
_MIfNxFirmwareRevision_Object = MibTableColumn
mIfNxFirmwareRevision = _MIfNxFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 6),
    _MIfNxFirmwareRevision_Type()
)
mIfNxFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxFirmwareRevision.setStatus("current")
_MIfNxHardwareId_Type = UnsignedByte
_MIfNxHardwareId_Object = MibTableColumn
mIfNxHardwareId = _MIfNxHardwareId_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 7),
    _MIfNxHardwareId_Type()
)
mIfNxHardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxHardwareId.setStatus("current")
_MIfNxHardwareRevision_Type = UnsignedByte
_MIfNxHardwareRevision_Object = MibTableColumn
mIfNxHardwareRevision = _MIfNxHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 8),
    _MIfNxHardwareRevision_Type()
)
mIfNxHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxHardwareRevision.setStatus("current")
_MIfNxTemperature_Type = Integer32
_MIfNxTemperature_Object = MibTableColumn
mIfNxTemperature = _MIfNxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 9),
    _MIfNxTemperature_Type()
)
mIfNxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxTemperature.setStatus("current")
_MIfNxApInfoApAddress_Type = MacAddress
_MIfNxApInfoApAddress_Object = MibTableColumn
mIfNxApInfoApAddress = _MIfNxApInfoApAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 10),
    _MIfNxApInfoApAddress_Type()
)
mIfNxApInfoApAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxApInfoApAddress.setStatus("current")
_MIfNxApInfoIpAddress_Type = InetIpAddress
_MIfNxApInfoIpAddress_Object = MibTableColumn
mIfNxApInfoIpAddress = _MIfNxApInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 11),
    _MIfNxApInfoIpAddress_Type()
)
mIfNxApInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxApInfoIpAddress.setStatus("current")
_MIfNxApInfoConnectedTime_Type = Integer32
_MIfNxApInfoConnectedTime_Object = MibTableColumn
mIfNxApInfoConnectedTime = _MIfNxApInfoConnectedTime_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 12),
    _MIfNxApInfoConnectedTime_Type()
)
mIfNxApInfoConnectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxApInfoConnectedTime.setStatus("current")
_MIfNxApInfoAvgRssi_Type = Integer32
_MIfNxApInfoAvgRssi_Object = MibTableColumn
mIfNxApInfoAvgRssi = _MIfNxApInfoAvgRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 13),
    _MIfNxApInfoAvgRssi_Type()
)
mIfNxApInfoAvgRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxApInfoAvgRssi.setStatus("current")
_MIfNxApInfoAvgLqi_Type = Unsigned32
_MIfNxApInfoAvgLqi_Object = MibTableColumn
mIfNxApInfoAvgLqi = _MIfNxApInfoAvgLqi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 14),
    _MIfNxApInfoAvgLqi_Type()
)
mIfNxApInfoAvgLqi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxApInfoAvgLqi.setStatus("current")
_MIfNxMacStatsTxSuccess_Type = Unsigned32
_MIfNxMacStatsTxSuccess_Object = MibTableColumn
mIfNxMacStatsTxSuccess = _MIfNxMacStatsTxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 15),
    _MIfNxMacStatsTxSuccess_Type()
)
mIfNxMacStatsTxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxMacStatsTxSuccess.setStatus("current")
_MIfNxMacStatsTxFail_Type = Unsigned32
_MIfNxMacStatsTxFail_Object = MibTableColumn
mIfNxMacStatsTxFail = _MIfNxMacStatsTxFail_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 16),
    _MIfNxMacStatsTxFail_Type()
)
mIfNxMacStatsTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxMacStatsTxFail.setStatus("current")
_MIfNxMacStatsTxQueueFull_Type = Unsigned32
_MIfNxMacStatsTxQueueFull_Object = MibTableColumn
mIfNxMacStatsTxQueueFull = _MIfNxMacStatsTxQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 17),
    _MIfNxMacStatsTxQueueFull_Type()
)
mIfNxMacStatsTxQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxMacStatsTxQueueFull.setStatus("current")
_MIfNxMacStatsTxNoSync_Type = Unsigned32
_MIfNxMacStatsTxNoSync_Object = MibTableColumn
mIfNxMacStatsTxNoSync = _MIfNxMacStatsTxNoSync_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 18),
    _MIfNxMacStatsTxNoSync_Type()
)
mIfNxMacStatsTxNoSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxMacStatsTxNoSync.setStatus("current")
_MIfNxMacStatsTxNoAssoc_Type = Unsigned32
_MIfNxMacStatsTxNoAssoc_Object = MibTableColumn
mIfNxMacStatsTxNoAssoc = _MIfNxMacStatsTxNoAssoc_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 19),
    _MIfNxMacStatsTxNoAssoc_Type()
)
mIfNxMacStatsTxNoAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxMacStatsTxNoAssoc.setStatus("current")
_MIfNxMacStatsTxError_Type = Unsigned32
_MIfNxMacStatsTxError_Object = MibTableColumn
mIfNxMacStatsTxError = _MIfNxMacStatsTxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 20),
    _MIfNxMacStatsTxError_Type()
)
mIfNxMacStatsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxMacStatsTxError.setStatus("current")
_MIfNxMacStatsTxRetry_Type = Unsigned32
_MIfNxMacStatsTxRetry_Object = MibTableColumn
mIfNxMacStatsTxRetry = _MIfNxMacStatsTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 21),
    _MIfNxMacStatsTxRetry_Type()
)
mIfNxMacStatsTxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxMacStatsTxRetry.setStatus("current")
_MIfNxMacStatsRxSuccess_Type = Unsigned32
_MIfNxMacStatsRxSuccess_Object = MibTableColumn
mIfNxMacStatsRxSuccess = _MIfNxMacStatsRxSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 22),
    _MIfNxMacStatsRxSuccess_Type()
)
mIfNxMacStatsRxSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxMacStatsRxSuccess.setStatus("current")
_MIfNxMacStatsSyncCheckError_Type = Unsigned32
_MIfNxMacStatsSyncCheckError_Object = MibTableColumn
mIfNxMacStatsSyncCheckError = _MIfNxMacStatsSyncCheckError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 23),
    _MIfNxMacStatsSyncCheckError_Type()
)
mIfNxMacStatsSyncCheckError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxMacStatsSyncCheckError.setStatus("current")
_MIfNxMacStatsSyncChange_Type = Unsigned32
_MIfNxMacStatsSyncChange_Object = MibTableColumn
mIfNxMacStatsSyncChange = _MIfNxMacStatsSyncChange_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 24),
    _MIfNxMacStatsSyncChange_Type()
)
mIfNxMacStatsSyncChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxMacStatsSyncChange.setStatus("current")
_MIfNxCurrentDeviceMode_Type = DeviceModeType
_MIfNxCurrentDeviceMode_Object = MibTableColumn
mIfNxCurrentDeviceMode = _MIfNxCurrentDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 25),
    _MIfNxCurrentDeviceMode_Type()
)
mIfNxCurrentDeviceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxCurrentDeviceMode.setStatus("current")
_MIfNxLastRssi_Type = Integer32
_MIfNxLastRssi_Object = MibTableColumn
mIfNxLastRssi = _MIfNxLastRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 26),
    _MIfNxLastRssi_Type()
)
mIfNxLastRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxLastRssi.setStatus("current")
_MIfNxLastLqi_Type = Unsigned32
_MIfNxLastLqi_Object = MibTableColumn
mIfNxLastLqi = _MIfNxLastLqi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 27),
    _MIfNxLastLqi_Type()
)
mIfNxLastLqi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxLastLqi.setStatus("current")
_MIfNxLastChan_Type = Unsigned32
_MIfNxLastChan_Object = MibTableColumn
mIfNxLastChan = _MIfNxLastChan_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 28),
    _MIfNxLastChan_Type()
)
mIfNxLastChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxLastChan.setStatus("current")
_MIfNxActiveNic_Type = TruthValue
_MIfNxActiveNic_Object = MibTableColumn
mIfNxActiveNic = _MIfNxActiveNic_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 29),
    _MIfNxActiveNic_Type()
)
mIfNxActiveNic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxActiveNic.setStatus("current")
_MIfNxStatusConnRemTable_Object = MibTable
mIfNxStatusConnRemTable = _MIfNxStatusConnRemTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mIfNxStatusConnRemTable.setStatus("current")
_MIfNxStatusConnRemEntry_Object = MibTableRow
mIfNxStatusConnRemEntry = _MIfNxStatusConnRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1)
)
mIfNxStatusConnRemEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MDS-IF-NX-MIB", "mIfNxStatusConnRemAddress"),
)
if mibBuilder.loadTexts:
    mIfNxStatusConnRemEntry.setStatus("current")
_MIfNxStatusConnRemAddress_Type = MacAddress
_MIfNxStatusConnRemAddress_Object = MibTableColumn
mIfNxStatusConnRemAddress = _MIfNxStatusConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 1),
    _MIfNxStatusConnRemAddress_Type()
)
mIfNxStatusConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemAddress.setStatus("current")
_MIfNxStatusConnRemIpAddress_Type = InetIpAddress
_MIfNxStatusConnRemIpAddress_Object = MibTableColumn
mIfNxStatusConnRemIpAddress = _MIfNxStatusConnRemIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 2),
    _MIfNxStatusConnRemIpAddress_Type()
)
mIfNxStatusConnRemIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemIpAddress.setStatus("current")
_MIfNxStatusConnRemTimeToLive_Type = Unsigned32
_MIfNxStatusConnRemTimeToLive_Object = MibTableColumn
mIfNxStatusConnRemTimeToLive = _MIfNxStatusConnRemTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 3),
    _MIfNxStatusConnRemTimeToLive_Type()
)
mIfNxStatusConnRemTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemTimeToLive.setStatus("current")
_MIfNxStatusConnRemLinkStatus_Type = LinkStatus
_MIfNxStatusConnRemLinkStatus_Object = MibTableColumn
mIfNxStatusConnRemLinkStatus = _MIfNxStatusConnRemLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 4),
    _MIfNxStatusConnRemLinkStatus_Type()
)
mIfNxStatusConnRemLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemLinkStatus.setStatus("current")
_MIfNxStatusConnRemNicId_Type = UnsignedShort
_MIfNxStatusConnRemNicId_Object = MibTableColumn
mIfNxStatusConnRemNicId = _MIfNxStatusConnRemNicId_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 5),
    _MIfNxStatusConnRemNicId_Type()
)
mIfNxStatusConnRemNicId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemNicId.setStatus("current")
_MIfNxStatusConnRemAvgRssi_Type = Integer32
_MIfNxStatusConnRemAvgRssi_Object = MibTableColumn
mIfNxStatusConnRemAvgRssi = _MIfNxStatusConnRemAvgRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 6),
    _MIfNxStatusConnRemAvgRssi_Type()
)
mIfNxStatusConnRemAvgRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemAvgRssi.setStatus("current")
_MIfNxStatusConnRemAvgLqi_Type = Unsigned32
_MIfNxStatusConnRemAvgLqi_Object = MibTableColumn
mIfNxStatusConnRemAvgLqi = _MIfNxStatusConnRemAvgLqi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 7),
    _MIfNxStatusConnRemAvgLqi_Type()
)
mIfNxStatusConnRemAvgLqi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemAvgLqi.setStatus("current")
_MIfNxStatusConnRemStatsTxPackets_Type = Unsigned32
_MIfNxStatusConnRemStatsTxPackets_Object = MibTableColumn
mIfNxStatusConnRemStatsTxPackets = _MIfNxStatusConnRemStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 8),
    _MIfNxStatusConnRemStatsTxPackets_Type()
)
mIfNxStatusConnRemStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsTxPackets.setStatus("current")
_MIfNxStatusConnRemStatsTxBytes_Type = Unsigned32
_MIfNxStatusConnRemStatsTxBytes_Object = MibTableColumn
mIfNxStatusConnRemStatsTxBytes = _MIfNxStatusConnRemStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 9),
    _MIfNxStatusConnRemStatsTxBytes_Type()
)
mIfNxStatusConnRemStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsTxBytes.setStatus("current")
_MIfNxStatusConnRemStatsRxPackets_Type = Unsigned32
_MIfNxStatusConnRemStatsRxPackets_Object = MibTableColumn
mIfNxStatusConnRemStatsRxPackets = _MIfNxStatusConnRemStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 10),
    _MIfNxStatusConnRemStatsRxPackets_Type()
)
mIfNxStatusConnRemStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsRxPackets.setStatus("current")
_MIfNxStatusConnRemStatsRxBytes_Type = Unsigned32
_MIfNxStatusConnRemStatsRxBytes_Object = MibTableColumn
mIfNxStatusConnRemStatsRxBytes = _MIfNxStatusConnRemStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 11),
    _MIfNxStatusConnRemStatsRxBytes_Type()
)
mIfNxStatusConnRemStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsRxBytes.setStatus("current")
_MIfNxStatusConnRemStatsTxError_Type = Unsigned32
_MIfNxStatusConnRemStatsTxError_Object = MibTableColumn
mIfNxStatusConnRemStatsTxError = _MIfNxStatusConnRemStatsTxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 12),
    _MIfNxStatusConnRemStatsTxError_Type()
)
mIfNxStatusConnRemStatsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsTxError.setStatus("current")
_MIfNxStatusConnRemStatsRxError_Type = Unsigned32
_MIfNxStatusConnRemStatsRxError_Object = MibTableColumn
mIfNxStatusConnRemStatsRxError = _MIfNxStatusConnRemStatsRxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 13),
    _MIfNxStatusConnRemStatsRxError_Type()
)
mIfNxStatusConnRemStatsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsRxError.setStatus("current")
_MIfNxStatusConnRemStatsTxDrop_Type = Unsigned32
_MIfNxStatusConnRemStatsTxDrop_Object = MibTableColumn
mIfNxStatusConnRemStatsTxDrop = _MIfNxStatusConnRemStatsTxDrop_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 14),
    _MIfNxStatusConnRemStatsTxDrop_Type()
)
mIfNxStatusConnRemStatsTxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsTxDrop.setStatus("current")
_MIfNxStatusConnRemStatsRxDrop_Type = Unsigned32
_MIfNxStatusConnRemStatsRxDrop_Object = MibTableColumn
mIfNxStatusConnRemStatsRxDrop = _MIfNxStatusConnRemStatsRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 15),
    _MIfNxStatusConnRemStatsRxDrop_Type()
)
mIfNxStatusConnRemStatsRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsRxDrop.setStatus("current")
_MIfNxStatusConnRemAvgSnr_Type = Unsigned32
_MIfNxStatusConnRemAvgSnr_Object = MibTableColumn
mIfNxStatusConnRemAvgSnr = _MIfNxStatusConnRemAvgSnr_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 16),
    _MIfNxStatusConnRemAvgSnr_Type()
)
mIfNxStatusConnRemAvgSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemAvgSnr.setStatus("current")
_MIfNxStatusConnRemStatsGateway_Type = MacAddress
_MIfNxStatusConnRemStatsGateway_Object = MibTableColumn
mIfNxStatusConnRemStatsGateway = _MIfNxStatusConnRemStatsGateway_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 17),
    _MIfNxStatusConnRemStatsGateway_Type()
)
mIfNxStatusConnRemStatsGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsGateway.setStatus("current")
_MIfNxStatusConnRemStatsAllIp_Type = OctetString
_MIfNxStatusConnRemStatsAllIp_Object = MibTableColumn
mIfNxStatusConnRemStatsAllIp = _MIfNxStatusConnRemStatsAllIp_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 18),
    _MIfNxStatusConnRemStatsAllIp_Type()
)
mIfNxStatusConnRemStatsAllIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsAllIp.setStatus("current")
_MIfNxStatusConnRemStatsName_Type = OctetString
_MIfNxStatusConnRemStatsName_Object = MibTableColumn
mIfNxStatusConnRemStatsName = _MIfNxStatusConnRemStatsName_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 19),
    _MIfNxStatusConnRemStatsName_Type()
)
mIfNxStatusConnRemStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsName.setStatus("current")
_MIfNxStatusConnRemStatsAlarmed_Type = TruthValue
_MIfNxStatusConnRemStatsAlarmed_Object = MibTableColumn
mIfNxStatusConnRemStatsAlarmed = _MIfNxStatusConnRemStatsAlarmed_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 20),
    _MIfNxStatusConnRemStatsAlarmed_Type()
)
mIfNxStatusConnRemStatsAlarmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsAlarmed.setStatus("current")
_MIfNxStatusConnRemStatsVersion_Type = OctetString
_MIfNxStatusConnRemStatsVersion_Object = MibTableColumn
mIfNxStatusConnRemStatsVersion = _MIfNxStatusConnRemStatsVersion_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 21),
    _MIfNxStatusConnRemStatsVersion_Type()
)
mIfNxStatusConnRemStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsVersion.setStatus("current")


class _MIfNxStatusConnRemStatsTemp_Type(Integer32):
    """Custom type mIfNxStatusConnRemStatsTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MIfNxStatusConnRemStatsTemp_Type.__name__ = "Integer32"
_MIfNxStatusConnRemStatsTemp_Object = MibTableColumn
mIfNxStatusConnRemStatsTemp = _MIfNxStatusConnRemStatsTemp_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 22),
    _MIfNxStatusConnRemStatsTemp_Type()
)
mIfNxStatusConnRemStatsTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsTemp.setStatus("current")
_MIfNxStatusConnRemStatsDwnRssi_Type = Integer32
_MIfNxStatusConnRemStatsDwnRssi_Object = MibTableColumn
mIfNxStatusConnRemStatsDwnRssi = _MIfNxStatusConnRemStatsDwnRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 23),
    _MIfNxStatusConnRemStatsDwnRssi_Type()
)
mIfNxStatusConnRemStatsDwnRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsDwnRssi.setStatus("current")
_MIfNxStatusConnRemStatsDwnLqi_Type = Unsigned32
_MIfNxStatusConnRemStatsDwnLqi_Object = MibTableColumn
mIfNxStatusConnRemStatsDwnLqi = _MIfNxStatusConnRemStatsDwnLqi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 24),
    _MIfNxStatusConnRemStatsDwnLqi_Type()
)
mIfNxStatusConnRemStatsDwnLqi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsDwnLqi.setStatus("current")
_MIfNxStatusConnRemStatsDwnSnr_Type = Unsigned32
_MIfNxStatusConnRemStatsDwnSnr_Object = MibTableColumn
mIfNxStatusConnRemStatsDwnSnr = _MIfNxStatusConnRemStatsDwnSnr_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 25),
    _MIfNxStatusConnRemStatsDwnSnr_Type()
)
mIfNxStatusConnRemStatsDwnSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusConnRemStatsDwnSnr.setStatus("current")
_MIfNxStatusEndpointTable_Object = MibTable
mIfNxStatusEndpointTable = _MIfNxStatusEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mIfNxStatusEndpointTable.setStatus("current")
_MIfNxStatusEndpointEntry_Object = MibTableRow
mIfNxStatusEndpointEntry = _MIfNxStatusEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1)
)
mIfNxStatusEndpointEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MDS-IF-NX-MIB", "mIfNxStatusEndpointAddress"),
)
if mibBuilder.loadTexts:
    mIfNxStatusEndpointEntry.setStatus("current")
_MIfNxStatusEndpointAddress_Type = MacAddress
_MIfNxStatusEndpointAddress_Object = MibTableColumn
mIfNxStatusEndpointAddress = _MIfNxStatusEndpointAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 1),
    _MIfNxStatusEndpointAddress_Type()
)
mIfNxStatusEndpointAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusEndpointAddress.setStatus("current")
_MIfNxStatusEndpointIpAddress_Type = InetIpAddress
_MIfNxStatusEndpointIpAddress_Object = MibTableColumn
mIfNxStatusEndpointIpAddress = _MIfNxStatusEndpointIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 2),
    _MIfNxStatusEndpointIpAddress_Type()
)
mIfNxStatusEndpointIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusEndpointIpAddress.setStatus("current")
_MIfNxStatusEndpointTimeToLive_Type = Unsigned32
_MIfNxStatusEndpointTimeToLive_Object = MibTableColumn
mIfNxStatusEndpointTimeToLive = _MIfNxStatusEndpointTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 3),
    _MIfNxStatusEndpointTimeToLive_Type()
)
mIfNxStatusEndpointTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusEndpointTimeToLive.setStatus("current")
_MIfNxStatusEndpointRemAddress_Type = MacAddress
_MIfNxStatusEndpointRemAddress_Object = MibTableColumn
mIfNxStatusEndpointRemAddress = _MIfNxStatusEndpointRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 4),
    _MIfNxStatusEndpointRemAddress_Type()
)
mIfNxStatusEndpointRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusEndpointRemAddress.setStatus("current")
_MIfNxStatusEndpointStatsTxPackets_Type = Unsigned32
_MIfNxStatusEndpointStatsTxPackets_Object = MibTableColumn
mIfNxStatusEndpointStatsTxPackets = _MIfNxStatusEndpointStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 5),
    _MIfNxStatusEndpointStatsTxPackets_Type()
)
mIfNxStatusEndpointStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusEndpointStatsTxPackets.setStatus("current")
_MIfNxStatusEndpointStatsTxBytes_Type = Unsigned32
_MIfNxStatusEndpointStatsTxBytes_Object = MibTableColumn
mIfNxStatusEndpointStatsTxBytes = _MIfNxStatusEndpointStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 6),
    _MIfNxStatusEndpointStatsTxBytes_Type()
)
mIfNxStatusEndpointStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusEndpointStatsTxBytes.setStatus("current")
_MIfNxStatusEndpointStatsRxPackets_Type = Unsigned32
_MIfNxStatusEndpointStatsRxPackets_Object = MibTableColumn
mIfNxStatusEndpointStatsRxPackets = _MIfNxStatusEndpointStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 7),
    _MIfNxStatusEndpointStatsRxPackets_Type()
)
mIfNxStatusEndpointStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusEndpointStatsRxPackets.setStatus("current")
_MIfNxStatusEndpointStatsRxBytes_Type = Unsigned32
_MIfNxStatusEndpointStatsRxBytes_Object = MibTableColumn
mIfNxStatusEndpointStatsRxBytes = _MIfNxStatusEndpointStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 8),
    _MIfNxStatusEndpointStatsRxBytes_Type()
)
mIfNxStatusEndpointStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusEndpointStatsRxBytes.setStatus("current")
_MIfNxStatusEndpointStatsTxError_Type = Unsigned32
_MIfNxStatusEndpointStatsTxError_Object = MibTableColumn
mIfNxStatusEndpointStatsTxError = _MIfNxStatusEndpointStatsTxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 9),
    _MIfNxStatusEndpointStatsTxError_Type()
)
mIfNxStatusEndpointStatsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusEndpointStatsTxError.setStatus("current")
_MIfNxStatusEndpointStatsRxError_Type = Unsigned32
_MIfNxStatusEndpointStatsRxError_Object = MibTableColumn
mIfNxStatusEndpointStatsRxError = _MIfNxStatusEndpointStatsRxError_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 10),
    _MIfNxStatusEndpointStatsRxError_Type()
)
mIfNxStatusEndpointStatsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusEndpointStatsRxError.setStatus("current")
_MIfNxStatusEndpointStatsTxDrop_Type = Unsigned32
_MIfNxStatusEndpointStatsTxDrop_Object = MibTableColumn
mIfNxStatusEndpointStatsTxDrop = _MIfNxStatusEndpointStatsTxDrop_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 11),
    _MIfNxStatusEndpointStatsTxDrop_Type()
)
mIfNxStatusEndpointStatsTxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusEndpointStatsTxDrop.setStatus("current")
_MIfNxStatusEndpointStatsRxDrop_Type = Unsigned32
_MIfNxStatusEndpointStatsRxDrop_Object = MibTableColumn
mIfNxStatusEndpointStatsRxDrop = _MIfNxStatusEndpointStatsRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 12),
    _MIfNxStatusEndpointStatsRxDrop_Type()
)
mIfNxStatusEndpointStatsRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusEndpointStatsRxDrop.setStatus("current")
_MIfNxStatusActChanTable_Object = MibTable
mIfNxStatusActChanTable = _MIfNxStatusActChanTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    mIfNxStatusActChanTable.setStatus("current")
_MIfNxStatusActChanEntry_Object = MibTableRow
mIfNxStatusActChanEntry = _MIfNxStatusActChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1)
)
mIfNxStatusActChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MDS-IF-NX-MIB", "mIfNxStatusActChanChannel"),
)
if mibBuilder.loadTexts:
    mIfNxStatusActChanEntry.setStatus("current")
_MIfNxStatusActChanChannel_Type = UnsignedByte
_MIfNxStatusActChanChannel_Object = MibTableColumn
mIfNxStatusActChanChannel = _MIfNxStatusActChanChannel_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1, 1),
    _MIfNxStatusActChanChannel_Type()
)
mIfNxStatusActChanChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusActChanChannel.setStatus("current")
_MIfNxStatusActChanFrequency_Type = OctetString
_MIfNxStatusActChanFrequency_Object = MibTableColumn
mIfNxStatusActChanFrequency = _MIfNxStatusActChanFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1, 2),
    _MIfNxStatusActChanFrequency_Type()
)
mIfNxStatusActChanFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusActChanFrequency.setStatus("current")
_MIfNxStatusActChanAvgRssi_Type = Integer32
_MIfNxStatusActChanAvgRssi_Object = MibTableColumn
mIfNxStatusActChanAvgRssi = _MIfNxStatusActChanAvgRssi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1, 3),
    _MIfNxStatusActChanAvgRssi_Type()
)
mIfNxStatusActChanAvgRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusActChanAvgRssi.setStatus("current")
_MIfNxStatusActChanAvgLqi_Type = Unsigned32
_MIfNxStatusActChanAvgLqi_Object = MibTableColumn
mIfNxStatusActChanAvgLqi = _MIfNxStatusActChanAvgLqi_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1, 4),
    _MIfNxStatusActChanAvgLqi_Type()
)
mIfNxStatusActChanAvgLqi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mIfNxStatusActChanAvgLqi.setStatus("current")
_MdsIfNxMIBConformance_ObjectIdentity = ObjectIdentity
mdsIfNxMIBConformance = _MdsIfNxMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3)
)
_MdsIfNxMIBCompliances_ObjectIdentity = ObjectIdentity
mdsIfNxMIBCompliances = _MdsIfNxMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 1)
)
_MdsIfNxMIBGroups_ObjectIdentity = ObjectIdentity
mdsIfNxMIBGroups = _MdsIfNxMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2)
)

# Managed Objects groups

mIfNxStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2, 1)
)
mIfNxStatusGroup.setObjects(
      *(("MDS-IF-NX-MIB", "mIfNxLinkStatus"),
        ("MDS-IF-NX-MIB", "mIfNxInitStatus"),
        ("MDS-IF-NX-MIB", "mIfNxCurrentModem"),
        ("MDS-IF-NX-MIB", "mIfNxAlarms"),
        ("MDS-IF-NX-MIB", "mIfNxSerialNumber"),
        ("MDS-IF-NX-MIB", "mIfNxFirmwareRevision"),
        ("MDS-IF-NX-MIB", "mIfNxHardwareId"),
        ("MDS-IF-NX-MIB", "mIfNxHardwareRevision"),
        ("MDS-IF-NX-MIB", "mIfNxTemperature"),
        ("MDS-IF-NX-MIB", "mIfNxApInfoApAddress"),
        ("MDS-IF-NX-MIB", "mIfNxApInfoIpAddress"),
        ("MDS-IF-NX-MIB", "mIfNxApInfoConnectedTime"),
        ("MDS-IF-NX-MIB", "mIfNxApInfoAvgRssi"),
        ("MDS-IF-NX-MIB", "mIfNxApInfoAvgLqi"),
        ("MDS-IF-NX-MIB", "mIfNxMacStatsTxSuccess"),
        ("MDS-IF-NX-MIB", "mIfNxMacStatsTxFail"),
        ("MDS-IF-NX-MIB", "mIfNxMacStatsTxQueueFull"),
        ("MDS-IF-NX-MIB", "mIfNxMacStatsTxNoSync"),
        ("MDS-IF-NX-MIB", "mIfNxMacStatsTxNoAssoc"),
        ("MDS-IF-NX-MIB", "mIfNxMacStatsTxError"),
        ("MDS-IF-NX-MIB", "mIfNxMacStatsTxRetry"),
        ("MDS-IF-NX-MIB", "mIfNxMacStatsRxSuccess"),
        ("MDS-IF-NX-MIB", "mIfNxMacStatsSyncCheckError"),
        ("MDS-IF-NX-MIB", "mIfNxMacStatsSyncChange"),
        ("MDS-IF-NX-MIB", "mIfNxCurrentDeviceMode"),
        ("MDS-IF-NX-MIB", "mIfNxLastRssi"),
        ("MDS-IF-NX-MIB", "mIfNxLastLqi"),
        ("MDS-IF-NX-MIB", "mIfNxLastChan"),
        ("MDS-IF-NX-MIB", "mIfNxActiveNic"))
)
if mibBuilder.loadTexts:
    mIfNxStatusGroup.setStatus("current")

mIfNxStatusConnRemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2, 2)
)
mIfNxStatusConnRemGroup.setObjects(
      *(("MDS-IF-NX-MIB", "mIfNxStatusConnRemAddress"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemIpAddress"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemTimeToLive"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemLinkStatus"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemNicId"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemAvgRssi"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemAvgLqi"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTxPackets"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTxBytes"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsRxPackets"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsRxBytes"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTxError"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsRxError"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTxDrop"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsRxDrop"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemAvgSnr"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsGateway"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsAllIp"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsName"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsAlarmed"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsVersion"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTemp"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsDwnRssi"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsDwnLqi"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsDwnSnr"))
)
if mibBuilder.loadTexts:
    mIfNxStatusConnRemGroup.setStatus("current")

mIfNxStatusEndpointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2, 3)
)
mIfNxStatusEndpointGroup.setObjects(
      *(("MDS-IF-NX-MIB", "mIfNxStatusEndpointAddress"),
        ("MDS-IF-NX-MIB", "mIfNxStatusEndpointIpAddress"),
        ("MDS-IF-NX-MIB", "mIfNxStatusEndpointTimeToLive"),
        ("MDS-IF-NX-MIB", "mIfNxStatusEndpointRemAddress"),
        ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsTxPackets"),
        ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsTxBytes"),
        ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsRxPackets"),
        ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsRxBytes"),
        ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsTxError"),
        ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsRxError"),
        ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsTxDrop"),
        ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsRxDrop"))
)
if mibBuilder.loadTexts:
    mIfNxStatusEndpointGroup.setStatus("current")

mIfNxStatusActChanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2, 4)
)
mIfNxStatusActChanGroup.setObjects(
      *(("MDS-IF-NX-MIB", "mIfNxStatusActChanChannel"),
        ("MDS-IF-NX-MIB", "mIfNxStatusActChanFrequency"),
        ("MDS-IF-NX-MIB", "mIfNxStatusActChanAvgRssi"),
        ("MDS-IF-NX-MIB", "mIfNxStatusActChanAvgLqi"))
)
if mibBuilder.loadTexts:
    mIfNxStatusActChanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mIfNxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 1, 1)
)
mIfNxCompliance.setObjects(
      *(("MDS-IF-NX-MIB", "mIfNxStatusGroup"),
        ("MDS-IF-NX-MIB", "mIfNxStatusConnRemGroup"),
        ("MDS-IF-NX-MIB", "mIfNxStatusEndpointGroup"),
        ("MDS-IF-NX-MIB", "mIfNxStatusActChanGroup"))
)
if mibBuilder.loadTexts:
    mIfNxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MDS-IF-NX-MIB",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "LinkStatus": LinkStatus,
       "InitStatus": InitStatus,
       "DeviceModeType": DeviceModeType,
       "ModemType": ModemType,
       "AlarmFlags": AlarmFlags,
       "FirmwareRevision": FirmwareRevision,
       "InetIpAddress": InetIpAddress,
       "mdsIfNxMIB": mdsIfNxMIB,
       "mIfNxMIBObjects": mIfNxMIBObjects,
       "mIfNxConfig": mIfNxConfig,
       "mIfNxStatus": mIfNxStatus,
       "mIfNxStatusTable": mIfNxStatusTable,
       "mIfNxStatusEntry": mIfNxStatusEntry,
       "mIfNxLinkStatus": mIfNxLinkStatus,
       "mIfNxInitStatus": mIfNxInitStatus,
       "mIfNxCurrentModem": mIfNxCurrentModem,
       "mIfNxAlarms": mIfNxAlarms,
       "mIfNxSerialNumber": mIfNxSerialNumber,
       "mIfNxFirmwareRevision": mIfNxFirmwareRevision,
       "mIfNxHardwareId": mIfNxHardwareId,
       "mIfNxHardwareRevision": mIfNxHardwareRevision,
       "mIfNxTemperature": mIfNxTemperature,
       "mIfNxApInfoApAddress": mIfNxApInfoApAddress,
       "mIfNxApInfoIpAddress": mIfNxApInfoIpAddress,
       "mIfNxApInfoConnectedTime": mIfNxApInfoConnectedTime,
       "mIfNxApInfoAvgRssi": mIfNxApInfoAvgRssi,
       "mIfNxApInfoAvgLqi": mIfNxApInfoAvgLqi,
       "mIfNxMacStatsTxSuccess": mIfNxMacStatsTxSuccess,
       "mIfNxMacStatsTxFail": mIfNxMacStatsTxFail,
       "mIfNxMacStatsTxQueueFull": mIfNxMacStatsTxQueueFull,
       "mIfNxMacStatsTxNoSync": mIfNxMacStatsTxNoSync,
       "mIfNxMacStatsTxNoAssoc": mIfNxMacStatsTxNoAssoc,
       "mIfNxMacStatsTxError": mIfNxMacStatsTxError,
       "mIfNxMacStatsTxRetry": mIfNxMacStatsTxRetry,
       "mIfNxMacStatsRxSuccess": mIfNxMacStatsRxSuccess,
       "mIfNxMacStatsSyncCheckError": mIfNxMacStatsSyncCheckError,
       "mIfNxMacStatsSyncChange": mIfNxMacStatsSyncChange,
       "mIfNxCurrentDeviceMode": mIfNxCurrentDeviceMode,
       "mIfNxLastRssi": mIfNxLastRssi,
       "mIfNxLastLqi": mIfNxLastLqi,
       "mIfNxLastChan": mIfNxLastChan,
       "mIfNxActiveNic": mIfNxActiveNic,
       "mIfNxStatusConnRemTable": mIfNxStatusConnRemTable,
       "mIfNxStatusConnRemEntry": mIfNxStatusConnRemEntry,
       "mIfNxStatusConnRemAddress": mIfNxStatusConnRemAddress,
       "mIfNxStatusConnRemIpAddress": mIfNxStatusConnRemIpAddress,
       "mIfNxStatusConnRemTimeToLive": mIfNxStatusConnRemTimeToLive,
       "mIfNxStatusConnRemLinkStatus": mIfNxStatusConnRemLinkStatus,
       "mIfNxStatusConnRemNicId": mIfNxStatusConnRemNicId,
       "mIfNxStatusConnRemAvgRssi": mIfNxStatusConnRemAvgRssi,
       "mIfNxStatusConnRemAvgLqi": mIfNxStatusConnRemAvgLqi,
       "mIfNxStatusConnRemStatsTxPackets": mIfNxStatusConnRemStatsTxPackets,
       "mIfNxStatusConnRemStatsTxBytes": mIfNxStatusConnRemStatsTxBytes,
       "mIfNxStatusConnRemStatsRxPackets": mIfNxStatusConnRemStatsRxPackets,
       "mIfNxStatusConnRemStatsRxBytes": mIfNxStatusConnRemStatsRxBytes,
       "mIfNxStatusConnRemStatsTxError": mIfNxStatusConnRemStatsTxError,
       "mIfNxStatusConnRemStatsRxError": mIfNxStatusConnRemStatsRxError,
       "mIfNxStatusConnRemStatsTxDrop": mIfNxStatusConnRemStatsTxDrop,
       "mIfNxStatusConnRemStatsRxDrop": mIfNxStatusConnRemStatsRxDrop,
       "mIfNxStatusConnRemAvgSnr": mIfNxStatusConnRemAvgSnr,
       "mIfNxStatusConnRemStatsGateway": mIfNxStatusConnRemStatsGateway,
       "mIfNxStatusConnRemStatsAllIp": mIfNxStatusConnRemStatsAllIp,
       "mIfNxStatusConnRemStatsName": mIfNxStatusConnRemStatsName,
       "mIfNxStatusConnRemStatsAlarmed": mIfNxStatusConnRemStatsAlarmed,
       "mIfNxStatusConnRemStatsVersion": mIfNxStatusConnRemStatsVersion,
       "mIfNxStatusConnRemStatsTemp": mIfNxStatusConnRemStatsTemp,
       "mIfNxStatusConnRemStatsDwnRssi": mIfNxStatusConnRemStatsDwnRssi,
       "mIfNxStatusConnRemStatsDwnLqi": mIfNxStatusConnRemStatsDwnLqi,
       "mIfNxStatusConnRemStatsDwnSnr": mIfNxStatusConnRemStatsDwnSnr,
       "mIfNxStatusEndpointTable": mIfNxStatusEndpointTable,
       "mIfNxStatusEndpointEntry": mIfNxStatusEndpointEntry,
       "mIfNxStatusEndpointAddress": mIfNxStatusEndpointAddress,
       "mIfNxStatusEndpointIpAddress": mIfNxStatusEndpointIpAddress,
       "mIfNxStatusEndpointTimeToLive": mIfNxStatusEndpointTimeToLive,
       "mIfNxStatusEndpointRemAddress": mIfNxStatusEndpointRemAddress,
       "mIfNxStatusEndpointStatsTxPackets": mIfNxStatusEndpointStatsTxPackets,
       "mIfNxStatusEndpointStatsTxBytes": mIfNxStatusEndpointStatsTxBytes,
       "mIfNxStatusEndpointStatsRxPackets": mIfNxStatusEndpointStatsRxPackets,
       "mIfNxStatusEndpointStatsRxBytes": mIfNxStatusEndpointStatsRxBytes,
       "mIfNxStatusEndpointStatsTxError": mIfNxStatusEndpointStatsTxError,
       "mIfNxStatusEndpointStatsRxError": mIfNxStatusEndpointStatsRxError,
       "mIfNxStatusEndpointStatsTxDrop": mIfNxStatusEndpointStatsTxDrop,
       "mIfNxStatusEndpointStatsRxDrop": mIfNxStatusEndpointStatsRxDrop,
       "mIfNxStatusActChanTable": mIfNxStatusActChanTable,
       "mIfNxStatusActChanEntry": mIfNxStatusActChanEntry,
       "mIfNxStatusActChanChannel": mIfNxStatusActChanChannel,
       "mIfNxStatusActChanFrequency": mIfNxStatusActChanFrequency,
       "mIfNxStatusActChanAvgRssi": mIfNxStatusActChanAvgRssi,
       "mIfNxStatusActChanAvgLqi": mIfNxStatusActChanAvgLqi,
       "mdsIfNxMIBConformance": mdsIfNxMIBConformance,
       "mdsIfNxMIBCompliances": mdsIfNxMIBCompliances,
       "mIfNxCompliance": mIfNxCompliance,
       "mdsIfNxMIBGroups": mdsIfNxMIBGroups,
       "mIfNxStatusGroup": mIfNxStatusGroup,
       "mIfNxStatusConnRemGroup": mIfNxStatusConnRemGroup,
       "mIfNxStatusEndpointGroup": mIfNxStatusEndpointGroup,
       "mIfNxStatusActChanGroup": mIfNxStatusActChanGroup}
)
