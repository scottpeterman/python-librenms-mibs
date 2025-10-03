# SNMP MIB module (SIAE-RADIO-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-RADIO-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:00 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(AlarmSeverityCode,
 AlarmStatus,
 alarmTrap) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "AlarmSeverityCode",
    "AlarmStatus",
    "alarmTrap")

(equipIpSnmpAgentAddress,) = mibBuilder.importSymbols(
    "SIAE-EQUIP-MIB",
    "equipIpSnmpAgentAddress")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

radioSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80)
)
if mibBuilder.loadTexts:
    radioSystem.setRevisions(
        ("2016-07-14 00:00",
         "2016-02-29 00:00",
         "2015-09-15 00:00",
         "2015-06-18 00:00",
         "2015-03-23 00:00",
         "2014-11-05 00:00",
         "2014-09-16 00:00",
         "2014-04-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ChannelSpacing(TextualConvention, Integer32):
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
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("bw3M5Hz", 0),
          ("bw7Mhz", 1),
          ("bw14MHz", 2),
          ("bw28MHz", 3),
          ("bw56MHz", 4),
          ("bw40MHz", 5),
          ("bw112MHz", 6),
          ("bw250Mhz", 7),
          ("bw500Mhz", 8),
          ("bw750Mhz", 9),
          ("bw1000Mhz", 10),
          ("bw10Mhz", 11),
          ("bw20Mhz", 12),
          ("bw30Mhz", 13),
          ("bw50Mhz", 14),
          ("bw60Mhz", 15),
          ("bw80Mhz", 16))
    )



class ModulationMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("modBPSK", 0),
          ("mod4QAM", 1),
          ("mod8PSK", 2),
          ("mod16QAM", 3),
          ("mod32QAM", 4),
          ("mod64QAM", 5),
          ("mod128QAM", 6),
          ("mod256QAM", 7),
          ("mod512QAM", 8),
          ("mod1024QAM", 9),
          ("mod2048QAM", 10),
          ("mod4096QAM", 11))
    )


class ConfigMismatchReason(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("securityMismatch", 0),
          ("frequencyFailMismatch", 1),
          ("frequencyAlertMismatch", 2),
          ("ptxMismatch", 3),
          ("channelSpacingAndModulationMismatch", 4),
          ("remoteConfigurationMismatch", 5),
          ("acmMismatch", 6),
          ("profileSetMismatch", 7))
    )


class RadioCapability(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("reserved", 0),
          ("trafficSquelch", 1),
          ("baseBandLoop", 2),
          ("maxPower", 3),
          ("carrierOnly", 4),
          ("iQLoop", 5),
          ("rfLoopGivenMod", 6),
          ("rfLoopAnyMod", 7))
    )


class BitsPerSymbol(TextualConvention, Integer32):
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bpsBPSK", 1),
          ("bps4QAM", 2),
          ("bps8PSK", 3),
          ("bps16QAM", 4),
          ("bps32QAM", 5),
          ("bps64QAM", 6),
          ("bps128QAM", 7),
          ("bps256QAM", 8),
          ("bps512QAM", 9),
          ("bps1024QAM", 10),
          ("bps2048QAM", 11),
          ("bps4096QAM", 12))
    )



class Stm1IndexOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_RadioSystemMibVersion_Type = Integer32
_RadioSystemMibVersion_Object = MibScalar
radioSystemMibVersion = _RadioSystemMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 1),
    _RadioSystemMibVersion_Type()
)
radioSystemMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioSystemMibVersion.setStatus("current")
_RadioTable_Object = MibTable
radioTable = _RadioTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 2)
)
if mibBuilder.loadTexts:
    radioTable.setStatus("current")
_RadioEntry_Object = MibTableRow
radioEntry = _RadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 2, 1)
)
radioEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioIndex"),
)
if mibBuilder.loadTexts:
    radioEntry.setStatus("current")
_RadioIndex_Type = Integer32
_RadioIndex_Object = MibTableColumn
radioIndex = _RadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 2, 1, 1),
    _RadioIndex_Type()
)
radioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioIndex.setStatus("current")


class _RadioLabel_Type(DisplayString):
    """Custom type radioLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RadioLabel_Type.__name__ = "DisplayString"
_RadioLabel_Object = MibTableColumn
radioLabel = _RadioLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 2, 1, 2),
    _RadioLabel_Type()
)
radioLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLabel.setStatus("current")


class _RadioType_Type(Integer32):
    """Custom type radioType based on Integer32"""
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
          ("analogRadio", 2),
          ("digitalRadio", 3),
          ("xpicRadio", 4))
    )


_RadioType_Type.__name__ = "Integer32"
_RadioType_Object = MibTableColumn
radioType = _RadioType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 2, 1, 3),
    _RadioType_Type()
)
radioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioType.setStatus("current")
_RadioIfIndex_Type = InterfaceIndexOrZero
_RadioIfIndex_Object = MibTableColumn
radioIfIndex = _RadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 2, 1, 4),
    _RadioIfIndex_Type()
)
radioIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioIfIndex.setStatus("current")
_RadioStorageType_Type = StorageType
_RadioStorageType_Object = MibTableColumn
radioStorageType = _RadioStorageType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 2, 1, 5),
    _RadioStorageType_Type()
)
radioStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioStorageType.setStatus("current")
_XpicTable_Object = MibTable
xpicTable = _XpicTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 3)
)
if mibBuilder.loadTexts:
    xpicTable.setStatus("current")
_XpicEntry_Object = MibTableRow
xpicEntry = _XpicEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 3, 1)
)
xpicEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "xpicIndex"),
)
if mibBuilder.loadTexts:
    xpicEntry.setStatus("current")
_XpicIndex_Type = Integer32
_XpicIndex_Object = MibTableColumn
xpicIndex = _XpicIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 3, 1, 1),
    _XpicIndex_Type()
)
xpicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpicIndex.setStatus("current")
_XpicRadioIdx_Type = Integer32
_XpicRadioIdx_Object = MibTableColumn
xpicRadioIdx = _XpicRadioIdx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 3, 1, 2),
    _XpicRadioIdx_Type()
)
xpicRadioIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpicRadioIdx.setStatus("current")
_XpicRowstatus_Type = RowStatus
_XpicRowstatus_Object = MibTableColumn
xpicRowstatus = _XpicRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 3, 1, 3),
    _XpicRowstatus_Type()
)
xpicRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpicRowstatus.setStatus("current")
_XpicChTable_Object = MibTable
xpicChTable = _XpicChTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 4)
)
if mibBuilder.loadTexts:
    xpicChTable.setStatus("current")
_XpicChEntry_Object = MibTableRow
xpicChEntry = _XpicChEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 4, 1)
)
xpicChEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "xpicIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "xpicChPolIndex"),
)
if mibBuilder.loadTexts:
    xpicChEntry.setStatus("current")


class _XpicChPolIndex_Type(Integer32):
    """Custom type xpicChPolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_XpicChPolIndex_Type.__name__ = "Integer32"
_XpicChPolIndex_Object = MibTableColumn
xpicChPolIndex = _XpicChPolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 4, 1, 1),
    _XpicChPolIndex_Type()
)
xpicChPolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpicChPolIndex.setStatus("current")
_XpicChRadioIdx_Type = Integer32
_XpicChRadioIdx_Object = MibTableColumn
xpicChRadioIdx = _XpicChRadioIdx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 4, 1, 2),
    _XpicChRadioIdx_Type()
)
xpicChRadioIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpicChRadioIdx.setStatus("current")
_XpicChRowstatus_Type = RowStatus
_XpicChRowstatus_Object = MibTableColumn
xpicChRowstatus = _XpicChRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 4, 1, 3),
    _XpicChRowstatus_Type()
)
xpicChRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xpicChRowstatus.setStatus("current")
_LinkAvailableIndex_Type = Integer32
_LinkAvailableIndex_Object = MibScalar
linkAvailableIndex = _LinkAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 5),
    _LinkAvailableIndex_Type()
)
linkAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAvailableIndex.setStatus("current")
_LinkTable_Object = MibTable
linkTable = _LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 6)
)
if mibBuilder.loadTexts:
    linkTable.setStatus("current")
_LinkEntry_Object = MibTableRow
linkEntry = _LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 6, 1)
)
linkEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
)
if mibBuilder.loadTexts:
    linkEntry.setStatus("current")
_LinkIndex_Type = Integer32
_LinkIndex_Object = MibTableColumn
linkIndex = _LinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 6, 1, 1),
    _LinkIndex_Type()
)
linkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkIndex.setStatus("current")


class _LinkType_Type(Integer32):
    """Custom type linkType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("radio1p0", 1),
          ("radio1p1HS", 2),
          ("radio1p1FD", 3),
          ("radio2p0Xpic", 4),
          ("radio2p2XpicHS", 5),
          ("radio2p2XpicFD", 6),
          ("radioNp1", 7))
    )


_LinkType_Type.__name__ = "Integer32"
_LinkType_Object = MibTableColumn
linkType = _LinkType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 6, 1, 2),
    _LinkType_Type()
)
linkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkType.setStatus("current")


class _LinkLabel_Type(DisplayString):
    """Custom type linkLabel based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LinkLabel_Type.__name__ = "DisplayString"
_LinkLabel_Object = MibTableColumn
linkLabel = _LinkLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 6, 1, 3),
    _LinkLabel_Type()
)
linkLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkLabel.setStatus("current")


class _LinkIfIndex_Type(InterfaceIndexOrZero):
    """Custom type linkIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_LinkIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_LinkIfIndex_Object = MibTableColumn
linkIfIndex = _LinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 6, 1, 4),
    _LinkIfIndex_Type()
)
linkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkIfIndex.setStatus("current")
_LinkRowstatus_Type = RowStatus
_LinkRowstatus_Object = MibTableColumn
linkRowstatus = _LinkRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 6, 1, 5),
    _LinkRowstatus_Type()
)
linkRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkRowstatus.setStatus("current")
_LinkChTable_Object = MibTable
linkChTable = _LinkChTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 7)
)
if mibBuilder.loadTexts:
    linkChTable.setStatus("current")
_LinkChEntry_Object = MibTableRow
linkChEntry = _LinkChEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 7, 1)
)
linkChEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkChIndex"),
)
if mibBuilder.loadTexts:
    linkChEntry.setStatus("current")
_LinkChIndex_Type = Integer32
_LinkChIndex_Object = MibTableColumn
linkChIndex = _LinkChIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 7, 1, 1),
    _LinkChIndex_Type()
)
linkChIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkChIndex.setStatus("current")
_LinkChRadioIdx_Type = Integer32
_LinkChRadioIdx_Object = MibTableColumn
linkChRadioIdx = _LinkChRadioIdx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 7, 1, 2),
    _LinkChRadioIdx_Type()
)
linkChRadioIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkChRadioIdx.setStatus("current")


class _LinkChRadioSettingsIdx_Type(Integer32):
    """Custom type linkChRadioSettingsIdx based on Integer32"""
    defaultValue = 0


_LinkChRadioSettingsIdx_Type.__name__ = "Integer32"
_LinkChRadioSettingsIdx_Object = MibTableColumn
linkChRadioSettingsIdx = _LinkChRadioSettingsIdx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 7, 1, 3),
    _LinkChRadioSettingsIdx_Type()
)
linkChRadioSettingsIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkChRadioSettingsIdx.setStatus("current")
_LinkChRowstatus_Type = RowStatus
_LinkChRowstatus_Object = MibTableColumn
linkChRowstatus = _LinkChRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 7, 1, 4),
    _LinkChRowstatus_Type()
)
linkChRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkChRowstatus.setStatus("current")
_LinkSettingsTable_Object = MibTable
linkSettingsTable = _LinkSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 8)
)
if mibBuilder.loadTexts:
    linkSettingsTable.setStatus("current")
_LinkSettingsEntry_Object = MibTableRow
linkSettingsEntry = _LinkSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 8, 1)
)
linkSettingsEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
)
if mibBuilder.loadTexts:
    linkSettingsEntry.setStatus("current")
_LinkBandwidthAndModulation_Type = Integer32
_LinkBandwidthAndModulation_Object = MibTableColumn
linkBandwidthAndModulation = _LinkBandwidthAndModulation_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 8, 1, 1),
    _LinkBandwidthAndModulation_Type()
)
linkBandwidthAndModulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkBandwidthAndModulation.setStatus("current")


class _LinkAcmEngineEnable_Type(Integer32):
    """Custom type linkAcmEngineEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkAcmEngineEnable_Type.__name__ = "Integer32"
_LinkAcmEngineEnable_Object = MibTableColumn
linkAcmEngineEnable = _LinkAcmEngineEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 8, 1, 2),
    _LinkAcmEngineEnable_Type()
)
linkAcmEngineEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkAcmEngineEnable.setStatus("current")
_LinkTxUpperProfile_Type = Integer32
_LinkTxUpperProfile_Object = MibTableColumn
linkTxUpperProfile = _LinkTxUpperProfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 8, 1, 3),
    _LinkTxUpperProfile_Type()
)
linkTxUpperProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkTxUpperProfile.setStatus("current")
_LinkTxLowerProfile_Type = Integer32
_LinkTxLowerProfile_Object = MibTableColumn
linkTxLowerProfile = _LinkTxLowerProfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 8, 1, 4),
    _LinkTxLowerProfile_Type()
)
linkTxLowerProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkTxLowerProfile.setStatus("current")


class _LinkId_Type(Integer32):
    """Custom type linkId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LinkId_Type.__name__ = "Integer32"
_LinkId_Object = MibTableColumn
linkId = _LinkId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 8, 1, 5),
    _LinkId_Type()
)
linkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkId.setStatus("current")


class _LinkTxPwrThresh_Type(Integer32):
    """Custom type linkTxPwrThresh based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 15),
    )


_LinkTxPwrThresh_Type.__name__ = "Integer32"
_LinkTxPwrThresh_Object = MibTableColumn
linkTxPwrThresh = _LinkTxPwrThresh_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 8, 1, 6),
    _LinkTxPwrThresh_Type()
)
linkTxPwrThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkTxPwrThresh.setStatus("current")


class _LinkRxPwrThresh_Type(Integer32):
    """Custom type linkRxPwrThresh based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -40),
    )


_LinkRxPwrThresh_Type.__name__ = "Integer32"
_LinkRxPwrThresh_Object = MibTableColumn
linkRxPwrThresh = _LinkRxPwrThresh_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 8, 1, 7),
    _LinkRxPwrThresh_Type()
)
linkRxPwrThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkRxPwrThresh.setStatus("current")


class _LinkSynchSetupProtocolEnable_Type(Integer32):
    """Custom type linkSynchSetupProtocolEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkSynchSetupProtocolEnable_Type.__name__ = "Integer32"
_LinkSynchSetupProtocolEnable_Object = MibTableColumn
linkSynchSetupProtocolEnable = _LinkSynchSetupProtocolEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 8, 1, 8),
    _LinkSynchSetupProtocolEnable_Type()
)
linkSynchSetupProtocolEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkSynchSetupProtocolEnable.setStatus("current")


class _LinkProfilesSetSelection_Type(Integer32):
    """Custom type linkProfilesSetSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highThroughput", 1),
          ("highGain", 2))
    )


_LinkProfilesSetSelection_Type.__name__ = "Integer32"
_LinkProfilesSetSelection_Object = MibTableColumn
linkProfilesSetSelection = _LinkProfilesSetSelection_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 8, 1, 9),
    _LinkProfilesSetSelection_Type()
)
linkProfilesSetSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProfilesSetSelection.setStatus("current")


class _LinkXpicControlProcedure_Type(Integer32):
    """Custom type linkXpicControlProcedure based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkXpicControlProcedure_Type.__name__ = "Integer32"
_LinkXpicControlProcedure_Object = MibTableColumn
linkXpicControlProcedure = _LinkXpicControlProcedure_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 8, 1, 10),
    _LinkXpicControlProcedure_Type()
)
linkXpicControlProcedure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkXpicControlProcedure.setStatus("current")
_RadioSettingsTable_Object = MibTable
radioSettingsTable = _RadioSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 9)
)
if mibBuilder.loadTexts:
    radioSettingsTable.setStatus("current")
_RadioSettingsEntry_Object = MibTableRow
radioSettingsEntry = _RadioSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 9, 1)
)
radioSettingsEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioSettingsIndex"),
)
if mibBuilder.loadTexts:
    radioSettingsEntry.setStatus("current")
_RadioSettingsIndex_Type = Integer32
_RadioSettingsIndex_Object = MibTableColumn
radioSettingsIndex = _RadioSettingsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 9, 1, 1),
    _RadioSettingsIndex_Type()
)
radioSettingsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioSettingsIndex.setStatus("current")
_RadioSettingsRowStatus_Type = RowStatus
_RadioSettingsRowStatus_Object = MibTableColumn
radioSettingsRowStatus = _RadioSettingsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 9, 1, 2),
    _RadioSettingsRowStatus_Type()
)
radioSettingsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radioSettingsRowStatus.setStatus("current")


class _RadioSettingsLabel_Type(DisplayString):
    """Custom type radioSettingsLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RadioSettingsLabel_Type.__name__ = "DisplayString"
_RadioSettingsLabel_Object = MibTableColumn
radioSettingsLabel = _RadioSettingsLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 9, 1, 3),
    _RadioSettingsLabel_Type()
)
radioSettingsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioSettingsLabel.setStatus("current")


class _RadioTxFrequency_Type(Integer32):
    """Custom type radioTxFrequency based on Integer32"""
    defaultValue = 0


_RadioTxFrequency_Type.__name__ = "Integer32"
_RadioTxFrequency_Object = MibTableColumn
radioTxFrequency = _RadioTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 9, 1, 4),
    _RadioTxFrequency_Type()
)
radioTxFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radioTxFrequency.setStatus("current")


class _RadioDuplexFrequency_Type(Integer32):
    """Custom type radioDuplexFrequency based on Integer32"""
    defaultValue = -2


_RadioDuplexFrequency_Type.__name__ = "Integer32"
_RadioDuplexFrequency_Object = MibTableColumn
radioDuplexFrequency = _RadioDuplexFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 9, 1, 5),
    _RadioDuplexFrequency_Type()
)
radioDuplexFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radioDuplexFrequency.setStatus("current")
_RadioTxAttenuation_Type = Integer32
_RadioTxAttenuation_Object = MibTableColumn
radioTxAttenuation = _RadioTxAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 9, 1, 6),
    _RadioTxAttenuation_Type()
)
radioTxAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radioTxAttenuation.setStatus("current")


class _RadioAtpcManual_Type(Integer32):
    """Custom type radioAtpcManual based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RadioAtpcManual_Type.__name__ = "Integer32"
_RadioAtpcManual_Object = MibTableColumn
radioAtpcManual = _RadioAtpcManual_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 9, 1, 7),
    _RadioAtpcManual_Type()
)
radioAtpcManual.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radioAtpcManual.setStatus("current")


class _RadioAtpcPwrHigh_Type(Integer32):
    """Custom type radioAtpcPwrHigh based on Integer32"""
    defaultValue = -40


_RadioAtpcPwrHigh_Type.__name__ = "Integer32"
_RadioAtpcPwrHigh_Object = MibTableColumn
radioAtpcPwrHigh = _RadioAtpcPwrHigh_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 9, 1, 8),
    _RadioAtpcPwrHigh_Type()
)
radioAtpcPwrHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radioAtpcPwrHigh.setStatus("current")


class _RadioAtpcPwrLow_Type(Integer32):
    """Custom type radioAtpcPwrLow based on Integer32"""
    defaultValue = -60


_RadioAtpcPwrLow_Type.__name__ = "Integer32"
_RadioAtpcPwrLow_Object = MibTableColumn
radioAtpcPwrLow = _RadioAtpcPwrLow_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 9, 1, 9),
    _RadioAtpcPwrLow_Type()
)
radioAtpcPwrLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radioAtpcPwrLow.setStatus("current")


class _RadioAtpcRange_Type(Integer32):
    """Custom type radioAtpcRange based on Integer32"""
    defaultValue = 0


_RadioAtpcRange_Type.__name__ = "Integer32"
_RadioAtpcRange_Object = MibTableColumn
radioAtpcRange = _RadioAtpcRange_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 9, 1, 10),
    _RadioAtpcRange_Type()
)
radioAtpcRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radioAtpcRange.setStatus("current")
_RadioFreqTableSelection_Type = ChannelSpacing
_RadioFreqTableSelection_Object = MibTableColumn
radioFreqTableSelection = _RadioFreqTableSelection_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 9, 1, 11),
    _RadioFreqTableSelection_Type()
)
radioFreqTableSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radioFreqTableSelection.setStatus("current")
_TdmSettingsTable_Object = MibTable
tdmSettingsTable = _TdmSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 10)
)
if mibBuilder.loadTexts:
    tdmSettingsTable.setStatus("current")
_TdmSettingsEntry_Object = MibTableRow
tdmSettingsEntry = _TdmSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 10, 1)
)
tdmSettingsEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "tdmPolIndex"),
)
if mibBuilder.loadTexts:
    tdmSettingsEntry.setStatus("current")
_TdmPolIndex_Type = Integer32
_TdmPolIndex_Object = MibTableColumn
tdmPolIndex = _TdmPolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 10, 1, 1),
    _TdmPolIndex_Type()
)
tdmPolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmPolIndex.setStatus("current")


class _TdmE1Channel_Type(Integer32):
    """Custom type tdmE1Channel based on Integer32"""
    defaultValue = 0


_TdmE1Channel_Type.__name__ = "Integer32"
_TdmE1Channel_Object = MibTableColumn
tdmE1Channel = _TdmE1Channel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 10, 1, 2),
    _TdmE1Channel_Type()
)
tdmE1Channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmE1Channel.setStatus("current")


class _TdmE1Framer_Type(Integer32):
    """Custom type tdmE1Framer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_TdmE1Framer_Type.__name__ = "Integer32"
_TdmE1Framer_Object = MibTableColumn
tdmE1Framer = _TdmE1Framer_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 10, 1, 3),
    _TdmE1Framer_Type()
)
tdmE1Framer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmE1Framer.setStatus("current")
_RadioCapabilitiesTable_Object = MibTable
radioCapabilitiesTable = _RadioCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 11)
)
if mibBuilder.loadTexts:
    radioCapabilitiesTable.setStatus("current")
_RadioCapabilitiesEntry_Object = MibTableRow
radioCapabilitiesEntry = _RadioCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 11, 1)
)
radioCapabilitiesEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioIndex"),
)
if mibBuilder.loadTexts:
    radioCapabilitiesEntry.setStatus("current")
_RadioCapabilitiesCapability_Type = RadioCapability
_RadioCapabilitiesCapability_Object = MibTableColumn
radioCapabilitiesCapability = _RadioCapabilitiesCapability_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 11, 1, 1),
    _RadioCapabilitiesCapability_Type()
)
radioCapabilitiesCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioCapabilitiesCapability.setStatus("current")
_RadioCapabilitiesTxMinFrequency_Type = Integer32
_RadioCapabilitiesTxMinFrequency_Object = MibTableColumn
radioCapabilitiesTxMinFrequency = _RadioCapabilitiesTxMinFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 11, 1, 2),
    _RadioCapabilitiesTxMinFrequency_Type()
)
radioCapabilitiesTxMinFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioCapabilitiesTxMinFrequency.setStatus("current")
_RadioCapabilitiesTxMaxFrequency_Type = Integer32
_RadioCapabilitiesTxMaxFrequency_Object = MibTableColumn
radioCapabilitiesTxMaxFrequency = _RadioCapabilitiesTxMaxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 11, 1, 3),
    _RadioCapabilitiesTxMaxFrequency_Type()
)
radioCapabilitiesTxMaxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioCapabilitiesTxMaxFrequency.setStatus("current")
_RadioCapabilitiesStepFrequency_Type = Integer32
_RadioCapabilitiesStepFrequency_Object = MibTableColumn
radioCapabilitiesStepFrequency = _RadioCapabilitiesStepFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 11, 1, 4),
    _RadioCapabilitiesStepFrequency_Type()
)
radioCapabilitiesStepFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioCapabilitiesStepFrequency.setStatus("current")
_RadioCapabilitiesMinPtxNominalValue_Type = Integer32
_RadioCapabilitiesMinPtxNominalValue_Object = MibTableColumn
radioCapabilitiesMinPtxNominalValue = _RadioCapabilitiesMinPtxNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 11, 1, 5),
    _RadioCapabilitiesMinPtxNominalValue_Type()
)
radioCapabilitiesMinPtxNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioCapabilitiesMinPtxNominalValue.setStatus("current")
_RadioCapabilitiesMaxPtxNominalValue_Type = Integer32
_RadioCapabilitiesMaxPtxNominalValue_Object = MibTableColumn
radioCapabilitiesMaxPtxNominalValue = _RadioCapabilitiesMaxPtxNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 11, 1, 6),
    _RadioCapabilitiesMaxPtxNominalValue_Type()
)
radioCapabilitiesMaxPtxNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioCapabilitiesMaxPtxNominalValue.setStatus("current")
_RadioCapabilitiesExtendedMinPwr_Type = Integer32
_RadioCapabilitiesExtendedMinPwr_Object = MibTableColumn
radioCapabilitiesExtendedMinPwr = _RadioCapabilitiesExtendedMinPwr_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 11, 1, 7),
    _RadioCapabilitiesExtendedMinPwr_Type()
)
radioCapabilitiesExtendedMinPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioCapabilitiesExtendedMinPwr.setStatus("current")
_RadioStatusTable_Object = MibTable
radioStatusTable = _RadioStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12)
)
if mibBuilder.loadTexts:
    radioStatusTable.setStatus("current")
_RadioStatusEntry_Object = MibTableRow
radioStatusEntry = _RadioStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1)
)
radioStatusEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioIndex"),
)
if mibBuilder.loadTexts:
    radioStatusEntry.setStatus("current")
_RadioCurrentDuplexFrequency_Type = Integer32
_RadioCurrentDuplexFrequency_Object = MibTableColumn
radioCurrentDuplexFrequency = _RadioCurrentDuplexFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 1),
    _RadioCurrentDuplexFrequency_Type()
)
radioCurrentDuplexFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioCurrentDuplexFrequency.setStatus("current")
_RadioTxChannelSpacing_Type = Integer32
_RadioTxChannelSpacing_Object = MibTableColumn
radioTxChannelSpacing = _RadioTxChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 2),
    _RadioTxChannelSpacing_Type()
)
radioTxChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioTxChannelSpacing.setStatus("current")
_RadioPrx_Type = Integer32
_RadioPrx_Object = MibTableColumn
radioPrx = _RadioPrx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 3),
    _RadioPrx_Type()
)
radioPrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioPrx.setStatus("current")
_RadioPtx_Type = Integer32
_RadioPtx_Object = MibTableColumn
radioPtx = _RadioPtx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 4),
    _RadioPtx_Type()
)
radioPtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioPtx.setStatus("current")
_RadioNormalizedMse_Type = Integer32
_RadioNormalizedMse_Object = MibTableColumn
radioNormalizedMse = _RadioNormalizedMse_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 5),
    _RadioNormalizedMse_Type()
)
radioNormalizedMse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioNormalizedMse.setStatus("current")


class _RadioRxActiveStatus_Type(Integer32):
    """Custom type radioRxActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("active", 2))
    )


_RadioRxActiveStatus_Type.__name__ = "Integer32"
_RadioRxActiveStatus_Object = MibTableColumn
radioRxActiveStatus = _RadioRxActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 6),
    _RadioRxActiveStatus_Type()
)
radioRxActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRxActiveStatus.setStatus("current")


class _RadioTxActiveStatus_Type(Integer32):
    """Custom type radioTxActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("active", 2))
    )


_RadioTxActiveStatus_Type.__name__ = "Integer32"
_RadioTxActiveStatus_Object = MibTableColumn
radioTxActiveStatus = _RadioTxActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 7),
    _RadioTxActiveStatus_Type()
)
radioTxActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioTxActiveStatus.setStatus("current")
_RadioCableOpenAlarm_Type = AlarmStatus
_RadioCableOpenAlarm_Object = MibTableColumn
radioCableOpenAlarm = _RadioCableOpenAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 8),
    _RadioCableOpenAlarm_Type()
)
radioCableOpenAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioCableOpenAlarm.setStatus("current")
_RadioCableShortAlarm_Type = AlarmStatus
_RadioCableShortAlarm_Object = MibTableColumn
radioCableShortAlarm = _RadioCableShortAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 9),
    _RadioCableShortAlarm_Type()
)
radioCableShortAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioCableShortAlarm.setStatus("current")
_RadioInvalidFrequencyAlarm_Type = AlarmStatus
_RadioInvalidFrequencyAlarm_Object = MibTableColumn
radioInvalidFrequencyAlarm = _RadioInvalidFrequencyAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 10),
    _RadioInvalidFrequencyAlarm_Type()
)
radioInvalidFrequencyAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioInvalidFrequencyAlarm.setStatus("current")
_RadioBaseBandRxAlarm_Type = AlarmStatus
_RadioBaseBandRxAlarm_Object = MibTableColumn
radioBaseBandRxAlarm = _RadioBaseBandRxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 11),
    _RadioBaseBandRxAlarm_Type()
)
radioBaseBandRxAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioBaseBandRxAlarm.setStatus("current")
_RadioModulatorFailAlarm_Type = AlarmStatus
_RadioModulatorFailAlarm_Object = MibTableColumn
radioModulatorFailAlarm = _RadioModulatorFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 12),
    _RadioModulatorFailAlarm_Type()
)
radioModulatorFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioModulatorFailAlarm.setStatus("current")
_RadioDemodulatorFailAlarm_Type = AlarmStatus
_RadioDemodulatorFailAlarm_Object = MibTableColumn
radioDemodulatorFailAlarm = _RadioDemodulatorFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 13),
    _RadioDemodulatorFailAlarm_Type()
)
radioDemodulatorFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioDemodulatorFailAlarm.setStatus("current")
_RadioRxPowerLowAlarm_Type = AlarmStatus
_RadioRxPowerLowAlarm_Object = MibTableColumn
radioRxPowerLowAlarm = _RadioRxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 14),
    _RadioRxPowerLowAlarm_Type()
)
radioRxPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRxPowerLowAlarm.setStatus("current")
_RadioTxPowerLowAlarm_Type = AlarmStatus
_RadioTxPowerLowAlarm_Object = MibTableColumn
radioTxPowerLowAlarm = _RadioTxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 15),
    _RadioTxPowerLowAlarm_Type()
)
radioTxPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioTxPowerLowAlarm.setStatus("current")
_RadioRemDemodulatorFailAlarm_Type = AlarmStatus
_RadioRemDemodulatorFailAlarm_Object = MibTableColumn
radioRemDemodulatorFailAlarm = _RadioRemDemodulatorFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 16),
    _RadioRemDemodulatorFailAlarm_Type()
)
radioRemDemodulatorFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRemDemodulatorFailAlarm.setStatus("current")
_RadioVcoFailAlarm_Type = AlarmStatus
_RadioVcoFailAlarm_Object = MibTableColumn
radioVcoFailAlarm = _RadioVcoFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 17),
    _RadioVcoFailAlarm_Type()
)
radioVcoFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioVcoFailAlarm.setStatus("current")
_RadioRxIFAgcAlarm_Type = AlarmStatus
_RadioRxIFAgcAlarm_Object = MibTableColumn
radioRxIFAgcAlarm = _RadioRxIFAgcAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 18),
    _RadioRxIFAgcAlarm_Type()
)
radioRxIFAgcAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRxIFAgcAlarm.setStatus("current")
_RadioTxIFAgcAlarm_Type = AlarmStatus
_RadioTxIFAgcAlarm_Object = MibTableColumn
radioTxIFAgcAlarm = _RadioTxIFAgcAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 19),
    _RadioTxIFAgcAlarm_Type()
)
radioTxIFAgcAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioTxIFAgcAlarm.setStatus("current")
_RadioIduOduCommunicationAlarm_Type = AlarmStatus
_RadioIduOduCommunicationAlarm_Object = MibTableColumn
radioIduOduCommunicationAlarm = _RadioIduOduCommunicationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 20),
    _RadioIduOduCommunicationAlarm_Type()
)
radioIduOduCommunicationAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioIduOduCommunicationAlarm.setStatus("current")
_RadioOduIduCommunicationAlarm_Type = AlarmStatus
_RadioOduIduCommunicationAlarm_Object = MibTableColumn
radioOduIduCommunicationAlarm = _RadioOduIduCommunicationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 21),
    _RadioOduIduCommunicationAlarm_Type()
)
radioOduIduCommunicationAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioOduIduCommunicationAlarm.setStatus("current")
_RadioLocalOduAlarmSynthesis_Type = AlarmStatus
_RadioLocalOduAlarmSynthesis_Object = MibTableColumn
radioLocalOduAlarmSynthesis = _RadioLocalOduAlarmSynthesis_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 22),
    _RadioLocalOduAlarmSynthesis_Type()
)
radioLocalOduAlarmSynthesis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLocalOduAlarmSynthesis.setStatus("current")
_RadioRemoteOduAlarmSynthesis_Type = AlarmStatus
_RadioRemoteOduAlarmSynthesis_Object = MibTableColumn
radioRemoteOduAlarmSynthesis = _RadioRemoteOduAlarmSynthesis_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 23),
    _RadioRemoteOduAlarmSynthesis_Type()
)
radioRemoteOduAlarmSynthesis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRemoteOduAlarmSynthesis.setStatus("current")
_RadioConfigMismatchAlarm_Type = AlarmStatus
_RadioConfigMismatchAlarm_Object = MibTableColumn
radioConfigMismatchAlarm = _RadioConfigMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 24),
    _RadioConfigMismatchAlarm_Type()
)
radioConfigMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioConfigMismatchAlarm.setStatus("current")
_RadioConfigAlarmReason_Type = ConfigMismatchReason
_RadioConfigAlarmReason_Object = MibTableColumn
radioConfigAlarmReason = _RadioConfigAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 25),
    _RadioConfigAlarmReason_Type()
)
radioConfigAlarmReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioConfigAlarmReason.setStatus("current")
_RadioRxQualityLowAlarm_Type = AlarmStatus
_RadioRxQualityLowAlarm_Object = MibTableColumn
radioRxQualityLowAlarm = _RadioRxQualityLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 26),
    _RadioRxQualityLowAlarm_Type()
)
radioRxQualityLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRxQualityLowAlarm.setStatus("current")
_RadioRxQualityWarningAlarm_Type = AlarmStatus
_RadioRxQualityWarningAlarm_Object = MibTableColumn
radioRxQualityWarningAlarm = _RadioRxQualityWarningAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 27),
    _RadioRxQualityWarningAlarm_Type()
)
radioRxQualityWarningAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRxQualityWarningAlarm.setStatus("current")
_RadioXpd_Type = Integer32
_RadioXpd_Object = MibTableColumn
radioXpd = _RadioXpd_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 12, 1, 28),
    _RadioXpd_Type()
)
radioXpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioXpd.setStatus("current")
_RadioMaintTable_Object = MibTable
radioMaintTable = _RadioMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 13)
)
if mibBuilder.loadTexts:
    radioMaintTable.setStatus("current")
_RadioMaintEntry_Object = MibTableRow
radioMaintEntry = _RadioMaintEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 13, 1)
)
radioMaintEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioIndex"),
)
if mibBuilder.loadTexts:
    radioMaintEntry.setStatus("current")


class _RadioTxStatus_Type(Integer32):
    """Custom type radioTxStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("transmitterOff", 1),
          ("transmitterOn", 2),
          ("permanentOff", 3))
    )


_RadioTxStatus_Type.__name__ = "Integer32"
_RadioTxStatus_Object = MibTableColumn
radioTxStatus = _RadioTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 13, 1, 1),
    _RadioTxStatus_Type()
)
radioTxStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioTxStatus.setStatus("current")


class _RadioCarrierOnly_Type(Integer32):
    """Custom type radioCarrierOnly based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("carrierOnlyOff", 1),
          ("carrierOnlyOn", 2))
    )


_RadioCarrierOnly_Type.__name__ = "Integer32"
_RadioCarrierOnly_Object = MibTableColumn
radioCarrierOnly = _RadioCarrierOnly_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 13, 1, 2),
    _RadioCarrierOnly_Type()
)
radioCarrierOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioCarrierOnly.setStatus("current")


class _RadioLoop_Type(Integer32):
    """Custom type radioLoop based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("loopOff", 1),
          ("rfLoop", 2),
          ("iqLoop", 3),
          ("baseBandLoop", 4),
          ("rfLoopAtFixedMod", 6),
          ("baseBandLoopEthSquelch", 7),
          ("rfLoopAtFixedModEthSquelch", 8),
          ("iqloopEthSquelch", 9))
    )


_RadioLoop_Type.__name__ = "Integer32"
_RadioLoop_Object = MibTableColumn
radioLoop = _RadioLoop_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 13, 1, 3),
    _RadioLoop_Type()
)
radioLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioLoop.setStatus("current")


class _RadioRFLoopTestResult_Type(Integer32):
    """Custom type radioRFLoopTestResult based on Integer32"""
    defaultValue = 0

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
        *(("testNone", 0),
          ("testRunning", 1),
          ("testNotPossible", 2),
          ("testPassed", 3),
          ("testFail", 4),
          ("testInterrupted", 5))
    )


_RadioRFLoopTestResult_Type.__name__ = "Integer32"
_RadioRFLoopTestResult_Object = MibTableColumn
radioRFLoopTestResult = _RadioRFLoopTestResult_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 13, 1, 4),
    _RadioRFLoopTestResult_Type()
)
radioRFLoopTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRFLoopTestResult.setStatus("current")


class _RadioRFLoopTestPercTime_Type(Integer32):
    """Custom type radioRFLoopTestPercTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RadioRFLoopTestPercTime_Type.__name__ = "Integer32"
_RadioRFLoopTestPercTime_Object = MibTableColumn
radioRFLoopTestPercTime = _RadioRFLoopTestPercTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 13, 1, 5),
    _RadioRFLoopTestPercTime_Type()
)
radioRFLoopTestPercTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRFLoopTestPercTime.setStatus("current")


class _RadioRtPsuOff_Type(Integer32):
    """Custom type radioRtPsuOff based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtPsuOff", 1),
          ("rtPsuOn", 2))
    )


_RadioRtPsuOff_Type.__name__ = "Integer32"
_RadioRtPsuOff_Object = MibTableColumn
radioRtPsuOff = _RadioRtPsuOff_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 13, 1, 6),
    _RadioRtPsuOff_Type()
)
radioRtPsuOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioRtPsuOff.setStatus("current")


class _RadioLom_Type(Integer32):
    """Custom type radioLom based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RadioLom_Type.__name__ = "Integer32"
_RadioLom_Object = MibTableColumn
radioLom = _RadioLom_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 13, 1, 7),
    _RadioLom_Type()
)
radioLom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioLom.setStatus("current")


class _RadioXpic_Type(Integer32):
    """Custom type radioXpic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RadioXpic_Type.__name__ = "Integer32"
_RadioXpic_Object = MibTableColumn
radioXpic = _RadioXpic_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 13, 1, 8),
    _RadioXpic_Type()
)
radioXpic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioXpic.setStatus("current")
_RadioFrequencyTable_Object = MibTable
radioFrequencyTable = _RadioFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 14)
)
if mibBuilder.loadTexts:
    radioFrequencyTable.setStatus("current")
_RadioFreqTabEntry_Object = MibTableRow
radioFreqTabEntry = _RadioFreqTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 14, 1)
)
radioFreqTabEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioFreqChannelId"),
)
if mibBuilder.loadTexts:
    radioFreqTabEntry.setStatus("current")
_RadioFreqChannelId_Type = Integer32
_RadioFreqChannelId_Object = MibTableColumn
radioFreqChannelId = _RadioFreqChannelId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 14, 1, 1),
    _RadioFreqChannelId_Type()
)
radioFreqChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioFreqChannelId.setStatus("current")
_RadioFreqChannelNum_Type = Integer32
_RadioFreqChannelNum_Object = MibTableColumn
radioFreqChannelNum = _RadioFreqChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 14, 1, 2),
    _RadioFreqChannelNum_Type()
)
radioFreqChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioFreqChannelNum.setStatus("current")
_RadioFreqValue_Type = Integer32
_RadioFreqValue_Object = MibTableColumn
radioFreqValue = _RadioFreqValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 14, 1, 3),
    _RadioFreqValue_Type()
)
radioFreqValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioFreqValue.setStatus("current")
_RadioDuplexFrequencyTable_Object = MibTable
radioDuplexFrequencyTable = _RadioDuplexFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 15)
)
if mibBuilder.loadTexts:
    radioDuplexFrequencyTable.setStatus("current")
_RadioDuplexFreqEntry_Object = MibTableRow
radioDuplexFreqEntry = _RadioDuplexFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 15, 1)
)
radioDuplexFreqEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioDuplexFreqId"),
)
if mibBuilder.loadTexts:
    radioDuplexFreqEntry.setStatus("current")
_RadioDuplexFreqId_Type = Integer32
_RadioDuplexFreqId_Object = MibTableColumn
radioDuplexFreqId = _RadioDuplexFreqId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 15, 1, 1),
    _RadioDuplexFreqId_Type()
)
radioDuplexFreqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioDuplexFreqId.setStatus("current")
_RadioDuplexFreqValue_Type = Integer32
_RadioDuplexFreqValue_Object = MibTableColumn
radioDuplexFreqValue = _RadioDuplexFreqValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 15, 1, 2),
    _RadioDuplexFreqValue_Type()
)
radioDuplexFreqValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioDuplexFreqValue.setStatus("current")
_RadioModulationTable_Object = MibTable
radioModulationTable = _RadioModulationTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 16)
)
if mibBuilder.loadTexts:
    radioModulationTable.setStatus("current")
_RadioModulationEntry_Object = MibTableRow
radioModulationEntry = _RadioModulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 16, 1)
)
radioModulationEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioChannelSpacing"),
)
if mibBuilder.loadTexts:
    radioModulationEntry.setStatus("current")
_RadioChannelSpacing_Type = ChannelSpacing
_RadioChannelSpacing_Object = MibTableColumn
radioChannelSpacing = _RadioChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 16, 1, 1),
    _RadioChannelSpacing_Type()
)
radioChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioChannelSpacing.setStatus("current")
_RadioModulationMap_Type = ModulationMap
_RadioModulationMap_Object = MibTableColumn
radioModulationMap = _RadioModulationMap_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 16, 1, 2),
    _RadioModulationMap_Type()
)
radioModulationMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioModulationMap.setStatus("current")
_RadioRefModulationMap_Type = ModulationMap
_RadioRefModulationMap_Object = MibTableColumn
radioRefModulationMap = _RadioRefModulationMap_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 16, 1, 3),
    _RadioRefModulationMap_Type()
)
radioRefModulationMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRefModulationMap.setStatus("current")
_LinkStatusTable_Object = MibTable
linkStatusTable = _LinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17)
)
if mibBuilder.loadTexts:
    linkStatusTable.setStatus("current")
_LinkStatusEntry_Object = MibTableRow
linkStatusEntry = _LinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1)
)
linkStatusEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkPolIndex"),
)
if mibBuilder.loadTexts:
    linkStatusEntry.setStatus("current")


class _LinkPolIndex_Type(Integer32):
    """Custom type linkPolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_LinkPolIndex_Type.__name__ = "Integer32"
_LinkPolIndex_Object = MibTableColumn
linkPolIndex = _LinkPolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 1),
    _LinkPolIndex_Type()
)
linkPolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPolIndex.setStatus("current")
_LinkAcmRxProfile_Type = Integer32
_LinkAcmRxProfile_Object = MibTableColumn
linkAcmRxProfile = _LinkAcmRxProfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 2),
    _LinkAcmRxProfile_Type()
)
linkAcmRxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmRxProfile.setStatus("current")
_LinkAcmTxProfile_Type = Integer32
_LinkAcmTxProfile_Object = MibTableColumn
linkAcmTxProfile = _LinkAcmTxProfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 3),
    _LinkAcmTxProfile_Type()
)
linkAcmTxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmTxProfile.setStatus("current")


class _LinkAcmRxProfileLabel_Type(DisplayString):
    """Custom type linkAcmRxProfileLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LinkAcmRxProfileLabel_Type.__name__ = "DisplayString"
_LinkAcmRxProfileLabel_Object = MibTableColumn
linkAcmRxProfileLabel = _LinkAcmRxProfileLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 4),
    _LinkAcmRxProfileLabel_Type()
)
linkAcmRxProfileLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmRxProfileLabel.setStatus("current")


class _LinkAcmTxProfileLabel_Type(DisplayString):
    """Custom type linkAcmTxProfileLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LinkAcmTxProfileLabel_Type.__name__ = "DisplayString"
_LinkAcmTxProfileLabel_Object = MibTableColumn
linkAcmTxProfileLabel = _LinkAcmTxProfileLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 5),
    _LinkAcmTxProfileLabel_Type()
)
linkAcmTxProfileLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmTxProfileLabel.setStatus("current")
_LinkAcmRxModulation_Type = BitsPerSymbol
_LinkAcmRxModulation_Object = MibTableColumn
linkAcmRxModulation = _LinkAcmRxModulation_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 6),
    _LinkAcmRxModulation_Type()
)
linkAcmRxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmRxModulation.setStatus("current")
_LinkAcmTxModulation_Type = BitsPerSymbol
_LinkAcmTxModulation_Object = MibTableColumn
linkAcmTxModulation = _LinkAcmTxModulation_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 7),
    _LinkAcmTxModulation_Type()
)
linkAcmTxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmTxModulation.setStatus("current")


class _LinkAcmRxCode_Type(Integer32):
    """Custom type linkAcmRxCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("normal", 1),
          ("strong", 2))
    )


_LinkAcmRxCode_Type.__name__ = "Integer32"
_LinkAcmRxCode_Object = MibTableColumn
linkAcmRxCode = _LinkAcmRxCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 8),
    _LinkAcmRxCode_Type()
)
linkAcmRxCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmRxCode.setStatus("current")


class _LinkAcmTxCode_Type(Integer32):
    """Custom type linkAcmTxCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("normal", 1),
          ("strong", 2))
    )


_LinkAcmTxCode_Type.__name__ = "Integer32"
_LinkAcmTxCode_Object = MibTableColumn
linkAcmTxCode = _LinkAcmTxCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 9),
    _LinkAcmTxCode_Type()
)
linkAcmTxCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmTxCode.setStatus("current")


class _LinkTxETHCapacity_Type(Integer32):
    """Custom type linkTxETHCapacity based on Integer32"""
    defaultValue = 0


_LinkTxETHCapacity_Type.__name__ = "Integer32"
_LinkTxETHCapacity_Object = MibTableColumn
linkTxETHCapacity = _LinkTxETHCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 10),
    _LinkTxETHCapacity_Type()
)
linkTxETHCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTxETHCapacity.setStatus("current")


class _LinkRxETHCapacity_Type(Integer32):
    """Custom type linkRxETHCapacity based on Integer32"""
    defaultValue = 0


_LinkRxETHCapacity_Type.__name__ = "Integer32"
_LinkRxETHCapacity_Object = MibTableColumn
linkRxETHCapacity = _LinkRxETHCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 11),
    _LinkRxETHCapacity_Type()
)
linkRxETHCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRxETHCapacity.setStatus("current")


class _LinkTxTDMCapacity_Type(Integer32):
    """Custom type linkTxTDMCapacity based on Integer32"""
    defaultValue = 0


_LinkTxTDMCapacity_Type.__name__ = "Integer32"
_LinkTxTDMCapacity_Object = MibTableColumn
linkTxTDMCapacity = _LinkTxTDMCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 12),
    _LinkTxTDMCapacity_Type()
)
linkTxTDMCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTxTDMCapacity.setStatus("current")


class _LinkRxTDMCapacity_Type(Integer32):
    """Custom type linkRxTDMCapacity based on Integer32"""
    defaultValue = 0


_LinkRxTDMCapacity_Type.__name__ = "Integer32"
_LinkRxTDMCapacity_Object = MibTableColumn
linkRxTDMCapacity = _LinkRxTDMCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 13),
    _LinkRxTDMCapacity_Type()
)
linkRxTDMCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRxTDMCapacity.setStatus("current")


class _LinkRescueModulation_Type(BitsPerSymbol):
    """Custom type linkRescueModulation based on BitsPerSymbol"""
    defaultValue = 2


_LinkRescueModulation_Type.__name__ = "BitsPerSymbol"
_LinkRescueModulation_Object = MibTableColumn
linkRescueModulation = _LinkRescueModulation_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 14),
    _LinkRescueModulation_Type()
)
linkRescueModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRescueModulation.setStatus("current")
_LinkReducedCapacityAlarm_Type = AlarmStatus
_LinkReducedCapacityAlarm_Object = MibTableColumn
linkReducedCapacityAlarm = _LinkReducedCapacityAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 15),
    _LinkReducedCapacityAlarm_Type()
)
linkReducedCapacityAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkReducedCapacityAlarm.setStatus("current")
_LinkLinkTelemetryFailAlarm_Type = AlarmStatus
_LinkLinkTelemetryFailAlarm_Object = MibTableColumn
linkLinkTelemetryFailAlarm = _LinkLinkTelemetryFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 16),
    _LinkLinkTelemetryFailAlarm_Type()
)
linkLinkTelemetryFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLinkTelemetryFailAlarm.setStatus("current")
_LinkIdMismatchAlarm_Type = AlarmStatus
_LinkIdMismatchAlarm_Object = MibTableColumn
linkIdMismatchAlarm = _LinkIdMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 17),
    _LinkIdMismatchAlarm_Type()
)
linkIdMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkIdMismatchAlarm.setStatus("current")
_LinkRadioEocAlarm_Type = AlarmStatus
_LinkRadioEocAlarm_Object = MibTableColumn
linkRadioEocAlarm = _LinkRadioEocAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 18),
    _LinkRadioEocAlarm_Type()
)
linkRadioEocAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRadioEocAlarm.setStatus("current")
_LinkSetupMismatchAlarm_Type = AlarmStatus
_LinkSetupMismatchAlarm_Object = MibTableColumn
linkSetupMismatchAlarm = _LinkSetupMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 19),
    _LinkSetupMismatchAlarm_Type()
)
linkSetupMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSetupMismatchAlarm.setStatus("current")
_LinkRescueSetupAlarm_Type = AlarmStatus
_LinkRescueSetupAlarm_Object = MibTableColumn
linkRescueSetupAlarm = _LinkRescueSetupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 20),
    _LinkRescueSetupAlarm_Type()
)
linkRescueSetupAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRescueSetupAlarm.setStatus("current")
_LinkXpicProcedureBlockAlarm_Type = AlarmStatus
_LinkXpicProcedureBlockAlarm_Object = MibTableColumn
linkXpicProcedureBlockAlarm = _LinkXpicProcedureBlockAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 21),
    _LinkXpicProcedureBlockAlarm_Type()
)
linkXpicProcedureBlockAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkXpicProcedureBlockAlarm.setStatus("current")
_LinkXpicRemTxOffAlarm_Type = AlarmStatus
_LinkXpicRemTxOffAlarm_Object = MibTableColumn
linkXpicRemTxOffAlarm = _LinkXpicRemTxOffAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 22),
    _LinkXpicRemTxOffAlarm_Type()
)
linkXpicRemTxOffAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkXpicRemTxOffAlarm.setStatus("current")
_LinkRemoteIduAlarmSynthesis_Type = AlarmStatus
_LinkRemoteIduAlarmSynthesis_Object = MibTableColumn
linkRemoteIduAlarmSynthesis = _LinkRemoteIduAlarmSynthesis_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 23),
    _LinkRemoteIduAlarmSynthesis_Type()
)
linkRemoteIduAlarmSynthesis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRemoteIduAlarmSynthesis.setStatus("current")
_LinkNotMatchingRadiosAlarm_Type = AlarmStatus
_LinkNotMatchingRadiosAlarm_Object = MibTableColumn
linkNotMatchingRadiosAlarm = _LinkNotMatchingRadiosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 24),
    _LinkNotMatchingRadiosAlarm_Type()
)
linkNotMatchingRadiosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNotMatchingRadiosAlarm.setStatus("current")


class _LinkConfigurationInProgress_Type(Integer32):
    """Custom type linkConfigurationInProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("active", 2))
    )


_LinkConfigurationInProgress_Type.__name__ = "Integer32"
_LinkConfigurationInProgress_Object = MibTableColumn
linkConfigurationInProgress = _LinkConfigurationInProgress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 25),
    _LinkConfigurationInProgress_Type()
)
linkConfigurationInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkConfigurationInProgress.setStatus("current")
_LinkXpd_Type = Integer32
_LinkXpd_Object = MibTableColumn
linkXpd = _LinkXpd_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 17, 1, 26),
    _LinkXpd_Type()
)
linkXpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkXpd.setStatus("deprecated")
_LinkTfcTable_Object = MibTable
linkTfcTable = _LinkTfcTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 18)
)
if mibBuilder.loadTexts:
    linkTfcTable.setStatus("deprecated")
_LinkTfcEntry_Object = MibTableRow
linkTfcEntry = _LinkTfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 18, 1)
)
linkTfcEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
)
if mibBuilder.loadTexts:
    linkTfcEntry.setStatus("deprecated")


class _LinkTfcAction_Type(Integer32):
    """Custom type linkTfcAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("reset", 1))
    )


_LinkTfcAction_Type.__name__ = "Integer32"
_LinkTfcAction_Object = MibTableColumn
linkTfcAction = _LinkTfcAction_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 18, 1, 1),
    _LinkTfcAction_Type()
)
linkTfcAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkTfcAction.setStatus("deprecated")


class _LinkTfcControl_Type(Integer32):
    """Custom type linkTfcControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkTfcControl_Type.__name__ = "Integer32"
_LinkTfcControl_Object = MibTableColumn
linkTfcControl = _LinkTfcControl_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 18, 1, 2),
    _LinkTfcControl_Type()
)
linkTfcControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkTfcControl.setStatus("deprecated")


class _LinkTfcWatchWindow_Type(Integer32):
    """Custom type linkTfcWatchWindow based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_LinkTfcWatchWindow_Type.__name__ = "Integer32"
_LinkTfcWatchWindow_Object = MibTableColumn
linkTfcWatchWindow = _LinkTfcWatchWindow_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 18, 1, 3),
    _LinkTfcWatchWindow_Type()
)
linkTfcWatchWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkTfcWatchWindow.setStatus("deprecated")


class _LinkTfcAlarmThreshold_Type(Integer32):
    """Custom type linkTfcAlarmThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_LinkTfcAlarmThreshold_Type.__name__ = "Integer32"
_LinkTfcAlarmThreshold_Object = MibTableColumn
linkTfcAlarmThreshold = _LinkTfcAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 18, 1, 4),
    _LinkTfcAlarmThreshold_Type()
)
linkTfcAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkTfcAlarmThreshold.setStatus("deprecated")
_LinkTfcAlarm_Type = AlarmStatus
_LinkTfcAlarm_Object = MibTableColumn
linkTfcAlarm = _LinkTfcAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 18, 1, 5),
    _LinkTfcAlarm_Type()
)
linkTfcAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTfcAlarm.setStatus("deprecated")
_LinkTfcRowStatus_Type = RowStatus
_LinkTfcRowStatus_Object = MibTableColumn
linkTfcRowStatus = _LinkTfcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 18, 1, 6),
    _LinkTfcRowStatus_Type()
)
linkTfcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkTfcRowStatus.setStatus("deprecated")
_LinkMaintTable_Object = MibTable
linkMaintTable = _LinkMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 19)
)
if mibBuilder.loadTexts:
    linkMaintTable.setStatus("current")
_LinkMaintEntry_Object = MibTableRow
linkMaintEntry = _LinkMaintEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 19, 1)
)
linkMaintEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkPolIndex"),
)
if mibBuilder.loadTexts:
    linkMaintEntry.setStatus("current")


class _LinkBerStart_Type(Integer32):
    """Custom type linkBerStart based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restart", 1),
          ("stop", 2))
    )


_LinkBerStart_Type.__name__ = "Integer32"
_LinkBerStart_Object = MibTableColumn
linkBerStart = _LinkBerStart_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 19, 1, 1),
    _LinkBerStart_Type()
)
linkBerStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkBerStart.setStatus("current")


class _LinkBaseBandLom_Type(Integer32):
    """Custom type linkBaseBandLom based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkBaseBandLom_Type.__name__ = "Integer32"
_LinkBaseBandLom_Object = MibTableColumn
linkBaseBandLom = _LinkBaseBandLom_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 19, 1, 2),
    _LinkBaseBandLom_Type()
)
linkBaseBandLom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkBaseBandLom.setStatus("current")


class _LinkFadeMarginMeasure_Type(Integer32):
    """Custom type linkFadeMarginMeasure based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkFadeMarginMeasure_Type.__name__ = "Integer32"
_LinkFadeMarginMeasure_Object = MibTableColumn
linkFadeMarginMeasure = _LinkFadeMarginMeasure_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 19, 1, 3),
    _LinkFadeMarginMeasure_Type()
)
linkFadeMarginMeasure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkFadeMarginMeasure.setStatus("deprecated")


class _LinkXpicControlProcedureReset_Type(Integer32):
    """Custom type linkXpicControlProcedureReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("reset", 1))
    )


_LinkXpicControlProcedureReset_Type.__name__ = "Integer32"
_LinkXpicControlProcedureReset_Object = MibTableColumn
linkXpicControlProcedureReset = _LinkXpicControlProcedureReset_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 19, 1, 4),
    _LinkXpicControlProcedureReset_Type()
)
linkXpicControlProcedureReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkXpicControlProcedureReset.setStatus("current")
_LinkBerTable_Object = MibTable
linkBerTable = _LinkBerTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 20)
)
if mibBuilder.loadTexts:
    linkBerTable.setStatus("current")
_LinkBerEntry_Object = MibTableRow
linkBerEntry = _LinkBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 20, 1)
)
linkBerEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkPolIndex"),
)
if mibBuilder.loadTexts:
    linkBerEntry.setStatus("current")
_LinkBerErrorCounterH_Type = Counter32
_LinkBerErrorCounterH_Object = MibTableColumn
linkBerErrorCounterH = _LinkBerErrorCounterH_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 20, 1, 1),
    _LinkBerErrorCounterH_Type()
)
linkBerErrorCounterH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkBerErrorCounterH.setStatus("current")
_LinkBerErrorCounterL_Type = Counter32
_LinkBerErrorCounterL_Object = MibTableColumn
linkBerErrorCounterL = _LinkBerErrorCounterL_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 20, 1, 2),
    _LinkBerErrorCounterL_Type()
)
linkBerErrorCounterL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkBerErrorCounterL.setStatus("current")
_LinkBerDataCounterH_Type = Counter32
_LinkBerDataCounterH_Object = MibTableColumn
linkBerDataCounterH = _LinkBerDataCounterH_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 20, 1, 3),
    _LinkBerDataCounterH_Type()
)
linkBerDataCounterH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkBerDataCounterH.setStatus("current")
_LinkBerDataCounterL_Type = Counter32
_LinkBerDataCounterL_Object = MibTableColumn
linkBerDataCounterL = _LinkBerDataCounterL_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 20, 1, 4),
    _LinkBerDataCounterL_Type()
)
linkBerDataCounterL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkBerDataCounterL.setStatus("current")
_LinkBerSyncLossAlarm_Type = AlarmStatus
_LinkBerSyncLossAlarm_Object = MibTableColumn
linkBerSyncLossAlarm = _LinkBerSyncLossAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 20, 1, 5),
    _LinkBerSyncLossAlarm_Type()
)
linkBerSyncLossAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkBerSyncLossAlarm.setStatus("current")
_LinkBerSyncLossAlarmCounter_Type = Integer32
_LinkBerSyncLossAlarmCounter_Object = MibTableColumn
linkBerSyncLossAlarmCounter = _LinkBerSyncLossAlarmCounter_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 20, 1, 6),
    _LinkBerSyncLossAlarmCounter_Type()
)
linkBerSyncLossAlarmCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkBerSyncLossAlarmCounter.setStatus("current")
_LinkBerElapsedTime_Type = Integer32
_LinkBerElapsedTime_Object = MibTableColumn
linkBerElapsedTime = _LinkBerElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 20, 1, 7),
    _LinkBerElapsedTime_Type()
)
linkBerElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkBerElapsedTime.setStatus("current")
_LinkAcmTable_Object = MibTable
linkAcmTable = _LinkAcmTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21)
)
if mibBuilder.loadTexts:
    linkAcmTable.setStatus("current")
_LinkAcmEntry_Object = MibTableRow
linkAcmEntry = _LinkAcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1)
)
linkAcmEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkPolIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkAcmProfileId"),
)
if mibBuilder.loadTexts:
    linkAcmEntry.setStatus("current")
_LinkAcmProfileId_Type = Integer32
_LinkAcmProfileId_Object = MibTableColumn
linkAcmProfileId = _LinkAcmProfileId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 1),
    _LinkAcmProfileId_Type()
)
linkAcmProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmProfileId.setStatus("current")
_LinkAcmProfileModulation_Type = BitsPerSymbol
_LinkAcmProfileModulation_Object = MibTableColumn
linkAcmProfileModulation = _LinkAcmProfileModulation_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 2),
    _LinkAcmProfileModulation_Type()
)
linkAcmProfileModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmProfileModulation.setStatus("current")


class _LinkAcmProfileCode_Type(Integer32):
    """Custom type linkAcmProfileCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("strong", 2))
    )


_LinkAcmProfileCode_Type.__name__ = "Integer32"
_LinkAcmProfileCode_Object = MibTableColumn
linkAcmProfileCode = _LinkAcmProfileCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 3),
    _LinkAcmProfileCode_Type()
)
linkAcmProfileCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmProfileCode.setStatus("current")
_LinkAcmProfileCapacity_Type = Integer32
_LinkAcmProfileCapacity_Object = MibTableColumn
linkAcmProfileCapacity = _LinkAcmProfileCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 4),
    _LinkAcmProfileCapacity_Type()
)
linkAcmProfileCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmProfileCapacity.setStatus("current")


class _LinkAcmProfileLabel_Type(DisplayString):
    """Custom type linkAcmProfileLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LinkAcmProfileLabel_Type.__name__ = "DisplayString"
_LinkAcmProfileLabel_Object = MibTableColumn
linkAcmProfileLabel = _LinkAcmProfileLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 5),
    _LinkAcmProfileLabel_Type()
)
linkAcmProfileLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkAcmProfileLabel.setStatus("current")


class _LinkAcmProfileEnable_Type(Integer32):
    """Custom type linkAcmProfileEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkAcmProfileEnable_Type.__name__ = "Integer32"
_LinkAcmProfileEnable_Object = MibTableColumn
linkAcmProfileEnable = _LinkAcmProfileEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 6),
    _LinkAcmProfileEnable_Type()
)
linkAcmProfileEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmProfileEnable.setStatus("current")


class _LinkAcmMaxTDMCapacity_Type(Integer32):
    """Custom type linkAcmMaxTDMCapacity based on Integer32"""
    defaultValue = 0


_LinkAcmMaxTDMCapacity_Type.__name__ = "Integer32"
_LinkAcmMaxTDMCapacity_Object = MibTableColumn
linkAcmMaxTDMCapacity = _LinkAcmMaxTDMCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 7),
    _LinkAcmMaxTDMCapacity_Type()
)
linkAcmMaxTDMCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmMaxTDMCapacity.setStatus("deprecated")
_LinkAcmPowerScaling_Type = Integer32
_LinkAcmPowerScaling_Object = MibTableColumn
linkAcmPowerScaling = _LinkAcmPowerScaling_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 8),
    _LinkAcmPowerScaling_Type()
)
linkAcmPowerScaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmPowerScaling.setStatus("deprecated")
_LinkAcmDownshiftThreshold_Type = Integer32
_LinkAcmDownshiftThreshold_Object = MibTableColumn
linkAcmDownshiftThreshold = _LinkAcmDownshiftThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 9),
    _LinkAcmDownshiftThreshold_Type()
)
linkAcmDownshiftThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmDownshiftThreshold.setStatus("current")
_LinkAcmUpshiftThreshold_Type = Integer32
_LinkAcmUpshiftThreshold_Object = MibTableColumn
linkAcmUpshiftThreshold = _LinkAcmUpshiftThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 10),
    _LinkAcmUpshiftThreshold_Type()
)
linkAcmUpshiftThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmUpshiftThreshold.setStatus("current")


class _LinkAcmActiveProfile_Type(Integer32):
    """Custom type linkAcmActiveProfile based on Integer32"""
    defaultValue = 1

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
        *(("cleared", 1),
          ("activeRx", 2),
          ("activeTx", 3),
          ("activeBoth", 4))
    )


_LinkAcmActiveProfile_Type.__name__ = "Integer32"
_LinkAcmActiveProfile_Object = MibTableColumn
linkAcmActiveProfile = _LinkAcmActiveProfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 11),
    _LinkAcmActiveProfile_Type()
)
linkAcmActiveProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmActiveProfile.setStatus("current")
_LinkAcmTDMCapacity_Type = Integer32
_LinkAcmTDMCapacity_Object = MibTableColumn
linkAcmTDMCapacity = _LinkAcmTDMCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 12),
    _LinkAcmTDMCapacity_Type()
)
linkAcmTDMCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmTDMCapacity.setStatus("current")
_LinkAcmETHCapacity_Type = Integer32
_LinkAcmETHCapacity_Object = MibTableColumn
linkAcmETHCapacity = _LinkAcmETHCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 13),
    _LinkAcmETHCapacity_Type()
)
linkAcmETHCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmETHCapacity.setStatus("current")
_LinkAcmAtpcRxPowerScaling_Type = Integer32
_LinkAcmAtpcRxPowerScaling_Object = MibTableColumn
linkAcmAtpcRxPowerScaling = _LinkAcmAtpcRxPowerScaling_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 14),
    _LinkAcmAtpcRxPowerScaling_Type()
)
linkAcmAtpcRxPowerScaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmAtpcRxPowerScaling.setStatus("deprecated")
_LinkAcmPowerRange_Type = Integer32
_LinkAcmPowerRange_Object = MibTableColumn
linkAcmPowerRange = _LinkAcmPowerRange_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 21, 1, 15),
    _LinkAcmPowerRange_Type()
)
linkAcmPowerRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAcmPowerRange.setStatus("deprecated")
_LinkProTable_Object = MibTable
linkProTable = _LinkProTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 22)
)
if mibBuilder.loadTexts:
    linkProTable.setStatus("deprecated")
_LinkProEntry_Object = MibTableRow
linkProEntry = _LinkProEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 22, 1)
)
linkProEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
)
if mibBuilder.loadTexts:
    linkProEntry.setStatus("deprecated")


class _LinkProProtectionTxChIdx_Type(Integer32):
    """Custom type linkProProtectionTxChIdx based on Integer32"""
    defaultValue = 0


_LinkProProtectionTxChIdx_Type.__name__ = "Integer32"
_LinkProProtectionTxChIdx_Object = MibTableColumn
linkProProtectionTxChIdx = _LinkProProtectionTxChIdx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 22, 1, 1),
    _LinkProProtectionTxChIdx_Type()
)
linkProProtectionTxChIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProProtectionTxChIdx.setStatus("deprecated")


class _LinkProProtectionRxChIdx_Type(Integer32):
    """Custom type linkProProtectionRxChIdx based on Integer32"""
    defaultValue = 0


_LinkProProtectionRxChIdx_Type.__name__ = "Integer32"
_LinkProProtectionRxChIdx_Object = MibTableColumn
linkProProtectionRxChIdx = _LinkProProtectionRxChIdx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 22, 1, 2),
    _LinkProProtectionRxChIdx_Type()
)
linkProProtectionRxChIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProProtectionRxChIdx.setStatus("deprecated")


class _LinkProTxWtrTime_Type(Integer32):
    """Custom type linkProTxWtrTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_LinkProTxWtrTime_Type.__name__ = "Integer32"
_LinkProTxWtrTime_Object = MibTableColumn
linkProTxWtrTime = _LinkProTxWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 22, 1, 3),
    _LinkProTxWtrTime_Type()
)
linkProTxWtrTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProTxWtrTime.setStatus("deprecated")


class _LinkProRxWtrTime_Type(Integer32):
    """Custom type linkProRxWtrTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_LinkProRxWtrTime_Type.__name__ = "Integer32"
_LinkProRxWtrTime_Object = MibTableColumn
linkProRxWtrTime = _LinkProRxWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 22, 1, 4),
    _LinkProRxWtrTime_Type()
)
linkProRxWtrTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProRxWtrTime.setStatus("deprecated")


class _LinkProTxSwitchedChIdx_Type(Integer32):
    """Custom type linkProTxSwitchedChIdx based on Integer32"""
    defaultValue = 0


_LinkProTxSwitchedChIdx_Type.__name__ = "Integer32"
_LinkProTxSwitchedChIdx_Object = MibTableColumn
linkProTxSwitchedChIdx = _LinkProTxSwitchedChIdx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 22, 1, 5),
    _LinkProTxSwitchedChIdx_Type()
)
linkProTxSwitchedChIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkProTxSwitchedChIdx.setStatus("deprecated")


class _LinkProRxSwitchedChIdx_Type(Integer32):
    """Custom type linkProRxSwitchedChIdx based on Integer32"""
    defaultValue = 0


_LinkProRxSwitchedChIdx_Type.__name__ = "Integer32"
_LinkProRxSwitchedChIdx_Object = MibTableColumn
linkProRxSwitchedChIdx = _LinkProRxSwitchedChIdx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 22, 1, 6),
    _LinkProRxSwitchedChIdx_Type()
)
linkProRxSwitchedChIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkProRxSwitchedChIdx.setStatus("deprecated")


class _LinkProTxRevertive_Type(Integer32):
    """Custom type linkProTxRevertive based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkProTxRevertive_Type.__name__ = "Integer32"
_LinkProTxRevertive_Object = MibTableColumn
linkProTxRevertive = _LinkProTxRevertive_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 22, 1, 7),
    _LinkProTxRevertive_Type()
)
linkProTxRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProTxRevertive.setStatus("deprecated")


class _LinkProRxRevertive_Type(Integer32):
    """Custom type linkProRxRevertive based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkProRxRevertive_Type.__name__ = "Integer32"
_LinkProRxRevertive_Object = MibTableColumn
linkProRxRevertive = _LinkProRxRevertive_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 22, 1, 8),
    _LinkProRxRevertive_Type()
)
linkProRxRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProRxRevertive.setStatus("deprecated")


class _LinkProExtraTraffic_Type(Integer32):
    """Custom type linkProExtraTraffic based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkProExtraTraffic_Type.__name__ = "Integer32"
_LinkProExtraTraffic_Object = MibTableColumn
linkProExtraTraffic = _LinkProExtraTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 22, 1, 9),
    _LinkProExtraTraffic_Type()
)
linkProExtraTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProExtraTraffic.setStatus("deprecated")
_LinkProRowStatus_Type = RowStatus
_LinkProRowStatus_Object = MibTableColumn
linkProRowStatus = _LinkProRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 22, 1, 10),
    _LinkProRowStatus_Type()
)
linkProRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProRowStatus.setStatus("deprecated")
_LinkProMaintTable_Object = MibTable
linkProMaintTable = _LinkProMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 23)
)
if mibBuilder.loadTexts:
    linkProMaintTable.setStatus("deprecated")
_LinkProMaintEntry_Object = MibTableRow
linkProMaintEntry = _LinkProMaintEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 23, 1)
)
linkProMaintEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
)
if mibBuilder.loadTexts:
    linkProMaintEntry.setStatus("deprecated")


class _LinkProMaintTxLockout_Type(Integer32):
    """Custom type linkProMaintTxLockout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkProMaintTxLockout_Type.__name__ = "Integer32"
_LinkProMaintTxLockout_Object = MibTableColumn
linkProMaintTxLockout = _LinkProMaintTxLockout_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 23, 1, 1),
    _LinkProMaintTxLockout_Type()
)
linkProMaintTxLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkProMaintTxLockout.setStatus("deprecated")


class _LinkProMaintRxLockout_Type(Integer32):
    """Custom type linkProMaintRxLockout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkProMaintRxLockout_Type.__name__ = "Integer32"
_LinkProMaintRxLockout_Object = MibTableColumn
linkProMaintRxLockout = _LinkProMaintRxLockout_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 23, 1, 2),
    _LinkProMaintRxLockout_Type()
)
linkProMaintRxLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkProMaintRxLockout.setStatus("deprecated")


class _LinkProMaintTxForced_Type(Integer32):
    """Custom type linkProMaintTxForced based on Integer32"""
    defaultValue = 0


_LinkProMaintTxForced_Type.__name__ = "Integer32"
_LinkProMaintTxForced_Object = MibTableColumn
linkProMaintTxForced = _LinkProMaintTxForced_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 23, 1, 3),
    _LinkProMaintTxForced_Type()
)
linkProMaintTxForced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkProMaintTxForced.setStatus("deprecated")


class _LinkProMaintRxForced_Type(Integer32):
    """Custom type linkProMaintRxForced based on Integer32"""
    defaultValue = 0


_LinkProMaintRxForced_Type.__name__ = "Integer32"
_LinkProMaintRxForced_Object = MibTableColumn
linkProMaintRxForced = _LinkProMaintRxForced_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 23, 1, 4),
    _LinkProMaintRxForced_Type()
)
linkProMaintRxForced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkProMaintRxForced.setStatus("deprecated")


class _LinkProMaintTxWtrReset_Type(Integer32):
    """Custom type linkProMaintTxWtrReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("on", 2))
    )


_LinkProMaintTxWtrReset_Type.__name__ = "Integer32"
_LinkProMaintTxWtrReset_Object = MibTableColumn
linkProMaintTxWtrReset = _LinkProMaintTxWtrReset_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 23, 1, 5),
    _LinkProMaintTxWtrReset_Type()
)
linkProMaintTxWtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkProMaintTxWtrReset.setStatus("deprecated")


class _LinkProMaintRxWtrReset_Type(Integer32):
    """Custom type linkProMaintRxWtrReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("on", 2))
    )


_LinkProMaintRxWtrReset_Type.__name__ = "Integer32"
_LinkProMaintRxWtrReset_Object = MibTableColumn
linkProMaintRxWtrReset = _LinkProMaintRxWtrReset_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 23, 1, 6),
    _LinkProMaintRxWtrReset_Type()
)
linkProMaintRxWtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkProMaintRxWtrReset.setStatus("deprecated")
_LinkCapabilitiesTable_Object = MibTable
linkCapabilitiesTable = _LinkCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 24)
)
if mibBuilder.loadTexts:
    linkCapabilitiesTable.setStatus("deprecated")
_LinkCapabilitiesEntry_Object = MibTableRow
linkCapabilitiesEntry = _LinkCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 24, 1)
)
linkCapabilitiesEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
)
if mibBuilder.loadTexts:
    linkCapabilitiesEntry.setStatus("deprecated")
_LinkCapabilitiesCapability_Type = RadioCapability
_LinkCapabilitiesCapability_Object = MibTableColumn
linkCapabilitiesCapability = _LinkCapabilitiesCapability_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 24, 1, 1),
    _LinkCapabilitiesCapability_Type()
)
linkCapabilitiesCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapabilitiesCapability.setStatus("deprecated")
_LinkCapabilitiesTxMinFrequency_Type = Integer32
_LinkCapabilitiesTxMinFrequency_Object = MibTableColumn
linkCapabilitiesTxMinFrequency = _LinkCapabilitiesTxMinFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 24, 1, 2),
    _LinkCapabilitiesTxMinFrequency_Type()
)
linkCapabilitiesTxMinFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapabilitiesTxMinFrequency.setStatus("deprecated")
_LinkCapabilitiesTxMaxFrequency_Type = Integer32
_LinkCapabilitiesTxMaxFrequency_Object = MibTableColumn
linkCapabilitiesTxMaxFrequency = _LinkCapabilitiesTxMaxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 24, 1, 3),
    _LinkCapabilitiesTxMaxFrequency_Type()
)
linkCapabilitiesTxMaxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapabilitiesTxMaxFrequency.setStatus("deprecated")
_LinkCapabilitiesStepFrequency_Type = Integer32
_LinkCapabilitiesStepFrequency_Object = MibTableColumn
linkCapabilitiesStepFrequency = _LinkCapabilitiesStepFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 24, 1, 4),
    _LinkCapabilitiesStepFrequency_Type()
)
linkCapabilitiesStepFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapabilitiesStepFrequency.setStatus("deprecated")
_LinkCapabilitiesMinPtxNominalValue_Type = Integer32
_LinkCapabilitiesMinPtxNominalValue_Object = MibTableColumn
linkCapabilitiesMinPtxNominalValue = _LinkCapabilitiesMinPtxNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 24, 1, 5),
    _LinkCapabilitiesMinPtxNominalValue_Type()
)
linkCapabilitiesMinPtxNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapabilitiesMinPtxNominalValue.setStatus("deprecated")
_LinkCapabilitiesMaxPtxNominalValue_Type = Integer32
_LinkCapabilitiesMaxPtxNominalValue_Object = MibTableColumn
linkCapabilitiesMaxPtxNominalValue = _LinkCapabilitiesMaxPtxNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 24, 1, 6),
    _LinkCapabilitiesMaxPtxNominalValue_Type()
)
linkCapabilitiesMaxPtxNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapabilitiesMaxPtxNominalValue.setStatus("deprecated")
_LinkCapabilitiesExtendedMinPwr_Type = Integer32
_LinkCapabilitiesExtendedMinPwr_Object = MibTableColumn
linkCapabilitiesExtendedMinPwr = _LinkCapabilitiesExtendedMinPwr_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 24, 1, 7),
    _LinkCapabilitiesExtendedMinPwr_Type()
)
linkCapabilitiesExtendedMinPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCapabilitiesExtendedMinPwr.setStatus("deprecated")
_LinkFrequencyTable_Object = MibTable
linkFrequencyTable = _LinkFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 25)
)
if mibBuilder.loadTexts:
    linkFrequencyTable.setStatus("deprecated")
_LinkFreqTabEntry_Object = MibTableRow
linkFreqTabEntry = _LinkFreqTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 25, 1)
)
linkFreqTabEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkFreqChannelId"),
)
if mibBuilder.loadTexts:
    linkFreqTabEntry.setStatus("deprecated")
_LinkFreqChannelId_Type = Integer32
_LinkFreqChannelId_Object = MibTableColumn
linkFreqChannelId = _LinkFreqChannelId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 25, 1, 1),
    _LinkFreqChannelId_Type()
)
linkFreqChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFreqChannelId.setStatus("deprecated")
_LinkFreqChannelNum_Type = Integer32
_LinkFreqChannelNum_Object = MibTableColumn
linkFreqChannelNum = _LinkFreqChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 25, 1, 2),
    _LinkFreqChannelNum_Type()
)
linkFreqChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFreqChannelNum.setStatus("deprecated")
_LinkFreqValue_Type = Integer32
_LinkFreqValue_Object = MibTableColumn
linkFreqValue = _LinkFreqValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 25, 1, 3),
    _LinkFreqValue_Type()
)
linkFreqValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFreqValue.setStatus("deprecated")
_LinkDuplexFrequencyTable_Object = MibTable
linkDuplexFrequencyTable = _LinkDuplexFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 26)
)
if mibBuilder.loadTexts:
    linkDuplexFrequencyTable.setStatus("deprecated")
_LinkDuplexFreqEntry_Object = MibTableRow
linkDuplexFreqEntry = _LinkDuplexFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 26, 1)
)
linkDuplexFreqEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkDuplexFreqId"),
)
if mibBuilder.loadTexts:
    linkDuplexFreqEntry.setStatus("deprecated")
_LinkDuplexFreqId_Type = Integer32
_LinkDuplexFreqId_Object = MibTableColumn
linkDuplexFreqId = _LinkDuplexFreqId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 26, 1, 1),
    _LinkDuplexFreqId_Type()
)
linkDuplexFreqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDuplexFreqId.setStatus("deprecated")
_LinkDuplexFreqValue_Type = Integer32
_LinkDuplexFreqValue_Object = MibTableColumn
linkDuplexFreqValue = _LinkDuplexFreqValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 26, 1, 2),
    _LinkDuplexFreqValue_Type()
)
linkDuplexFreqValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDuplexFreqValue.setStatus("deprecated")
_LinkModulationTable_Object = MibTable
linkModulationTable = _LinkModulationTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 27)
)
if mibBuilder.loadTexts:
    linkModulationTable.setStatus("current")
_LinkModulationEntry_Object = MibTableRow
linkModulationEntry = _LinkModulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 27, 1)
)
linkModulationEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkChannelSpacing"),
)
if mibBuilder.loadTexts:
    linkModulationEntry.setStatus("current")
_LinkChannelSpacing_Type = ChannelSpacing
_LinkChannelSpacing_Object = MibTableColumn
linkChannelSpacing = _LinkChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 27, 1, 1),
    _LinkChannelSpacing_Type()
)
linkChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkChannelSpacing.setStatus("current")
_LinkModulationMap_Type = ModulationMap
_LinkModulationMap_Object = MibTableColumn
linkModulationMap = _LinkModulationMap_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 27, 1, 2),
    _LinkModulationMap_Type()
)
linkModulationMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkModulationMap.setStatus("current")
_LinkRefModulationMap_Type = ModulationMap
_LinkRefModulationMap_Object = MibTableColumn
linkRefModulationMap = _LinkRefModulationMap_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 27, 1, 3),
    _LinkRefModulationMap_Type()
)
linkRefModulationMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRefModulationMap.setStatus("current")
_CombinedRadioCapabilitiesTable_Object = MibTable
combinedRadioCapabilitiesTable = _CombinedRadioCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 28)
)
if mibBuilder.loadTexts:
    combinedRadioCapabilitiesTable.setStatus("current")
_CombinedRadioCapabilitiesEntry_Object = MibTableRow
combinedRadioCapabilitiesEntry = _CombinedRadioCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 28, 1)
)
combinedRadioCapabilitiesEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioSettingsIndex"),
)
if mibBuilder.loadTexts:
    combinedRadioCapabilitiesEntry.setStatus("current")
_CombinedRadioCapabilitiesCapability_Type = RadioCapability
_CombinedRadioCapabilitiesCapability_Object = MibTableColumn
combinedRadioCapabilitiesCapability = _CombinedRadioCapabilitiesCapability_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 28, 1, 1),
    _CombinedRadioCapabilitiesCapability_Type()
)
combinedRadioCapabilitiesCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioCapabilitiesCapability.setStatus("current")
_CombinedRadioCapabilitiesTxMinFrequency_Type = Integer32
_CombinedRadioCapabilitiesTxMinFrequency_Object = MibTableColumn
combinedRadioCapabilitiesTxMinFrequency = _CombinedRadioCapabilitiesTxMinFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 28, 1, 2),
    _CombinedRadioCapabilitiesTxMinFrequency_Type()
)
combinedRadioCapabilitiesTxMinFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioCapabilitiesTxMinFrequency.setStatus("current")
_CombinedRadioCapabilitiesTxMaxFrequency_Type = Integer32
_CombinedRadioCapabilitiesTxMaxFrequency_Object = MibTableColumn
combinedRadioCapabilitiesTxMaxFrequency = _CombinedRadioCapabilitiesTxMaxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 28, 1, 3),
    _CombinedRadioCapabilitiesTxMaxFrequency_Type()
)
combinedRadioCapabilitiesTxMaxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioCapabilitiesTxMaxFrequency.setStatus("current")
_CombinedRadioCapabilitiesStepFrequency_Type = Integer32
_CombinedRadioCapabilitiesStepFrequency_Object = MibTableColumn
combinedRadioCapabilitiesStepFrequency = _CombinedRadioCapabilitiesStepFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 28, 1, 4),
    _CombinedRadioCapabilitiesStepFrequency_Type()
)
combinedRadioCapabilitiesStepFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioCapabilitiesStepFrequency.setStatus("current")
_CombinedRadioCapabilitiesMinPtxNominalValue_Type = Integer32
_CombinedRadioCapabilitiesMinPtxNominalValue_Object = MibTableColumn
combinedRadioCapabilitiesMinPtxNominalValue = _CombinedRadioCapabilitiesMinPtxNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 28, 1, 5),
    _CombinedRadioCapabilitiesMinPtxNominalValue_Type()
)
combinedRadioCapabilitiesMinPtxNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioCapabilitiesMinPtxNominalValue.setStatus("current")
_CombinedRadioCapabilitiesMaxPtxNominalValue_Type = Integer32
_CombinedRadioCapabilitiesMaxPtxNominalValue_Object = MibTableColumn
combinedRadioCapabilitiesMaxPtxNominalValue = _CombinedRadioCapabilitiesMaxPtxNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 28, 1, 6),
    _CombinedRadioCapabilitiesMaxPtxNominalValue_Type()
)
combinedRadioCapabilitiesMaxPtxNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioCapabilitiesMaxPtxNominalValue.setStatus("current")
_CombinedRadioCapabilitiesExtendedMinPwr_Type = Integer32
_CombinedRadioCapabilitiesExtendedMinPwr_Object = MibTableColumn
combinedRadioCapabilitiesExtendedMinPwr = _CombinedRadioCapabilitiesExtendedMinPwr_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 28, 1, 7),
    _CombinedRadioCapabilitiesExtendedMinPwr_Type()
)
combinedRadioCapabilitiesExtendedMinPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioCapabilitiesExtendedMinPwr.setStatus("current")
_CombinedRadioFrequencyTable_Object = MibTable
combinedRadioFrequencyTable = _CombinedRadioFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 29)
)
if mibBuilder.loadTexts:
    combinedRadioFrequencyTable.setStatus("current")
_CombinedRadioFreqTabEntry_Object = MibTableRow
combinedRadioFreqTabEntry = _CombinedRadioFreqTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 29, 1)
)
combinedRadioFreqTabEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioSettingsIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "combinedRadioFreqChannelId"),
)
if mibBuilder.loadTexts:
    combinedRadioFreqTabEntry.setStatus("current")
_CombinedRadioFreqChannelId_Type = Integer32
_CombinedRadioFreqChannelId_Object = MibTableColumn
combinedRadioFreqChannelId = _CombinedRadioFreqChannelId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 29, 1, 1),
    _CombinedRadioFreqChannelId_Type()
)
combinedRadioFreqChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioFreqChannelId.setStatus("current")
_CombinedRadioFreqChannelNum_Type = Integer32
_CombinedRadioFreqChannelNum_Object = MibTableColumn
combinedRadioFreqChannelNum = _CombinedRadioFreqChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 29, 1, 2),
    _CombinedRadioFreqChannelNum_Type()
)
combinedRadioFreqChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioFreqChannelNum.setStatus("current")
_CombinedRadioFreqValue_Type = Integer32
_CombinedRadioFreqValue_Object = MibTableColumn
combinedRadioFreqValue = _CombinedRadioFreqValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 29, 1, 3),
    _CombinedRadioFreqValue_Type()
)
combinedRadioFreqValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioFreqValue.setStatus("current")
_CombinedRadioDuplexFrequencyTable_Object = MibTable
combinedRadioDuplexFrequencyTable = _CombinedRadioDuplexFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 30)
)
if mibBuilder.loadTexts:
    combinedRadioDuplexFrequencyTable.setStatus("current")
_CombinedRadioDuplexFreqEntry_Object = MibTableRow
combinedRadioDuplexFreqEntry = _CombinedRadioDuplexFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 30, 1)
)
combinedRadioDuplexFreqEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioSettingsIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "combinedRadioDuplexFreqId"),
)
if mibBuilder.loadTexts:
    combinedRadioDuplexFreqEntry.setStatus("current")
_CombinedRadioDuplexFreqId_Type = Integer32
_CombinedRadioDuplexFreqId_Object = MibTableColumn
combinedRadioDuplexFreqId = _CombinedRadioDuplexFreqId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 30, 1, 1),
    _CombinedRadioDuplexFreqId_Type()
)
combinedRadioDuplexFreqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioDuplexFreqId.setStatus("current")
_CombinedRadioDuplexFreqValue_Type = Integer32
_CombinedRadioDuplexFreqValue_Object = MibTableColumn
combinedRadioDuplexFreqValue = _CombinedRadioDuplexFreqValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 30, 1, 2),
    _CombinedRadioDuplexFreqValue_Type()
)
combinedRadioDuplexFreqValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioDuplexFreqValue.setStatus("current")
_CombinedRadioPowerScalingTable_Object = MibTable
combinedRadioPowerScalingTable = _CombinedRadioPowerScalingTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 31)
)
if mibBuilder.loadTexts:
    combinedRadioPowerScalingTable.setStatus("current")
_CombinedRadioPowerScalingEntry_Object = MibTableRow
combinedRadioPowerScalingEntry = _CombinedRadioPowerScalingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 31, 1)
)
combinedRadioPowerScalingEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioSettingsIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkAcmProfileId"),
)
if mibBuilder.loadTexts:
    combinedRadioPowerScalingEntry.setStatus("current")
_CombinedRadioPowerScaling_Type = Integer32
_CombinedRadioPowerScaling_Object = MibTableColumn
combinedRadioPowerScaling = _CombinedRadioPowerScaling_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 31, 1, 1),
    _CombinedRadioPowerScaling_Type()
)
combinedRadioPowerScaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioPowerScaling.setStatus("current")
_CombinedRadioAtpcRxPowerScaling_Type = Integer32
_CombinedRadioAtpcRxPowerScaling_Object = MibTableColumn
combinedRadioAtpcRxPowerScaling = _CombinedRadioAtpcRxPowerScaling_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 31, 1, 2),
    _CombinedRadioAtpcRxPowerScaling_Type()
)
combinedRadioAtpcRxPowerScaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioAtpcRxPowerScaling.setStatus("current")
_CombinedRadioPowerRange_Type = Integer32
_CombinedRadioPowerRange_Object = MibTableColumn
combinedRadioPowerRange = _CombinedRadioPowerRange_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 31, 1, 3),
    _CombinedRadioPowerRange_Type()
)
combinedRadioPowerRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    combinedRadioPowerRange.setStatus("current")
_Stm1BulkMappingTable_Object = MibTable
stm1BulkMappingTable = _Stm1BulkMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 32)
)
if mibBuilder.loadTexts:
    stm1BulkMappingTable.setStatus("current")
_Stm1BulkMappingEntry_Object = MibTableRow
stm1BulkMappingEntry = _Stm1BulkMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 32, 1)
)
stm1BulkMappingEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "stm1BulkPolIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "stm1BulkChanIndex"),
)
if mibBuilder.loadTexts:
    stm1BulkMappingEntry.setStatus("current")
_Stm1BulkPolIndex_Type = Integer32
_Stm1BulkPolIndex_Object = MibTableColumn
stm1BulkPolIndex = _Stm1BulkPolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 32, 1, 1),
    _Stm1BulkPolIndex_Type()
)
stm1BulkPolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1BulkPolIndex.setStatus("current")
_Stm1BulkChanIndex_Type = Integer32
_Stm1BulkChanIndex_Object = MibTableColumn
stm1BulkChanIndex = _Stm1BulkChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 32, 1, 2),
    _Stm1BulkChanIndex_Type()
)
stm1BulkChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stm1BulkChanIndex.setStatus("current")


class _Stm1BulkChannel_Type(Stm1IndexOrZero):
    """Custom type stm1BulkChannel based on Stm1IndexOrZero"""
    defaultValue = 0


_Stm1BulkChannel_Type.__name__ = "Stm1IndexOrZero"
_Stm1BulkChannel_Object = MibTableColumn
stm1BulkChannel = _Stm1BulkChannel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 32, 1, 3),
    _Stm1BulkChannel_Type()
)
stm1BulkChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stm1BulkChannel.setStatus("current")
_LinkE1vsSTM1CapacityTable_Object = MibTable
linkE1vsSTM1CapacityTable = _LinkE1vsSTM1CapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 33)
)
if mibBuilder.loadTexts:
    linkE1vsSTM1CapacityTable.setStatus("current")
_LinkE1vsSTM1CapacityEntry_Object = MibTableRow
linkE1vsSTM1CapacityEntry = _LinkE1vsSTM1CapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 33, 1)
)
linkE1vsSTM1CapacityEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkAcmProfileId"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkE1vsSTM1CapacityStm1"),
)
if mibBuilder.loadTexts:
    linkE1vsSTM1CapacityEntry.setStatus("current")
_LinkE1vsSTM1CapacityStm1_Type = Integer32
_LinkE1vsSTM1CapacityStm1_Object = MibTableColumn
linkE1vsSTM1CapacityStm1 = _LinkE1vsSTM1CapacityStm1_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 33, 1, 1),
    _LinkE1vsSTM1CapacityStm1_Type()
)
linkE1vsSTM1CapacityStm1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkE1vsSTM1CapacityStm1.setStatus("current")
_LinkE1vsSTM1CapacityE1_Type = Integer32
_LinkE1vsSTM1CapacityE1_Object = MibTableColumn
linkE1vsSTM1CapacityE1 = _LinkE1vsSTM1CapacityE1_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 33, 1, 2),
    _LinkE1vsSTM1CapacityE1_Type()
)
linkE1vsSTM1CapacityE1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkE1vsSTM1CapacityE1.setStatus("current")
_LinkTfcV2Table_Object = MibTable
linkTfcV2Table = _LinkTfcV2Table_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 34)
)
if mibBuilder.loadTexts:
    linkTfcV2Table.setStatus("current")
_LinkTfcV2Entry_Object = MibTableRow
linkTfcV2Entry = _LinkTfcV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 34, 1)
)
linkTfcV2Entry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkPolIndex"),
)
if mibBuilder.loadTexts:
    linkTfcV2Entry.setStatus("current")


class _LinkTfcV2Action_Type(Integer32):
    """Custom type linkTfcV2Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("reset", 1))
    )


_LinkTfcV2Action_Type.__name__ = "Integer32"
_LinkTfcV2Action_Object = MibTableColumn
linkTfcV2Action = _LinkTfcV2Action_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 34, 1, 1),
    _LinkTfcV2Action_Type()
)
linkTfcV2Action.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkTfcV2Action.setStatus("current")


class _LinkTfcV2Control_Type(Integer32):
    """Custom type linkTfcV2Control based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkTfcV2Control_Type.__name__ = "Integer32"
_LinkTfcV2Control_Object = MibTableColumn
linkTfcV2Control = _LinkTfcV2Control_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 34, 1, 2),
    _LinkTfcV2Control_Type()
)
linkTfcV2Control.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkTfcV2Control.setStatus("current")


class _LinkTfcV2WatchWindow_Type(Integer32):
    """Custom type linkTfcV2WatchWindow based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_LinkTfcV2WatchWindow_Type.__name__ = "Integer32"
_LinkTfcV2WatchWindow_Object = MibTableColumn
linkTfcV2WatchWindow = _LinkTfcV2WatchWindow_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 34, 1, 3),
    _LinkTfcV2WatchWindow_Type()
)
linkTfcV2WatchWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkTfcV2WatchWindow.setStatus("current")


class _LinkTfcV2AlarmThreshold_Type(Integer32):
    """Custom type linkTfcV2AlarmThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_LinkTfcV2AlarmThreshold_Type.__name__ = "Integer32"
_LinkTfcV2AlarmThreshold_Object = MibTableColumn
linkTfcV2AlarmThreshold = _LinkTfcV2AlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 34, 1, 4),
    _LinkTfcV2AlarmThreshold_Type()
)
linkTfcV2AlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkTfcV2AlarmThreshold.setStatus("current")
_LinkTfcV2Alarm_Type = AlarmStatus
_LinkTfcV2Alarm_Object = MibTableColumn
linkTfcV2Alarm = _LinkTfcV2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 34, 1, 5),
    _LinkTfcV2Alarm_Type()
)
linkTfcV2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTfcV2Alarm.setStatus("current")
_LinkTfcV2RowStatus_Type = RowStatus
_LinkTfcV2RowStatus_Object = MibTableColumn
linkTfcV2RowStatus = _LinkTfcV2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 34, 1, 6),
    _LinkTfcV2RowStatus_Type()
)
linkTfcV2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkTfcV2RowStatus.setStatus("current")
_LinkProV2Table_Object = MibTable
linkProV2Table = _LinkProV2Table_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 35)
)
if mibBuilder.loadTexts:
    linkProV2Table.setStatus("current")
_LinkProV2Entry_Object = MibTableRow
linkProV2Entry = _LinkProV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 35, 1)
)
linkProV2Entry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkPolIndex"),
)
if mibBuilder.loadTexts:
    linkProV2Entry.setStatus("current")


class _LinkProV2ProtectionTxChIdx_Type(Integer32):
    """Custom type linkProV2ProtectionTxChIdx based on Integer32"""
    defaultValue = 0


_LinkProV2ProtectionTxChIdx_Type.__name__ = "Integer32"
_LinkProV2ProtectionTxChIdx_Object = MibTableColumn
linkProV2ProtectionTxChIdx = _LinkProV2ProtectionTxChIdx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 35, 1, 1),
    _LinkProV2ProtectionTxChIdx_Type()
)
linkProV2ProtectionTxChIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProV2ProtectionTxChIdx.setStatus("current")


class _LinkProV2ProtectionRxChIdx_Type(Integer32):
    """Custom type linkProV2ProtectionRxChIdx based on Integer32"""
    defaultValue = 0


_LinkProV2ProtectionRxChIdx_Type.__name__ = "Integer32"
_LinkProV2ProtectionRxChIdx_Object = MibTableColumn
linkProV2ProtectionRxChIdx = _LinkProV2ProtectionRxChIdx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 35, 1, 2),
    _LinkProV2ProtectionRxChIdx_Type()
)
linkProV2ProtectionRxChIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProV2ProtectionRxChIdx.setStatus("current")


class _LinkProV2TxWtrTime_Type(Integer32):
    """Custom type linkProV2TxWtrTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_LinkProV2TxWtrTime_Type.__name__ = "Integer32"
_LinkProV2TxWtrTime_Object = MibTableColumn
linkProV2TxWtrTime = _LinkProV2TxWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 35, 1, 3),
    _LinkProV2TxWtrTime_Type()
)
linkProV2TxWtrTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProV2TxWtrTime.setStatus("current")


class _LinkProV2RxWtrTime_Type(Integer32):
    """Custom type linkProV2RxWtrTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_LinkProV2RxWtrTime_Type.__name__ = "Integer32"
_LinkProV2RxWtrTime_Object = MibTableColumn
linkProV2RxWtrTime = _LinkProV2RxWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 35, 1, 4),
    _LinkProV2RxWtrTime_Type()
)
linkProV2RxWtrTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProV2RxWtrTime.setStatus("current")


class _LinkProV2TxSwitchedChIdx_Type(Integer32):
    """Custom type linkProV2TxSwitchedChIdx based on Integer32"""
    defaultValue = 0


_LinkProV2TxSwitchedChIdx_Type.__name__ = "Integer32"
_LinkProV2TxSwitchedChIdx_Object = MibTableColumn
linkProV2TxSwitchedChIdx = _LinkProV2TxSwitchedChIdx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 35, 1, 5),
    _LinkProV2TxSwitchedChIdx_Type()
)
linkProV2TxSwitchedChIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkProV2TxSwitchedChIdx.setStatus("current")


class _LinkProV2RxSwitchedChIdx_Type(Integer32):
    """Custom type linkProV2RxSwitchedChIdx based on Integer32"""
    defaultValue = 0


_LinkProV2RxSwitchedChIdx_Type.__name__ = "Integer32"
_LinkProV2RxSwitchedChIdx_Object = MibTableColumn
linkProV2RxSwitchedChIdx = _LinkProV2RxSwitchedChIdx_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 35, 1, 6),
    _LinkProV2RxSwitchedChIdx_Type()
)
linkProV2RxSwitchedChIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkProV2RxSwitchedChIdx.setStatus("current")


class _LinkProV2TxRevertive_Type(Integer32):
    """Custom type linkProV2TxRevertive based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkProV2TxRevertive_Type.__name__ = "Integer32"
_LinkProV2TxRevertive_Object = MibTableColumn
linkProV2TxRevertive = _LinkProV2TxRevertive_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 35, 1, 7),
    _LinkProV2TxRevertive_Type()
)
linkProV2TxRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProV2TxRevertive.setStatus("current")


class _LinkProV2RxRevertive_Type(Integer32):
    """Custom type linkProV2RxRevertive based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkProV2RxRevertive_Type.__name__ = "Integer32"
_LinkProV2RxRevertive_Object = MibTableColumn
linkProV2RxRevertive = _LinkProV2RxRevertive_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 35, 1, 8),
    _LinkProV2RxRevertive_Type()
)
linkProV2RxRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProV2RxRevertive.setStatus("current")


class _LinkProV2ExtraTraffic_Type(Integer32):
    """Custom type linkProV2ExtraTraffic based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkProV2ExtraTraffic_Type.__name__ = "Integer32"
_LinkProV2ExtraTraffic_Object = MibTableColumn
linkProV2ExtraTraffic = _LinkProV2ExtraTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 35, 1, 9),
    _LinkProV2ExtraTraffic_Type()
)
linkProV2ExtraTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProV2ExtraTraffic.setStatus("current")
_LinkProV2RowStatus_Type = RowStatus
_LinkProV2RowStatus_Object = MibTableColumn
linkProV2RowStatus = _LinkProV2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 35, 1, 10),
    _LinkProV2RowStatus_Type()
)
linkProV2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkProV2RowStatus.setStatus("current")
_LinkProMaintV2Table_Object = MibTable
linkProMaintV2Table = _LinkProMaintV2Table_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 36)
)
if mibBuilder.loadTexts:
    linkProMaintV2Table.setStatus("current")
_LinkProMaintV2Entry_Object = MibTableRow
linkProMaintV2Entry = _LinkProMaintV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 36, 1)
)
linkProMaintV2Entry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkPolIndex"),
)
if mibBuilder.loadTexts:
    linkProMaintV2Entry.setStatus("current")


class _LinkProMaintV2TxLockout_Type(Integer32):
    """Custom type linkProMaintV2TxLockout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkProMaintV2TxLockout_Type.__name__ = "Integer32"
_LinkProMaintV2TxLockout_Object = MibTableColumn
linkProMaintV2TxLockout = _LinkProMaintV2TxLockout_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 36, 1, 1),
    _LinkProMaintV2TxLockout_Type()
)
linkProMaintV2TxLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkProMaintV2TxLockout.setStatus("current")


class _LinkProMaintV2RxLockout_Type(Integer32):
    """Custom type linkProMaintV2RxLockout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LinkProMaintV2RxLockout_Type.__name__ = "Integer32"
_LinkProMaintV2RxLockout_Object = MibTableColumn
linkProMaintV2RxLockout = _LinkProMaintV2RxLockout_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 36, 1, 2),
    _LinkProMaintV2RxLockout_Type()
)
linkProMaintV2RxLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkProMaintV2RxLockout.setStatus("current")


class _LinkProMaintV2TxForced_Type(Integer32):
    """Custom type linkProMaintV2TxForced based on Integer32"""
    defaultValue = 0


_LinkProMaintV2TxForced_Type.__name__ = "Integer32"
_LinkProMaintV2TxForced_Object = MibTableColumn
linkProMaintV2TxForced = _LinkProMaintV2TxForced_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 36, 1, 3),
    _LinkProMaintV2TxForced_Type()
)
linkProMaintV2TxForced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkProMaintV2TxForced.setStatus("current")


class _LinkProMaintV2RxForced_Type(Integer32):
    """Custom type linkProMaintV2RxForced based on Integer32"""
    defaultValue = 0


_LinkProMaintV2RxForced_Type.__name__ = "Integer32"
_LinkProMaintV2RxForced_Object = MibTableColumn
linkProMaintV2RxForced = _LinkProMaintV2RxForced_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 36, 1, 4),
    _LinkProMaintV2RxForced_Type()
)
linkProMaintV2RxForced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkProMaintV2RxForced.setStatus("current")


class _LinkProMaintV2TxWtrReset_Type(Integer32):
    """Custom type linkProMaintV2TxWtrReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("on", 2))
    )


_LinkProMaintV2TxWtrReset_Type.__name__ = "Integer32"
_LinkProMaintV2TxWtrReset_Object = MibTableColumn
linkProMaintV2TxWtrReset = _LinkProMaintV2TxWtrReset_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 36, 1, 5),
    _LinkProMaintV2TxWtrReset_Type()
)
linkProMaintV2TxWtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkProMaintV2TxWtrReset.setStatus("current")


class _LinkProMaintV2RxWtrReset_Type(Integer32):
    """Custom type linkProMaintV2RxWtrReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("on", 2))
    )


_LinkProMaintV2RxWtrReset_Type.__name__ = "Integer32"
_LinkProMaintV2RxWtrReset_Object = MibTableColumn
linkProMaintV2RxWtrReset = _LinkProMaintV2RxWtrReset_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 36, 1, 6),
    _LinkProMaintV2RxWtrReset_Type()
)
linkProMaintV2RxWtrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkProMaintV2RxWtrReset.setStatus("current")
_SspTable_Object = MibTable
sspTable = _SspTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 37)
)
if mibBuilder.loadTexts:
    sspTable.setStatus("current")
_SspEntry_Object = MibTableRow
sspEntry = _SspEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 37, 1)
)
sspEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "linkPolIndex"),
    (0, "SIAE-RADIO-SYSTEM-MIB", "sspParameterType"),
)
if mibBuilder.loadTexts:
    sspEntry.setStatus("current")


class _SspParameterType_Type(Integer32):
    """Custom type sspParameterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localAdminStatus", 1),
          ("localOperStatus", 2),
          ("remoteAdminStatus", 3))
    )


_SspParameterType_Type.__name__ = "Integer32"
_SspParameterType_Object = MibTableColumn
sspParameterType = _SspParameterType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 37, 1, 1),
    _SspParameterType_Type()
)
sspParameterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sspParameterType.setStatus("current")


class _SspLinkBandwidth_Type(Integer32):
    """Custom type sspLinkBandwidth based on Integer32"""
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
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("sspBw3p5Mhz", 0),
          ("sspBw7MHz", 1),
          ("sspBw14MHz", 2),
          ("sspBw28MHz", 3),
          ("sspBw56MHz", 4),
          ("sspBw10MHz", 5),
          ("sspBw20MHz", 6),
          ("sspBw30MHz", 7),
          ("sspBw40MHz", 8),
          ("sspBw50MHz", 9),
          ("sspBw112Mhz", 10),
          ("sspBw250Mhz", 11),
          ("sspBw500Mhz", 12),
          ("sspBw750Mhz", 13),
          ("sspBw1Ghz", 14),
          ("sspBw60MHz", 15),
          ("sspBw80MHz", 16))
    )


_SspLinkBandwidth_Type.__name__ = "Integer32"
_SspLinkBandwidth_Object = MibTableColumn
sspLinkBandwidth = _SspLinkBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 37, 1, 2),
    _SspLinkBandwidth_Type()
)
sspLinkBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspLinkBandwidth.setStatus("current")


class _SspLinkModulation_Type(Integer32):
    """Custom type sspLinkModulation based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("sspModBPSK", 1),
          ("sspMod4QAM", 2),
          ("sspMod8PSK", 3),
          ("sspMod16QAM", 4),
          ("sspMod32QAM", 5),
          ("sspMod64QAM", 6),
          ("sspMod128QAM", 7),
          ("sspMod256QAM", 8),
          ("sspMod512QAM", 9),
          ("sspMod1024QAM", 10),
          ("sspMod2048QAM", 11),
          ("sspMod4096QAM", 12))
    )


_SspLinkModulation_Type.__name__ = "Integer32"
_SspLinkModulation_Object = MibTableColumn
sspLinkModulation = _SspLinkModulation_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 37, 1, 3),
    _SspLinkModulation_Type()
)
sspLinkModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspLinkModulation.setStatus("current")


class _SspLinkAcmEngineEnable_Type(Integer32):
    """Custom type sspLinkAcmEngineEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SspLinkAcmEngineEnable_Type.__name__ = "Integer32"
_SspLinkAcmEngineEnable_Object = MibTableColumn
sspLinkAcmEngineEnable = _SspLinkAcmEngineEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 37, 1, 4),
    _SspLinkAcmEngineEnable_Type()
)
sspLinkAcmEngineEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspLinkAcmEngineEnable.setStatus("current")
_SspLinkTxUpperProfile_Type = Integer32
_SspLinkTxUpperProfile_Object = MibTableColumn
sspLinkTxUpperProfile = _SspLinkTxUpperProfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 37, 1, 5),
    _SspLinkTxUpperProfile_Type()
)
sspLinkTxUpperProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspLinkTxUpperProfile.setStatus("current")
_SspLinkTxLowerProfile_Type = Integer32
_SspLinkTxLowerProfile_Object = MibTableColumn
sspLinkTxLowerProfile = _SspLinkTxLowerProfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 37, 1, 6),
    _SspLinkTxLowerProfile_Type()
)
sspLinkTxLowerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspLinkTxLowerProfile.setStatus("current")


class _SspLinkSynchSetupProtocolEnable_Type(Integer32):
    """Custom type sspLinkSynchSetupProtocolEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SspLinkSynchSetupProtocolEnable_Type.__name__ = "Integer32"
_SspLinkSynchSetupProtocolEnable_Object = MibTableColumn
sspLinkSynchSetupProtocolEnable = _SspLinkSynchSetupProtocolEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 37, 1, 7),
    _SspLinkSynchSetupProtocolEnable_Type()
)
sspLinkSynchSetupProtocolEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspLinkSynchSetupProtocolEnable.setStatus("current")


class _SspLinkProfilesSetSelection_Type(Integer32):
    """Custom type sspLinkProfilesSetSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highThroughput", 1),
          ("highGain", 2))
    )


_SspLinkProfilesSetSelection_Type.__name__ = "Integer32"
_SspLinkProfilesSetSelection_Object = MibTableColumn
sspLinkProfilesSetSelection = _SspLinkProfilesSetSelection_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 37, 1, 8),
    _SspLinkProfilesSetSelection_Type()
)
sspLinkProfilesSetSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspLinkProfilesSetSelection.setStatus("current")
_SspTdmE1Channel_Type = Integer32
_SspTdmE1Channel_Object = MibTableColumn
sspTdmE1Channel = _SspTdmE1Channel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 37, 1, 9),
    _SspTdmE1Channel_Type()
)
sspTdmE1Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspTdmE1Channel.setStatus("current")
_SspTdmStm1Channel_Type = Integer32
_SspTdmStm1Channel_Object = MibTableColumn
sspTdmStm1Channel = _SspTdmStm1Channel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 37, 1, 10),
    _SspTdmStm1Channel_Type()
)
sspTdmStm1Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sspTdmStm1Channel.setStatus("current")
_RadioLoopCapabilityTable_Object = MibTable
radioLoopCapabilityTable = _RadioLoopCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 38)
)
if mibBuilder.loadTexts:
    radioLoopCapabilityTable.setStatus("current")
_RadioLoopCapabilityEntry_Object = MibTableRow
radioLoopCapabilityEntry = _RadioLoopCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 38, 1)
)
radioLoopCapabilityEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioIndex"),
)
if mibBuilder.loadTexts:
    radioLoopCapabilityEntry.setStatus("current")
_RadioLoopRfGroup_Type = Integer32
_RadioLoopRfGroup_Object = MibTableColumn
radioLoopRfGroup = _RadioLoopRfGroup_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 38, 1, 1),
    _RadioLoopRfGroup_Type()
)
radioLoopRfGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLoopRfGroup.setStatus("current")
_RadioLoopIqGroup_Type = Integer32
_RadioLoopIqGroup_Object = MibTableColumn
radioLoopIqGroup = _RadioLoopIqGroup_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 38, 1, 2),
    _RadioLoopIqGroup_Type()
)
radioLoopIqGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLoopIqGroup.setStatus("current")
_RadioLoopBaseBandGroup_Type = Integer32
_RadioLoopBaseBandGroup_Object = MibTableColumn
radioLoopBaseBandGroup = _RadioLoopBaseBandGroup_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 38, 1, 3),
    _RadioLoopBaseBandGroup_Type()
)
radioLoopBaseBandGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLoopBaseBandGroup.setStatus("current")
_RadioRxBerThresholdTable_Object = MibTable
radioRxBerThresholdTable = _RadioRxBerThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 39)
)
if mibBuilder.loadTexts:
    radioRxBerThresholdTable.setStatus("current")
_RadioRxBerThresholdEntry_Object = MibTableRow
radioRxBerThresholdEntry = _RadioRxBerThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 39, 1)
)
radioRxBerThresholdEntry.setIndexNames(
    (0, "SIAE-RADIO-SYSTEM-MIB", "radioIndex"),
)
if mibBuilder.loadTexts:
    radioRxBerThresholdEntry.setStatus("current")


class _RadioRxBerThresholdStatus_Type(Integer32):
    """Custom type radioRxBerThresholdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonValid", 1),
          ("valid", 2))
    )


_RadioRxBerThresholdStatus_Type.__name__ = "Integer32"
_RadioRxBerThresholdStatus_Object = MibTableColumn
radioRxBerThresholdStatus = _RadioRxBerThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 39, 1, 1),
    _RadioRxBerThresholdStatus_Type()
)
radioRxBerThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRxBerThresholdStatus.setStatus("current")
_RadioNominalRxBerThreshold_Type = Integer32
_RadioNominalRxBerThreshold_Object = MibTableColumn
radioNominalRxBerThreshold = _RadioNominalRxBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 39, 1, 2),
    _RadioNominalRxBerThreshold_Type()
)
radioNominalRxBerThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioNominalRxBerThreshold.setStatus("current")
_RadioMeasuredRxBerThreshold_Type = Integer32
_RadioMeasuredRxBerThreshold_Object = MibTableColumn
radioMeasuredRxBerThreshold = _RadioMeasuredRxBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 39, 1, 3),
    _RadioMeasuredRxBerThreshold_Type()
)
radioMeasuredRxBerThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioMeasuredRxBerThreshold.setStatus("current")


class _RadioRemDemodulatorFailAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioRemDemodulatorFailAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioRemDemodulatorFailAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioRemDemodulatorFailAlarmSeverityCode_Object = MibScalar
radioRemDemodulatorFailAlarmSeverityCode = _RadioRemDemodulatorFailAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 50),
    _RadioRemDemodulatorFailAlarmSeverityCode_Type()
)
radioRemDemodulatorFailAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioRemDemodulatorFailAlarmSeverityCode.setStatus("current")


class _RadioRxActiveStatusTrapNotification_Type(Integer32):
    """Custom type radioRxActiveStatusTrapNotification based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapDisable", 1),
          ("trapEnable", 2))
    )


_RadioRxActiveStatusTrapNotification_Type.__name__ = "Integer32"
_RadioRxActiveStatusTrapNotification_Object = MibScalar
radioRxActiveStatusTrapNotification = _RadioRxActiveStatusTrapNotification_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 51),
    _RadioRxActiveStatusTrapNotification_Type()
)
radioRxActiveStatusTrapNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioRxActiveStatusTrapNotification.setStatus("current")


class _RadioTxActiveStatusTrapNotification_Type(Integer32):
    """Custom type radioTxActiveStatusTrapNotification based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapDisable", 1),
          ("trapEnable", 2))
    )


_RadioTxActiveStatusTrapNotification_Type.__name__ = "Integer32"
_RadioTxActiveStatusTrapNotification_Object = MibScalar
radioTxActiveStatusTrapNotification = _RadioTxActiveStatusTrapNotification_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 52),
    _RadioTxActiveStatusTrapNotification_Type()
)
radioTxActiveStatusTrapNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioTxActiveStatusTrapNotification.setStatus("current")


class _RadioCableOpenAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioCableOpenAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioCableOpenAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioCableOpenAlarmSeverityCode_Object = MibScalar
radioCableOpenAlarmSeverityCode = _RadioCableOpenAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 53),
    _RadioCableOpenAlarmSeverityCode_Type()
)
radioCableOpenAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioCableOpenAlarmSeverityCode.setStatus("current")


class _RadioCableShortAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioCableShortAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioCableShortAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioCableShortAlarmSeverityCode_Object = MibScalar
radioCableShortAlarmSeverityCode = _RadioCableShortAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 54),
    _RadioCableShortAlarmSeverityCode_Type()
)
radioCableShortAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioCableShortAlarmSeverityCode.setStatus("current")


class _RadioInvalidFrequencyAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioInvalidFrequencyAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioInvalidFrequencyAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioInvalidFrequencyAlarmSeverityCode_Object = MibScalar
radioInvalidFrequencyAlarmSeverityCode = _RadioInvalidFrequencyAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 55),
    _RadioInvalidFrequencyAlarmSeverityCode_Type()
)
radioInvalidFrequencyAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioInvalidFrequencyAlarmSeverityCode.setStatus("current")


class _RadioBaseBandRxAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioBaseBandRxAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioBaseBandRxAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioBaseBandRxAlarmSeverityCode_Object = MibScalar
radioBaseBandRxAlarmSeverityCode = _RadioBaseBandRxAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 56),
    _RadioBaseBandRxAlarmSeverityCode_Type()
)
radioBaseBandRxAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioBaseBandRxAlarmSeverityCode.setStatus("current")


class _RadioModulatorFailAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioModulatorFailAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioModulatorFailAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioModulatorFailAlarmSeverityCode_Object = MibScalar
radioModulatorFailAlarmSeverityCode = _RadioModulatorFailAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 57),
    _RadioModulatorFailAlarmSeverityCode_Type()
)
radioModulatorFailAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioModulatorFailAlarmSeverityCode.setStatus("current")


class _RadioDemodulatorFailAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioDemodulatorFailAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioDemodulatorFailAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioDemodulatorFailAlarmSeverityCode_Object = MibScalar
radioDemodulatorFailAlarmSeverityCode = _RadioDemodulatorFailAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 58),
    _RadioDemodulatorFailAlarmSeverityCode_Type()
)
radioDemodulatorFailAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioDemodulatorFailAlarmSeverityCode.setStatus("current")


class _RadioRxPowerLowAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioRxPowerLowAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioRxPowerLowAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioRxPowerLowAlarmSeverityCode_Object = MibScalar
radioRxPowerLowAlarmSeverityCode = _RadioRxPowerLowAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 59),
    _RadioRxPowerLowAlarmSeverityCode_Type()
)
radioRxPowerLowAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioRxPowerLowAlarmSeverityCode.setStatus("current")


class _RadioTxPowerLowAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioTxPowerLowAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioTxPowerLowAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioTxPowerLowAlarmSeverityCode_Object = MibScalar
radioTxPowerLowAlarmSeverityCode = _RadioTxPowerLowAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 60),
    _RadioTxPowerLowAlarmSeverityCode_Type()
)
radioTxPowerLowAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioTxPowerLowAlarmSeverityCode.setStatus("current")


class _RadioVcoFailAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioVcoFailAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioVcoFailAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioVcoFailAlarmSeverityCode_Object = MibScalar
radioVcoFailAlarmSeverityCode = _RadioVcoFailAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 61),
    _RadioVcoFailAlarmSeverityCode_Type()
)
radioVcoFailAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioVcoFailAlarmSeverityCode.setStatus("current")


class _RadioRxIFAgcAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioRxIFAgcAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioRxIFAgcAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioRxIFAgcAlarmSeverityCode_Object = MibScalar
radioRxIFAgcAlarmSeverityCode = _RadioRxIFAgcAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 62),
    _RadioRxIFAgcAlarmSeverityCode_Type()
)
radioRxIFAgcAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioRxIFAgcAlarmSeverityCode.setStatus("current")


class _RadioTxIFAgcAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioTxIFAgcAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioTxIFAgcAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioTxIFAgcAlarmSeverityCode_Object = MibScalar
radioTxIFAgcAlarmSeverityCode = _RadioTxIFAgcAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 63),
    _RadioTxIFAgcAlarmSeverityCode_Type()
)
radioTxIFAgcAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioTxIFAgcAlarmSeverityCode.setStatus("current")


class _RadioIduOduCommunicationAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioIduOduCommunicationAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioIduOduCommunicationAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioIduOduCommunicationAlarmSeverityCode_Object = MibScalar
radioIduOduCommunicationAlarmSeverityCode = _RadioIduOduCommunicationAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 64),
    _RadioIduOduCommunicationAlarmSeverityCode_Type()
)
radioIduOduCommunicationAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioIduOduCommunicationAlarmSeverityCode.setStatus("current")


class _RadioOduIduCommunicationAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioOduIduCommunicationAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_RadioOduIduCommunicationAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioOduIduCommunicationAlarmSeverityCode_Object = MibScalar
radioOduIduCommunicationAlarmSeverityCode = _RadioOduIduCommunicationAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 65),
    _RadioOduIduCommunicationAlarmSeverityCode_Type()
)
radioOduIduCommunicationAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioOduIduCommunicationAlarmSeverityCode.setStatus("current")


class _RadioLocalOduAlarmSynthesisSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioLocalOduAlarmSynthesisSeverityCode based on AlarmSeverityCode"""
    defaultValue = 18


_RadioLocalOduAlarmSynthesisSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioLocalOduAlarmSynthesisSeverityCode_Object = MibScalar
radioLocalOduAlarmSynthesisSeverityCode = _RadioLocalOduAlarmSynthesisSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 66),
    _RadioLocalOduAlarmSynthesisSeverityCode_Type()
)
radioLocalOduAlarmSynthesisSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioLocalOduAlarmSynthesisSeverityCode.setStatus("current")


class _RadioRemoteOduAlarmSynthesisSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioRemoteOduAlarmSynthesisSeverityCode based on AlarmSeverityCode"""
    defaultValue = 18


_RadioRemoteOduAlarmSynthesisSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioRemoteOduAlarmSynthesisSeverityCode_Object = MibScalar
radioRemoteOduAlarmSynthesisSeverityCode = _RadioRemoteOduAlarmSynthesisSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 67),
    _RadioRemoteOduAlarmSynthesisSeverityCode_Type()
)
radioRemoteOduAlarmSynthesisSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioRemoteOduAlarmSynthesisSeverityCode.setStatus("current")


class _RadioConfigMismatchAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioConfigMismatchAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioConfigMismatchAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioConfigMismatchAlarmSeverityCode_Object = MibScalar
radioConfigMismatchAlarmSeverityCode = _RadioConfigMismatchAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 68),
    _RadioConfigMismatchAlarmSeverityCode_Type()
)
radioConfigMismatchAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioConfigMismatchAlarmSeverityCode.setStatus("current")


class _RadioPrxHysteresisValue_Type(Integer32):
    """Custom type radioPrxHysteresisValue based on Integer32"""
    defaultValue = 3


_RadioPrxHysteresisValue_Type.__name__ = "Integer32"
_RadioPrxHysteresisValue_Object = MibScalar
radioPrxHysteresisValue = _RadioPrxHysteresisValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 69),
    _RadioPrxHysteresisValue_Type()
)
radioPrxHysteresisValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioPrxHysteresisValue.setStatus("current")


class _RadioPtxHysteresisValue_Type(Integer32):
    """Custom type radioPtxHysteresisValue based on Integer32"""
    defaultValue = 3


_RadioPtxHysteresisValue_Type.__name__ = "Integer32"
_RadioPtxHysteresisValue_Object = MibScalar
radioPtxHysteresisValue = _RadioPtxHysteresisValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 70),
    _RadioPtxHysteresisValue_Type()
)
radioPtxHysteresisValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioPtxHysteresisValue.setStatus("current")


class _RadioPrxHysteresisValueTrapNotification_Type(Integer32):
    """Custom type radioPrxHysteresisValueTrapNotification based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapDisable", 1),
          ("trapEnable", 2))
    )


_RadioPrxHysteresisValueTrapNotification_Type.__name__ = "Integer32"
_RadioPrxHysteresisValueTrapNotification_Object = MibScalar
radioPrxHysteresisValueTrapNotification = _RadioPrxHysteresisValueTrapNotification_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 71),
    _RadioPrxHysteresisValueTrapNotification_Type()
)
radioPrxHysteresisValueTrapNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioPrxHysteresisValueTrapNotification.setStatus("current")


class _RadioPtxHysteresisValueTrapNotification_Type(Integer32):
    """Custom type radioPtxHysteresisValueTrapNotification based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapDisable", 1),
          ("trapEnable", 2))
    )


_RadioPtxHysteresisValueTrapNotification_Type.__name__ = "Integer32"
_RadioPtxHysteresisValueTrapNotification_Object = MibScalar
radioPtxHysteresisValueTrapNotification = _RadioPtxHysteresisValueTrapNotification_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 72),
    _RadioPtxHysteresisValueTrapNotification_Type()
)
radioPtxHysteresisValueTrapNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioPtxHysteresisValueTrapNotification.setStatus("current")


class _RadioRxQualityLowAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioRxQualityLowAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioRxQualityLowAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioRxQualityLowAlarmSeverityCode_Object = MibScalar
radioRxQualityLowAlarmSeverityCode = _RadioRxQualityLowAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 73),
    _RadioRxQualityLowAlarmSeverityCode_Type()
)
radioRxQualityLowAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioRxQualityLowAlarmSeverityCode.setStatus("current")


class _RadioRxQualityWarningAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type radioRxQualityWarningAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RadioRxQualityWarningAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RadioRxQualityWarningAlarmSeverityCode_Object = MibScalar
radioRxQualityWarningAlarmSeverityCode = _RadioRxQualityWarningAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 74),
    _RadioRxQualityWarningAlarmSeverityCode_Type()
)
radioRxQualityWarningAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioRxQualityWarningAlarmSeverityCode.setStatus("current")


class _LinkReducedCapacityAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type linkReducedCapacityAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_LinkReducedCapacityAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LinkReducedCapacityAlarmSeverityCode_Object = MibScalar
linkReducedCapacityAlarmSeverityCode = _LinkReducedCapacityAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 75),
    _LinkReducedCapacityAlarmSeverityCode_Type()
)
linkReducedCapacityAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkReducedCapacityAlarmSeverityCode.setStatus("current")


class _LinkLinkTelemetryFailAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type linkLinkTelemetryFailAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_LinkLinkTelemetryFailAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LinkLinkTelemetryFailAlarmSeverityCode_Object = MibScalar
linkLinkTelemetryFailAlarmSeverityCode = _LinkLinkTelemetryFailAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 76),
    _LinkLinkTelemetryFailAlarmSeverityCode_Type()
)
linkLinkTelemetryFailAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkLinkTelemetryFailAlarmSeverityCode.setStatus("current")


class _LinkIdMismatchAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type linkIdMismatchAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_LinkIdMismatchAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LinkIdMismatchAlarmSeverityCode_Object = MibScalar
linkIdMismatchAlarmSeverityCode = _LinkIdMismatchAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 77),
    _LinkIdMismatchAlarmSeverityCode_Type()
)
linkIdMismatchAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkIdMismatchAlarmSeverityCode.setStatus("current")


class _LinkRadioEocAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type linkRadioEocAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_LinkRadioEocAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LinkRadioEocAlarmSeverityCode_Object = MibScalar
linkRadioEocAlarmSeverityCode = _LinkRadioEocAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 78),
    _LinkRadioEocAlarmSeverityCode_Type()
)
linkRadioEocAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkRadioEocAlarmSeverityCode.setStatus("current")


class _LinkSetupMismatchAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type linkSetupMismatchAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_LinkSetupMismatchAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LinkSetupMismatchAlarmSeverityCode_Object = MibScalar
linkSetupMismatchAlarmSeverityCode = _LinkSetupMismatchAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 79),
    _LinkSetupMismatchAlarmSeverityCode_Type()
)
linkSetupMismatchAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkSetupMismatchAlarmSeverityCode.setStatus("current")


class _LinkRescueSetupAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type linkRescueSetupAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 6


_LinkRescueSetupAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LinkRescueSetupAlarmSeverityCode_Object = MibScalar
linkRescueSetupAlarmSeverityCode = _LinkRescueSetupAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 80),
    _LinkRescueSetupAlarmSeverityCode_Type()
)
linkRescueSetupAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkRescueSetupAlarmSeverityCode.setStatus("current")


class _LinkXpicProcedureBlockAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type linkXpicProcedureBlockAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_LinkXpicProcedureBlockAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LinkXpicProcedureBlockAlarmSeverityCode_Object = MibScalar
linkXpicProcedureBlockAlarmSeverityCode = _LinkXpicProcedureBlockAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 81),
    _LinkXpicProcedureBlockAlarmSeverityCode_Type()
)
linkXpicProcedureBlockAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkXpicProcedureBlockAlarmSeverityCode.setStatus("current")


class _LinkXpicRemTxOffAlarmAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type linkXpicRemTxOffAlarmAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_LinkXpicRemTxOffAlarmAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LinkXpicRemTxOffAlarmAlarmSeverityCode_Object = MibScalar
linkXpicRemTxOffAlarmAlarmSeverityCode = _LinkXpicRemTxOffAlarmAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 82),
    _LinkXpicRemTxOffAlarmAlarmSeverityCode_Type()
)
linkXpicRemTxOffAlarmAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkXpicRemTxOffAlarmAlarmSeverityCode.setStatus("current")
_LinkLocalIduAlarmSynthesis_Type = AlarmStatus
_LinkLocalIduAlarmSynthesis_Object = MibScalar
linkLocalIduAlarmSynthesis = _LinkLocalIduAlarmSynthesis_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 83),
    _LinkLocalIduAlarmSynthesis_Type()
)
linkLocalIduAlarmSynthesis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLocalIduAlarmSynthesis.setStatus("current")


class _LinkLocalIduAlarmSynthesisSeverityCode_Type(AlarmSeverityCode):
    """Custom type linkLocalIduAlarmSynthesisSeverityCode based on AlarmSeverityCode"""
    defaultValue = 18


_LinkLocalIduAlarmSynthesisSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LinkLocalIduAlarmSynthesisSeverityCode_Object = MibScalar
linkLocalIduAlarmSynthesisSeverityCode = _LinkLocalIduAlarmSynthesisSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 84),
    _LinkLocalIduAlarmSynthesisSeverityCode_Type()
)
linkLocalIduAlarmSynthesisSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkLocalIduAlarmSynthesisSeverityCode.setStatus("current")


class _LinkRemoteIduAlarmSynthesisSeverityCode_Type(AlarmSeverityCode):
    """Custom type linkRemoteIduAlarmSynthesisSeverityCode based on AlarmSeverityCode"""
    defaultValue = 18


_LinkRemoteIduAlarmSynthesisSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LinkRemoteIduAlarmSynthesisSeverityCode_Object = MibScalar
linkRemoteIduAlarmSynthesisSeverityCode = _LinkRemoteIduAlarmSynthesisSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 85),
    _LinkRemoteIduAlarmSynthesisSeverityCode_Type()
)
linkRemoteIduAlarmSynthesisSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkRemoteIduAlarmSynthesisSeverityCode.setStatus("current")


class _LinkTfcAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type linkTfcAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 4


_LinkTfcAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LinkTfcAlarmSeverityCode_Object = MibScalar
linkTfcAlarmSeverityCode = _LinkTfcAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 86),
    _LinkTfcAlarmSeverityCode_Type()
)
linkTfcAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTfcAlarmSeverityCode.setStatus("current")


class _LinkBerSyncLossAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type linkBerSyncLossAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_LinkBerSyncLossAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LinkBerSyncLossAlarmSeverityCode_Object = MibScalar
linkBerSyncLossAlarmSeverityCode = _LinkBerSyncLossAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 87),
    _LinkBerSyncLossAlarmSeverityCode_Type()
)
linkBerSyncLossAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkBerSyncLossAlarmSeverityCode.setStatus("current")


class _LinkNotMatchingRadiosAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type linkNotMatchingRadiosAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_LinkNotMatchingRadiosAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_LinkNotMatchingRadiosAlarmSeverityCode_Object = MibScalar
linkNotMatchingRadiosAlarmSeverityCode = _LinkNotMatchingRadiosAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 88),
    _LinkNotMatchingRadiosAlarmSeverityCode_Type()
)
linkNotMatchingRadiosAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkNotMatchingRadiosAlarmSeverityCode.setStatus("current")


class _ChannelSpacingSelection_Type(Bits):
    """Custom type channelSpacingSelection based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("etsi", 0),
          ("fcc", 1))
    )

_ChannelSpacingSelection_Type.__name__ = "Bits"
_ChannelSpacingSelection_Object = MibScalar
channelSpacingSelection = _ChannelSpacingSelection_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 89),
    _ChannelSpacingSelection_Type()
)
channelSpacingSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelSpacingSelection.setStatus("current")


class _FadeMarginMeasure_Type(Integer32):
    """Custom type fadeMarginMeasure based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FadeMarginMeasure_Type.__name__ = "Integer32"
_FadeMarginMeasure_Object = MibScalar
fadeMarginMeasure = _FadeMarginMeasure_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 90),
    _FadeMarginMeasure_Type()
)
fadeMarginMeasure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fadeMarginMeasure.setStatus("current")


class _LinkConfigurationInProgressTrapNotification_Type(Integer32):
    """Custom type linkConfigurationInProgressTrapNotification based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapDisable", 1),
          ("trapEnable", 2))
    )


_LinkConfigurationInProgressTrapNotification_Type.__name__ = "Integer32"
_LinkConfigurationInProgressTrapNotification_Object = MibScalar
linkConfigurationInProgressTrapNotification = _LinkConfigurationInProgressTrapNotification_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 80, 91),
    _LinkConfigurationInProgressTrapNotification_Type()
)
linkConfigurationInProgressTrapNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkConfigurationInProgressTrapNotification.setStatus("current")

# Managed Objects groups


# Notification objects

radioPrxChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 8001)
)
radioPrxChange.setObjects(
      *(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"),
        ("SIAE-RADIO-SYSTEM-MIB", "radioIndex"),
        ("SIAE-RADIO-SYSTEM-MIB", "radioSettingsLabel"),
        ("SIAE-RADIO-SYSTEM-MIB", "radioPrx"))
)
if mibBuilder.loadTexts:
    radioPrxChange.setStatus(
        "current"
    )

radioPtxChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 8002)
)
radioPtxChange.setObjects(
      *(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"),
        ("SIAE-RADIO-SYSTEM-MIB", "radioIndex"),
        ("SIAE-RADIO-SYSTEM-MIB", "radioSettingsLabel"),
        ("SIAE-RADIO-SYSTEM-MIB", "radioPtx"))
)
if mibBuilder.loadTexts:
    radioPtxChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-RADIO-SYSTEM-MIB",
    **{"ChannelSpacing": ChannelSpacing,
       "ModulationMap": ModulationMap,
       "ConfigMismatchReason": ConfigMismatchReason,
       "RadioCapability": RadioCapability,
       "BitsPerSymbol": BitsPerSymbol,
       "Stm1IndexOrZero": Stm1IndexOrZero,
       "radioPrxChange": radioPrxChange,
       "radioPtxChange": radioPtxChange,
       "radioSystem": radioSystem,
       "radioSystemMibVersion": radioSystemMibVersion,
       "radioTable": radioTable,
       "radioEntry": radioEntry,
       "radioIndex": radioIndex,
       "radioLabel": radioLabel,
       "radioType": radioType,
       "radioIfIndex": radioIfIndex,
       "radioStorageType": radioStorageType,
       "xpicTable": xpicTable,
       "xpicEntry": xpicEntry,
       "xpicIndex": xpicIndex,
       "xpicRadioIdx": xpicRadioIdx,
       "xpicRowstatus": xpicRowstatus,
       "xpicChTable": xpicChTable,
       "xpicChEntry": xpicChEntry,
       "xpicChPolIndex": xpicChPolIndex,
       "xpicChRadioIdx": xpicChRadioIdx,
       "xpicChRowstatus": xpicChRowstatus,
       "linkAvailableIndex": linkAvailableIndex,
       "linkTable": linkTable,
       "linkEntry": linkEntry,
       "linkIndex": linkIndex,
       "linkType": linkType,
       "linkLabel": linkLabel,
       "linkIfIndex": linkIfIndex,
       "linkRowstatus": linkRowstatus,
       "linkChTable": linkChTable,
       "linkChEntry": linkChEntry,
       "linkChIndex": linkChIndex,
       "linkChRadioIdx": linkChRadioIdx,
       "linkChRadioSettingsIdx": linkChRadioSettingsIdx,
       "linkChRowstatus": linkChRowstatus,
       "linkSettingsTable": linkSettingsTable,
       "linkSettingsEntry": linkSettingsEntry,
       "linkBandwidthAndModulation": linkBandwidthAndModulation,
       "linkAcmEngineEnable": linkAcmEngineEnable,
       "linkTxUpperProfile": linkTxUpperProfile,
       "linkTxLowerProfile": linkTxLowerProfile,
       "linkId": linkId,
       "linkTxPwrThresh": linkTxPwrThresh,
       "linkRxPwrThresh": linkRxPwrThresh,
       "linkSynchSetupProtocolEnable": linkSynchSetupProtocolEnable,
       "linkProfilesSetSelection": linkProfilesSetSelection,
       "linkXpicControlProcedure": linkXpicControlProcedure,
       "radioSettingsTable": radioSettingsTable,
       "radioSettingsEntry": radioSettingsEntry,
       "radioSettingsIndex": radioSettingsIndex,
       "radioSettingsRowStatus": radioSettingsRowStatus,
       "radioSettingsLabel": radioSettingsLabel,
       "radioTxFrequency": radioTxFrequency,
       "radioDuplexFrequency": radioDuplexFrequency,
       "radioTxAttenuation": radioTxAttenuation,
       "radioAtpcManual": radioAtpcManual,
       "radioAtpcPwrHigh": radioAtpcPwrHigh,
       "radioAtpcPwrLow": radioAtpcPwrLow,
       "radioAtpcRange": radioAtpcRange,
       "radioFreqTableSelection": radioFreqTableSelection,
       "tdmSettingsTable": tdmSettingsTable,
       "tdmSettingsEntry": tdmSettingsEntry,
       "tdmPolIndex": tdmPolIndex,
       "tdmE1Channel": tdmE1Channel,
       "tdmE1Framer": tdmE1Framer,
       "radioCapabilitiesTable": radioCapabilitiesTable,
       "radioCapabilitiesEntry": radioCapabilitiesEntry,
       "radioCapabilitiesCapability": radioCapabilitiesCapability,
       "radioCapabilitiesTxMinFrequency": radioCapabilitiesTxMinFrequency,
       "radioCapabilitiesTxMaxFrequency": radioCapabilitiesTxMaxFrequency,
       "radioCapabilitiesStepFrequency": radioCapabilitiesStepFrequency,
       "radioCapabilitiesMinPtxNominalValue": radioCapabilitiesMinPtxNominalValue,
       "radioCapabilitiesMaxPtxNominalValue": radioCapabilitiesMaxPtxNominalValue,
       "radioCapabilitiesExtendedMinPwr": radioCapabilitiesExtendedMinPwr,
       "radioStatusTable": radioStatusTable,
       "radioStatusEntry": radioStatusEntry,
       "radioCurrentDuplexFrequency": radioCurrentDuplexFrequency,
       "radioTxChannelSpacing": radioTxChannelSpacing,
       "radioPrx": radioPrx,
       "radioPtx": radioPtx,
       "radioNormalizedMse": radioNormalizedMse,
       "radioRxActiveStatus": radioRxActiveStatus,
       "radioTxActiveStatus": radioTxActiveStatus,
       "radioCableOpenAlarm": radioCableOpenAlarm,
       "radioCableShortAlarm": radioCableShortAlarm,
       "radioInvalidFrequencyAlarm": radioInvalidFrequencyAlarm,
       "radioBaseBandRxAlarm": radioBaseBandRxAlarm,
       "radioModulatorFailAlarm": radioModulatorFailAlarm,
       "radioDemodulatorFailAlarm": radioDemodulatorFailAlarm,
       "radioRxPowerLowAlarm": radioRxPowerLowAlarm,
       "radioTxPowerLowAlarm": radioTxPowerLowAlarm,
       "radioRemDemodulatorFailAlarm": radioRemDemodulatorFailAlarm,
       "radioVcoFailAlarm": radioVcoFailAlarm,
       "radioRxIFAgcAlarm": radioRxIFAgcAlarm,
       "radioTxIFAgcAlarm": radioTxIFAgcAlarm,
       "radioIduOduCommunicationAlarm": radioIduOduCommunicationAlarm,
       "radioOduIduCommunicationAlarm": radioOduIduCommunicationAlarm,
       "radioLocalOduAlarmSynthesis": radioLocalOduAlarmSynthesis,
       "radioRemoteOduAlarmSynthesis": radioRemoteOduAlarmSynthesis,
       "radioConfigMismatchAlarm": radioConfigMismatchAlarm,
       "radioConfigAlarmReason": radioConfigAlarmReason,
       "radioRxQualityLowAlarm": radioRxQualityLowAlarm,
       "radioRxQualityWarningAlarm": radioRxQualityWarningAlarm,
       "radioXpd": radioXpd,
       "radioMaintTable": radioMaintTable,
       "radioMaintEntry": radioMaintEntry,
       "radioTxStatus": radioTxStatus,
       "radioCarrierOnly": radioCarrierOnly,
       "radioLoop": radioLoop,
       "radioRFLoopTestResult": radioRFLoopTestResult,
       "radioRFLoopTestPercTime": radioRFLoopTestPercTime,
       "radioRtPsuOff": radioRtPsuOff,
       "radioLom": radioLom,
       "radioXpic": radioXpic,
       "radioFrequencyTable": radioFrequencyTable,
       "radioFreqTabEntry": radioFreqTabEntry,
       "radioFreqChannelId": radioFreqChannelId,
       "radioFreqChannelNum": radioFreqChannelNum,
       "radioFreqValue": radioFreqValue,
       "radioDuplexFrequencyTable": radioDuplexFrequencyTable,
       "radioDuplexFreqEntry": radioDuplexFreqEntry,
       "radioDuplexFreqId": radioDuplexFreqId,
       "radioDuplexFreqValue": radioDuplexFreqValue,
       "radioModulationTable": radioModulationTable,
       "radioModulationEntry": radioModulationEntry,
       "radioChannelSpacing": radioChannelSpacing,
       "radioModulationMap": radioModulationMap,
       "radioRefModulationMap": radioRefModulationMap,
       "linkStatusTable": linkStatusTable,
       "linkStatusEntry": linkStatusEntry,
       "linkPolIndex": linkPolIndex,
       "linkAcmRxProfile": linkAcmRxProfile,
       "linkAcmTxProfile": linkAcmTxProfile,
       "linkAcmRxProfileLabel": linkAcmRxProfileLabel,
       "linkAcmTxProfileLabel": linkAcmTxProfileLabel,
       "linkAcmRxModulation": linkAcmRxModulation,
       "linkAcmTxModulation": linkAcmTxModulation,
       "linkAcmRxCode": linkAcmRxCode,
       "linkAcmTxCode": linkAcmTxCode,
       "linkTxETHCapacity": linkTxETHCapacity,
       "linkRxETHCapacity": linkRxETHCapacity,
       "linkTxTDMCapacity": linkTxTDMCapacity,
       "linkRxTDMCapacity": linkRxTDMCapacity,
       "linkRescueModulation": linkRescueModulation,
       "linkReducedCapacityAlarm": linkReducedCapacityAlarm,
       "linkLinkTelemetryFailAlarm": linkLinkTelemetryFailAlarm,
       "linkIdMismatchAlarm": linkIdMismatchAlarm,
       "linkRadioEocAlarm": linkRadioEocAlarm,
       "linkSetupMismatchAlarm": linkSetupMismatchAlarm,
       "linkRescueSetupAlarm": linkRescueSetupAlarm,
       "linkXpicProcedureBlockAlarm": linkXpicProcedureBlockAlarm,
       "linkXpicRemTxOffAlarm": linkXpicRemTxOffAlarm,
       "linkRemoteIduAlarmSynthesis": linkRemoteIduAlarmSynthesis,
       "linkNotMatchingRadiosAlarm": linkNotMatchingRadiosAlarm,
       "linkConfigurationInProgress": linkConfigurationInProgress,
       "linkXpd": linkXpd,
       "linkTfcTable": linkTfcTable,
       "linkTfcEntry": linkTfcEntry,
       "linkTfcAction": linkTfcAction,
       "linkTfcControl": linkTfcControl,
       "linkTfcWatchWindow": linkTfcWatchWindow,
       "linkTfcAlarmThreshold": linkTfcAlarmThreshold,
       "linkTfcAlarm": linkTfcAlarm,
       "linkTfcRowStatus": linkTfcRowStatus,
       "linkMaintTable": linkMaintTable,
       "linkMaintEntry": linkMaintEntry,
       "linkBerStart": linkBerStart,
       "linkBaseBandLom": linkBaseBandLom,
       "linkFadeMarginMeasure": linkFadeMarginMeasure,
       "linkXpicControlProcedureReset": linkXpicControlProcedureReset,
       "linkBerTable": linkBerTable,
       "linkBerEntry": linkBerEntry,
       "linkBerErrorCounterH": linkBerErrorCounterH,
       "linkBerErrorCounterL": linkBerErrorCounterL,
       "linkBerDataCounterH": linkBerDataCounterH,
       "linkBerDataCounterL": linkBerDataCounterL,
       "linkBerSyncLossAlarm": linkBerSyncLossAlarm,
       "linkBerSyncLossAlarmCounter": linkBerSyncLossAlarmCounter,
       "linkBerElapsedTime": linkBerElapsedTime,
       "linkAcmTable": linkAcmTable,
       "linkAcmEntry": linkAcmEntry,
       "linkAcmProfileId": linkAcmProfileId,
       "linkAcmProfileModulation": linkAcmProfileModulation,
       "linkAcmProfileCode": linkAcmProfileCode,
       "linkAcmProfileCapacity": linkAcmProfileCapacity,
       "linkAcmProfileLabel": linkAcmProfileLabel,
       "linkAcmProfileEnable": linkAcmProfileEnable,
       "linkAcmMaxTDMCapacity": linkAcmMaxTDMCapacity,
       "linkAcmPowerScaling": linkAcmPowerScaling,
       "linkAcmDownshiftThreshold": linkAcmDownshiftThreshold,
       "linkAcmUpshiftThreshold": linkAcmUpshiftThreshold,
       "linkAcmActiveProfile": linkAcmActiveProfile,
       "linkAcmTDMCapacity": linkAcmTDMCapacity,
       "linkAcmETHCapacity": linkAcmETHCapacity,
       "linkAcmAtpcRxPowerScaling": linkAcmAtpcRxPowerScaling,
       "linkAcmPowerRange": linkAcmPowerRange,
       "linkProTable": linkProTable,
       "linkProEntry": linkProEntry,
       "linkProProtectionTxChIdx": linkProProtectionTxChIdx,
       "linkProProtectionRxChIdx": linkProProtectionRxChIdx,
       "linkProTxWtrTime": linkProTxWtrTime,
       "linkProRxWtrTime": linkProRxWtrTime,
       "linkProTxSwitchedChIdx": linkProTxSwitchedChIdx,
       "linkProRxSwitchedChIdx": linkProRxSwitchedChIdx,
       "linkProTxRevertive": linkProTxRevertive,
       "linkProRxRevertive": linkProRxRevertive,
       "linkProExtraTraffic": linkProExtraTraffic,
       "linkProRowStatus": linkProRowStatus,
       "linkProMaintTable": linkProMaintTable,
       "linkProMaintEntry": linkProMaintEntry,
       "linkProMaintTxLockout": linkProMaintTxLockout,
       "linkProMaintRxLockout": linkProMaintRxLockout,
       "linkProMaintTxForced": linkProMaintTxForced,
       "linkProMaintRxForced": linkProMaintRxForced,
       "linkProMaintTxWtrReset": linkProMaintTxWtrReset,
       "linkProMaintRxWtrReset": linkProMaintRxWtrReset,
       "linkCapabilitiesTable": linkCapabilitiesTable,
       "linkCapabilitiesEntry": linkCapabilitiesEntry,
       "linkCapabilitiesCapability": linkCapabilitiesCapability,
       "linkCapabilitiesTxMinFrequency": linkCapabilitiesTxMinFrequency,
       "linkCapabilitiesTxMaxFrequency": linkCapabilitiesTxMaxFrequency,
       "linkCapabilitiesStepFrequency": linkCapabilitiesStepFrequency,
       "linkCapabilitiesMinPtxNominalValue": linkCapabilitiesMinPtxNominalValue,
       "linkCapabilitiesMaxPtxNominalValue": linkCapabilitiesMaxPtxNominalValue,
       "linkCapabilitiesExtendedMinPwr": linkCapabilitiesExtendedMinPwr,
       "linkFrequencyTable": linkFrequencyTable,
       "linkFreqTabEntry": linkFreqTabEntry,
       "linkFreqChannelId": linkFreqChannelId,
       "linkFreqChannelNum": linkFreqChannelNum,
       "linkFreqValue": linkFreqValue,
       "linkDuplexFrequencyTable": linkDuplexFrequencyTable,
       "linkDuplexFreqEntry": linkDuplexFreqEntry,
       "linkDuplexFreqId": linkDuplexFreqId,
       "linkDuplexFreqValue": linkDuplexFreqValue,
       "linkModulationTable": linkModulationTable,
       "linkModulationEntry": linkModulationEntry,
       "linkChannelSpacing": linkChannelSpacing,
       "linkModulationMap": linkModulationMap,
       "linkRefModulationMap": linkRefModulationMap,
       "combinedRadioCapabilitiesTable": combinedRadioCapabilitiesTable,
       "combinedRadioCapabilitiesEntry": combinedRadioCapabilitiesEntry,
       "combinedRadioCapabilitiesCapability": combinedRadioCapabilitiesCapability,
       "combinedRadioCapabilitiesTxMinFrequency": combinedRadioCapabilitiesTxMinFrequency,
       "combinedRadioCapabilitiesTxMaxFrequency": combinedRadioCapabilitiesTxMaxFrequency,
       "combinedRadioCapabilitiesStepFrequency": combinedRadioCapabilitiesStepFrequency,
       "combinedRadioCapabilitiesMinPtxNominalValue": combinedRadioCapabilitiesMinPtxNominalValue,
       "combinedRadioCapabilitiesMaxPtxNominalValue": combinedRadioCapabilitiesMaxPtxNominalValue,
       "combinedRadioCapabilitiesExtendedMinPwr": combinedRadioCapabilitiesExtendedMinPwr,
       "combinedRadioFrequencyTable": combinedRadioFrequencyTable,
       "combinedRadioFreqTabEntry": combinedRadioFreqTabEntry,
       "combinedRadioFreqChannelId": combinedRadioFreqChannelId,
       "combinedRadioFreqChannelNum": combinedRadioFreqChannelNum,
       "combinedRadioFreqValue": combinedRadioFreqValue,
       "combinedRadioDuplexFrequencyTable": combinedRadioDuplexFrequencyTable,
       "combinedRadioDuplexFreqEntry": combinedRadioDuplexFreqEntry,
       "combinedRadioDuplexFreqId": combinedRadioDuplexFreqId,
       "combinedRadioDuplexFreqValue": combinedRadioDuplexFreqValue,
       "combinedRadioPowerScalingTable": combinedRadioPowerScalingTable,
       "combinedRadioPowerScalingEntry": combinedRadioPowerScalingEntry,
       "combinedRadioPowerScaling": combinedRadioPowerScaling,
       "combinedRadioAtpcRxPowerScaling": combinedRadioAtpcRxPowerScaling,
       "combinedRadioPowerRange": combinedRadioPowerRange,
       "stm1BulkMappingTable": stm1BulkMappingTable,
       "stm1BulkMappingEntry": stm1BulkMappingEntry,
       "stm1BulkPolIndex": stm1BulkPolIndex,
       "stm1BulkChanIndex": stm1BulkChanIndex,
       "stm1BulkChannel": stm1BulkChannel,
       "linkE1vsSTM1CapacityTable": linkE1vsSTM1CapacityTable,
       "linkE1vsSTM1CapacityEntry": linkE1vsSTM1CapacityEntry,
       "linkE1vsSTM1CapacityStm1": linkE1vsSTM1CapacityStm1,
       "linkE1vsSTM1CapacityE1": linkE1vsSTM1CapacityE1,
       "linkTfcV2Table": linkTfcV2Table,
       "linkTfcV2Entry": linkTfcV2Entry,
       "linkTfcV2Action": linkTfcV2Action,
       "linkTfcV2Control": linkTfcV2Control,
       "linkTfcV2WatchWindow": linkTfcV2WatchWindow,
       "linkTfcV2AlarmThreshold": linkTfcV2AlarmThreshold,
       "linkTfcV2Alarm": linkTfcV2Alarm,
       "linkTfcV2RowStatus": linkTfcV2RowStatus,
       "linkProV2Table": linkProV2Table,
       "linkProV2Entry": linkProV2Entry,
       "linkProV2ProtectionTxChIdx": linkProV2ProtectionTxChIdx,
       "linkProV2ProtectionRxChIdx": linkProV2ProtectionRxChIdx,
       "linkProV2TxWtrTime": linkProV2TxWtrTime,
       "linkProV2RxWtrTime": linkProV2RxWtrTime,
       "linkProV2TxSwitchedChIdx": linkProV2TxSwitchedChIdx,
       "linkProV2RxSwitchedChIdx": linkProV2RxSwitchedChIdx,
       "linkProV2TxRevertive": linkProV2TxRevertive,
       "linkProV2RxRevertive": linkProV2RxRevertive,
       "linkProV2ExtraTraffic": linkProV2ExtraTraffic,
       "linkProV2RowStatus": linkProV2RowStatus,
       "linkProMaintV2Table": linkProMaintV2Table,
       "linkProMaintV2Entry": linkProMaintV2Entry,
       "linkProMaintV2TxLockout": linkProMaintV2TxLockout,
       "linkProMaintV2RxLockout": linkProMaintV2RxLockout,
       "linkProMaintV2TxForced": linkProMaintV2TxForced,
       "linkProMaintV2RxForced": linkProMaintV2RxForced,
       "linkProMaintV2TxWtrReset": linkProMaintV2TxWtrReset,
       "linkProMaintV2RxWtrReset": linkProMaintV2RxWtrReset,
       "sspTable": sspTable,
       "sspEntry": sspEntry,
       "sspParameterType": sspParameterType,
       "sspLinkBandwidth": sspLinkBandwidth,
       "sspLinkModulation": sspLinkModulation,
       "sspLinkAcmEngineEnable": sspLinkAcmEngineEnable,
       "sspLinkTxUpperProfile": sspLinkTxUpperProfile,
       "sspLinkTxLowerProfile": sspLinkTxLowerProfile,
       "sspLinkSynchSetupProtocolEnable": sspLinkSynchSetupProtocolEnable,
       "sspLinkProfilesSetSelection": sspLinkProfilesSetSelection,
       "sspTdmE1Channel": sspTdmE1Channel,
       "sspTdmStm1Channel": sspTdmStm1Channel,
       "radioLoopCapabilityTable": radioLoopCapabilityTable,
       "radioLoopCapabilityEntry": radioLoopCapabilityEntry,
       "radioLoopRfGroup": radioLoopRfGroup,
       "radioLoopIqGroup": radioLoopIqGroup,
       "radioLoopBaseBandGroup": radioLoopBaseBandGroup,
       "radioRxBerThresholdTable": radioRxBerThresholdTable,
       "radioRxBerThresholdEntry": radioRxBerThresholdEntry,
       "radioRxBerThresholdStatus": radioRxBerThresholdStatus,
       "radioNominalRxBerThreshold": radioNominalRxBerThreshold,
       "radioMeasuredRxBerThreshold": radioMeasuredRxBerThreshold,
       "radioRemDemodulatorFailAlarmSeverityCode": radioRemDemodulatorFailAlarmSeverityCode,
       "radioRxActiveStatusTrapNotification": radioRxActiveStatusTrapNotification,
       "radioTxActiveStatusTrapNotification": radioTxActiveStatusTrapNotification,
       "radioCableOpenAlarmSeverityCode": radioCableOpenAlarmSeverityCode,
       "radioCableShortAlarmSeverityCode": radioCableShortAlarmSeverityCode,
       "radioInvalidFrequencyAlarmSeverityCode": radioInvalidFrequencyAlarmSeverityCode,
       "radioBaseBandRxAlarmSeverityCode": radioBaseBandRxAlarmSeverityCode,
       "radioModulatorFailAlarmSeverityCode": radioModulatorFailAlarmSeverityCode,
       "radioDemodulatorFailAlarmSeverityCode": radioDemodulatorFailAlarmSeverityCode,
       "radioRxPowerLowAlarmSeverityCode": radioRxPowerLowAlarmSeverityCode,
       "radioTxPowerLowAlarmSeverityCode": radioTxPowerLowAlarmSeverityCode,
       "radioVcoFailAlarmSeverityCode": radioVcoFailAlarmSeverityCode,
       "radioRxIFAgcAlarmSeverityCode": radioRxIFAgcAlarmSeverityCode,
       "radioTxIFAgcAlarmSeverityCode": radioTxIFAgcAlarmSeverityCode,
       "radioIduOduCommunicationAlarmSeverityCode": radioIduOduCommunicationAlarmSeverityCode,
       "radioOduIduCommunicationAlarmSeverityCode": radioOduIduCommunicationAlarmSeverityCode,
       "radioLocalOduAlarmSynthesisSeverityCode": radioLocalOduAlarmSynthesisSeverityCode,
       "radioRemoteOduAlarmSynthesisSeverityCode": radioRemoteOduAlarmSynthesisSeverityCode,
       "radioConfigMismatchAlarmSeverityCode": radioConfigMismatchAlarmSeverityCode,
       "radioPrxHysteresisValue": radioPrxHysteresisValue,
       "radioPtxHysteresisValue": radioPtxHysteresisValue,
       "radioPrxHysteresisValueTrapNotification": radioPrxHysteresisValueTrapNotification,
       "radioPtxHysteresisValueTrapNotification": radioPtxHysteresisValueTrapNotification,
       "radioRxQualityLowAlarmSeverityCode": radioRxQualityLowAlarmSeverityCode,
       "radioRxQualityWarningAlarmSeverityCode": radioRxQualityWarningAlarmSeverityCode,
       "linkReducedCapacityAlarmSeverityCode": linkReducedCapacityAlarmSeverityCode,
       "linkLinkTelemetryFailAlarmSeverityCode": linkLinkTelemetryFailAlarmSeverityCode,
       "linkIdMismatchAlarmSeverityCode": linkIdMismatchAlarmSeverityCode,
       "linkRadioEocAlarmSeverityCode": linkRadioEocAlarmSeverityCode,
       "linkSetupMismatchAlarmSeverityCode": linkSetupMismatchAlarmSeverityCode,
       "linkRescueSetupAlarmSeverityCode": linkRescueSetupAlarmSeverityCode,
       "linkXpicProcedureBlockAlarmSeverityCode": linkXpicProcedureBlockAlarmSeverityCode,
       "linkXpicRemTxOffAlarmAlarmSeverityCode": linkXpicRemTxOffAlarmAlarmSeverityCode,
       "linkLocalIduAlarmSynthesis": linkLocalIduAlarmSynthesis,
       "linkLocalIduAlarmSynthesisSeverityCode": linkLocalIduAlarmSynthesisSeverityCode,
       "linkRemoteIduAlarmSynthesisSeverityCode": linkRemoteIduAlarmSynthesisSeverityCode,
       "linkTfcAlarmSeverityCode": linkTfcAlarmSeverityCode,
       "linkBerSyncLossAlarmSeverityCode": linkBerSyncLossAlarmSeverityCode,
       "linkNotMatchingRadiosAlarmSeverityCode": linkNotMatchingRadiosAlarmSeverityCode,
       "channelSpacingSelection": channelSpacingSelection,
       "fadeMarginMeasure": fadeMarginMeasure,
       "linkConfigurationInProgressTrapNotification": linkConfigurationInProgressTrapNotification}
)
