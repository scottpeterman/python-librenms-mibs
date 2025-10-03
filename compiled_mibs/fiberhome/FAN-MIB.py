# SNMP MIB module (FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fiberhome\FAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:11 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(wri,
 wriProducts) = mibBuilder.importSymbols(
    "WRI-SMI",
    "wri",
    "wriProducts")


# MODULE-IDENTITY

msppFan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11)
)
if mibBuilder.loadTexts:
    msppFan.setRevisions(
        ("2010-01-11 00:00",
         "2009-01-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EntryStatus(TextualConvention, Integer32):
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Mspp_ObjectIdentity = ObjectIdentity
mspp = _Mspp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012)
)
_MsppChassis_ObjectIdentity = ObjectIdentity
msppChassis = _MsppChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1)
)
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 1)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 1, 1)
)
fanEntry.setIndexNames(
    (0, "FAN-MIB", "fanIndex"),
    (0, "FAN-MIB", "fanCtrlNumIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")


class _FanIndex_Type(Integer32):
    """Custom type fanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_FanIndex_Type.__name__ = "Integer32"
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 1, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanIndex.setStatus("current")
_FanCtrlNumIndex_Type = Unsigned32
_FanCtrlNumIndex_Object = MibTableColumn
fanCtrlNumIndex = _FanCtrlNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 1, 1, 2),
    _FanCtrlNumIndex_Type()
)
fanCtrlNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCtrlNumIndex.setStatus("current")
_FanSpeed_Type = Integer32
_FanSpeed_Object = MibTableColumn
fanSpeed = _FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 1, 1, 3),
    _FanSpeed_Type()
)
fanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanSpeed.setStatus("current")
_FanLThreshold_Type = Integer32
_FanLThreshold_Object = MibTableColumn
fanLThreshold = _FanLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 1, 1, 4),
    _FanLThreshold_Type()
)
fanLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanLThreshold.setStatus("current")
_FanHThreshold_Type = Integer32
_FanHThreshold_Object = MibTableColumn
fanHThreshold = _FanHThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 1, 1, 5),
    _FanHThreshold_Type()
)
fanHThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanHThreshold.setStatus("current")
_FanState_Type = Integer32
_FanState_Object = MibTableColumn
fanState = _FanState_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 1, 1, 6),
    _FanState_Type()
)
fanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanState.setStatus("current")
_FanCtrlId_Type = Integer32
_FanCtrlId_Object = MibTableColumn
fanCtrlId = _FanCtrlId_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 1, 1, 7),
    _FanCtrlId_Type()
)
fanCtrlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCtrlId.setStatus("current")
_FanTrap_ObjectIdentity = ObjectIdentity
fanTrap = _FanTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 2)
)
_FanGeneral_ObjectIdentity = ObjectIdentity
fanGeneral = _FanGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 3)
)
_FanBits_Type = Counter32
_FanBits_Object = MibScalar
fanBits = _FanBits_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 3, 1),
    _FanBits_Type()
)
fanBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanBits.setStatus("current")
_FanNum_Type = Integer32
_FanNum_Object = MibScalar
fanNum = _FanNum_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 3, 2),
    _FanNum_Type()
)
fanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNum.setStatus("current")


class _FanTrapEnable_Type(Integer32):
    """Custom type fanTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FanTrapEnable_Type.__name__ = "Integer32"
_FanTrapEnable_Object = MibScalar
fanTrapEnable = _FanTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 3, 3),
    _FanTrapEnable_Type()
)
fanTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanTrapEnable.setStatus("current")


class _FanMonitorEnable_Type(Integer32):
    """Custom type fanMonitorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FanMonitorEnable_Type.__name__ = "Integer32"
_FanMonitorEnable_Object = MibScalar
fanMonitorEnable = _FanMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 3, 4),
    _FanMonitorEnable_Type()
)
fanMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanMonitorEnable.setStatus("current")
_FanCtrlTable_Object = MibTable
fanCtrlTable = _FanCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4)
)
if mibBuilder.loadTexts:
    fanCtrlTable.setStatus("current")
_FanCtrlEntry_Object = MibTableRow
fanCtrlEntry = _FanCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4, 1)
)
fanCtrlEntry.setIndexNames(
    (0, "FAN-MIB", "fanCtrlIndex"),
)
if mibBuilder.loadTexts:
    fanCtrlEntry.setStatus("current")
_FanCtrlIndex_Type = Unsigned32
_FanCtrlIndex_Object = MibTableColumn
fanCtrlIndex = _FanCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4, 1, 1),
    _FanCtrlIndex_Type()
)
fanCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCtrlIndex.setStatus("current")
_FanCtrlSpeed_Type = Integer32
_FanCtrlSpeed_Object = MibTableColumn
fanCtrlSpeed = _FanCtrlSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4, 1, 2),
    _FanCtrlSpeed_Type()
)
fanCtrlSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanCtrlSpeed.setStatus("current")
_FanCtrlLThreshold_Type = Integer32
_FanCtrlLThreshold_Object = MibTableColumn
fanCtrlLThreshold = _FanCtrlLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4, 1, 3),
    _FanCtrlLThreshold_Type()
)
fanCtrlLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanCtrlLThreshold.setStatus("current")
_FanCtrlHThreshold_Type = Integer32
_FanCtrlHThreshold_Object = MibTableColumn
fanCtrlHThreshold = _FanCtrlHThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4, 1, 4),
    _FanCtrlHThreshold_Type()
)
fanCtrlHThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanCtrlHThreshold.setStatus("current")


class _FanCtrlState_Type(Integer32):
    """Custom type fanCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("highoverflow", 1),
          ("lowunderflow", 2),
          ("counteroverflow", 4))
    )


_FanCtrlState_Type.__name__ = "Integer32"
_FanCtrlState_Object = MibTableColumn
fanCtrlState = _FanCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4, 1, 5),
    _FanCtrlState_Type()
)
fanCtrlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCtrlState.setStatus("current")
_FanCtrlSerial_Type = OctetString
_FanCtrlSerial_Object = MibTableColumn
fanCtrlSerial = _FanCtrlSerial_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4, 1, 6),
    _FanCtrlSerial_Type()
)
fanCtrlSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCtrlSerial.setStatus("current")
_FanCtrlDescr_Type = OctetString
_FanCtrlDescr_Object = MibTableColumn
fanCtrlDescr = _FanCtrlDescr_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4, 1, 7),
    _FanCtrlDescr_Type()
)
fanCtrlDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanCtrlDescr.setStatus("current")


class _FanCtrlTrapEnable_Type(Integer32):
    """Custom type fanCtrlTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FanCtrlTrapEnable_Type.__name__ = "Integer32"
_FanCtrlTrapEnable_Object = MibTableColumn
fanCtrlTrapEnable = _FanCtrlTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4, 1, 8),
    _FanCtrlTrapEnable_Type()
)
fanCtrlTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanCtrlTrapEnable.setStatus("current")


class _FanCtrlType_Type(Integer32):
    """Custom type fanCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dc", 0),
          ("reserved", 1))
    )


_FanCtrlType_Type.__name__ = "Integer32"
_FanCtrlType_Object = MibTableColumn
fanCtrlType = _FanCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4, 1, 9),
    _FanCtrlType_Type()
)
fanCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCtrlType.setStatus("current")


class _FanCtrlMode_Type(Integer32):
    """Custom type fanCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixedspeed", 1),
          ("temperatureControl", 2),
          ("temperatureControlEx", 3))
    )


_FanCtrlMode_Type.__name__ = "Integer32"
_FanCtrlMode_Object = MibTableColumn
fanCtrlMode = _FanCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4, 1, 10),
    _FanCtrlMode_Type()
)
fanCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanCtrlMode.setStatus("current")
_FanCtrlAllSetting_Type = OctetString
_FanCtrlAllSetting_Object = MibTableColumn
fanCtrlAllSetting = _FanCtrlAllSetting_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4, 1, 11),
    _FanCtrlAllSetting_Type()
)
fanCtrlAllSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanCtrlAllSetting.setStatus("current")
_FanCtrlIndexDescr_Type = OctetString
_FanCtrlIndexDescr_Object = MibTableColumn
fanCtrlIndexDescr = _FanCtrlIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 4, 1, 12),
    _FanCtrlIndexDescr_Type()
)
fanCtrlIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCtrlIndexDescr.setStatus("current")
_FanTmprtrCtrlTable_Object = MibTable
fanTmprtrCtrlTable = _FanTmprtrCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 5)
)
if mibBuilder.loadTexts:
    fanTmprtrCtrlTable.setStatus("current")
_FanTmprtrCtrlEntry_Object = MibTableRow
fanTmprtrCtrlEntry = _FanTmprtrCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 5, 1)
)
fanTmprtrCtrlEntry.setIndexNames(
    (0, "FAN-MIB", "fanCtrlIndex"),
    (0, "FAN-MIB", "fanTemperatureVaule"),
)
if mibBuilder.loadTexts:
    fanTmprtrCtrlEntry.setStatus("current")


class _FanTemperatureVaule_Type(Integer32):
    """Custom type fanTemperatureVaule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FanTemperatureVaule_Type.__name__ = "Integer32"
_FanTemperatureVaule_Object = MibTableColumn
fanTemperatureVaule = _FanTemperatureVaule_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 5, 1, 1),
    _FanTemperatureVaule_Type()
)
fanTemperatureVaule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanTemperatureVaule.setStatus("current")
_FanTemperatureSpeed_Type = Integer32
_FanTemperatureSpeed_Object = MibTableColumn
fanTemperatureSpeed = _FanTemperatureSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 5, 1, 2),
    _FanTemperatureSpeed_Type()
)
fanTemperatureSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanTemperatureSpeed.setStatus("current")
_FanTemperatureStatus_Type = EntryStatus
_FanTemperatureStatus_Object = MibTableColumn
fanTemperatureStatus = _FanTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 5, 1, 3),
    _FanTemperatureStatus_Type()
)
fanTemperatureStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanTemperatureStatus.setStatus("current")

# Managed Objects groups


# Notification objects

fanUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 2, 1)
)
fanUp.setObjects(
    ("FAN-MIB", "fanCtrlState")
)
if mibBuilder.loadTexts:
    fanUp.setStatus(
        "current"
    )

fanDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 2, 2)
)
fanDown.setObjects(
    ("FAN-MIB", "fanCtrlState")
)
if mibBuilder.loadTexts:
    fanDown.setStatus(
        "current"
    )

fanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 2, 3)
)
fanOk.setObjects(
    ("FAN-MIB", "fanCtrlState")
)
if mibBuilder.loadTexts:
    fanOk.setStatus(
        "current"
    )

fanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 11, 2, 4)
)
fanFault.setObjects(
    ("FAN-MIB", "fanCtrlState")
)
if mibBuilder.loadTexts:
    fanFault.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FAN-MIB",
    **{"EntryStatus": EntryStatus,
       "mspp": mspp,
       "msppChassis": msppChassis,
       "msppFan": msppFan,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanIndex": fanIndex,
       "fanCtrlNumIndex": fanCtrlNumIndex,
       "fanSpeed": fanSpeed,
       "fanLThreshold": fanLThreshold,
       "fanHThreshold": fanHThreshold,
       "fanState": fanState,
       "fanCtrlId": fanCtrlId,
       "fanTrap": fanTrap,
       "fanUp": fanUp,
       "fanDown": fanDown,
       "fanOk": fanOk,
       "fanFault": fanFault,
       "fanGeneral": fanGeneral,
       "fanBits": fanBits,
       "fanNum": fanNum,
       "fanTrapEnable": fanTrapEnable,
       "fanMonitorEnable": fanMonitorEnable,
       "fanCtrlTable": fanCtrlTable,
       "fanCtrlEntry": fanCtrlEntry,
       "fanCtrlIndex": fanCtrlIndex,
       "fanCtrlSpeed": fanCtrlSpeed,
       "fanCtrlLThreshold": fanCtrlLThreshold,
       "fanCtrlHThreshold": fanCtrlHThreshold,
       "fanCtrlState": fanCtrlState,
       "fanCtrlSerial": fanCtrlSerial,
       "fanCtrlDescr": fanCtrlDescr,
       "fanCtrlTrapEnable": fanCtrlTrapEnable,
       "fanCtrlType": fanCtrlType,
       "fanCtrlMode": fanCtrlMode,
       "fanCtrlAllSetting": fanCtrlAllSetting,
       "fanCtrlIndexDescr": fanCtrlIndexDescr,
       "fanTmprtrCtrlTable": fanTmprtrCtrlTable,
       "fanTmprtrCtrlEntry": fanTmprtrCtrlEntry,
       "fanTemperatureVaule": fanTemperatureVaule,
       "fanTemperatureSpeed": fanTemperatureSpeed,
       "fanTemperatureStatus": fanTemperatureStatus}
)
