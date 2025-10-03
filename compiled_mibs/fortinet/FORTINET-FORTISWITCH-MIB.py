# SNMP MIB module (FORTINET-FORTISWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\FORTINET-FORTISWITCH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:55 2025
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

(dot1dTpFdbAddress,
 dot1dTpFdbPort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dTpFdbAddress",
    "dot1dTpFdbPort")

(fnSysSerial,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "fnSysSerial",
    "fortinet")

(ifName,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifName")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fnFortiSwitchMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106)
)
if mibBuilder.loadTexts:
    fnFortiSwitchMib.setRevisions(
        ("2022-04-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsCommon_ObjectIdentity = ObjectIdentity
fsCommon = _FsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 1)
)
_FsSys_ObjectIdentity = ObjectIdentity
fsSys = _FsSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 1, 1)
)
_FsSysSerial_Type = DisplayString
_FsSysSerial_Object = MibScalar
fsSysSerial = _FsSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 1, 1, 1),
    _FsSysSerial_Type()
)
fsSysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSysSerial.setStatus("current")
_FsTraps_ObjectIdentity = ObjectIdentity
fsTraps = _FsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2)
)
_FsTrapPrefix_ObjectIdentity = ObjectIdentity
fsTrapPrefix = _FsTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0)
)
_FsTrapObjects_ObjectIdentity = ObjectIdentity
fsTrapObjects = _FsTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1)
)
_FsLlvTrapMsg_Type = DisplayString
_FsLlvTrapMsg_Object = MibScalar
fsLlvTrapMsg = _FsLlvTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 1),
    _FsLlvTrapMsg_Type()
)
fsLlvTrapMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsLlvTrapMsg.setStatus("current")
_FsLearningTrapVid_Type = Integer32
_FsLearningTrapVid_Object = MibScalar
fsLearningTrapVid = _FsLearningTrapVid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 2),
    _FsLearningTrapVid_Type()
)
fsLearningTrapVid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsLearningTrapVid.setStatus("current")


class _FsLearningTrapType_Type(Integer32):
    """Custom type fsLearningTrapType based on Integer32"""
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
        *(("add", 1),
          ("delete", 2),
          ("movefrom", 3),
          ("moveto", 4))
    )


_FsLearningTrapType_Type.__name__ = "Integer32"
_FsLearningTrapType_Object = MibScalar
fsLearningTrapType = _FsLearningTrapType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 3),
    _FsLearningTrapType_Type()
)
fsLearningTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsLearningTrapType.setStatus("current")
_FsSensorName_Type = DisplayString
_FsSensorName_Object = MibScalar
fsSensorName = _FsSensorName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 4),
    _FsSensorName_Type()
)
fsSensorName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSensorName.setStatus("current")


class _FsSensorType_Type(Integer32):
    """Custom type fsSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("temperature", 1),
          ("poe", 2),
          ("cpu", 3),
          ("memory", 4),
          ("disk", 6))
    )


_FsSensorType_Type.__name__ = "Integer32"
_FsSensorType_Object = MibScalar
fsSensorType = _FsSensorType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 5),
    _FsSensorType_Type()
)
fsSensorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSensorType.setStatus("current")
_FsSensorIdx_Type = Integer32
_FsSensorIdx_Object = MibScalar
fsSensorIdx = _FsSensorIdx_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 6),
    _FsSensorIdx_Type()
)
fsSensorIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSensorIdx.setStatus("current")


class _FsSensorFanEventType_Type(Integer32):
    """Custom type fsSensorFanEventType based on Integer32"""
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
        *(("detected", 1),
          ("undetected", 2),
          ("resumed", 3),
          ("failure", 4))
    )


_FsSensorFanEventType_Type.__name__ = "Integer32"
_FsSensorFanEventType_Object = MibScalar
fsSensorFanEventType = _FsSensorFanEventType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 7),
    _FsSensorFanEventType_Type()
)
fsSensorFanEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSensorFanEventType.setStatus("current")


class _FsSensorPsuEventType_Type(Integer32):
    """Custom type fsSensorPsuEventType based on Integer32"""
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
        *(("up", 1),
          ("connected", 2),
          ("good", 3),
          ("down", 4),
          ("disconnected", 5),
          ("bad", 6))
    )


_FsSensorPsuEventType_Type.__name__ = "Integer32"
_FsSensorPsuEventType_Object = MibScalar
fsSensorPsuEventType = _FsSensorPsuEventType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 8),
    _FsSensorPsuEventType_Type()
)
fsSensorPsuEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSensorPsuEventType.setStatus("current")


class _FsAlarmEventType_Type(Integer32):
    """Custom type fsAlarmEventType based on Integer32"""
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
        *(("inrange", 1),
          ("warning", 2),
          ("outofrange", 3),
          ("cleared", 4))
    )


_FsAlarmEventType_Type.__name__ = "Integer32"
_FsAlarmEventType_Object = MibScalar
fsAlarmEventType = _FsAlarmEventType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 9),
    _FsAlarmEventType_Type()
)
fsAlarmEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsAlarmEventType.setStatus("current")
_FsAlarmThresholdValue_Type = Integer32
_FsAlarmThresholdValue_Object = MibScalar
fsAlarmThresholdValue = _FsAlarmThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 10),
    _FsAlarmThresholdValue_Type()
)
fsAlarmThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsAlarmThresholdValue.setStatus("current")


class _FsAlarmThresholdUnits_Type(Integer32):
    """Custom type fsAlarmThresholdUnits based on Integer32"""
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
        *(("celcius", 1),
          ("watts", 2),
          ("percentage", 3),
          ("unknown", 4))
    )


_FsAlarmThresholdUnits_Type.__name__ = "Integer32"
_FsAlarmThresholdUnits_Object = MibScalar
fsAlarmThresholdUnits = _FsAlarmThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 11),
    _FsAlarmThresholdUnits_Type()
)
fsAlarmThresholdUnits.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsAlarmThresholdUnits.setStatus("current")
_FsIpAddress_Type = IpAddress
_FsIpAddress_Object = MibScalar
fsIpAddress = _FsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 12),
    _FsIpAddress_Type()
)
fsIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsIpAddress.setStatus("current")


class _FsJsonString_Type(OctetString):
    """Custom type fsJsonString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1360),
    )


_FsJsonString_Type.__name__ = "OctetString"
_FsJsonString_Object = MibScalar
fsJsonString = _FsJsonString_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 13),
    _FsJsonString_Type()
)
fsJsonString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsJsonString.setStatus("current")
_FsSwitchStormContrl_Type = DisplayString
_FsSwitchStormContrl_Object = MibScalar
fsSwitchStormContrl = _FsSwitchStormContrl_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 1, 14),
    _FsSwitchStormContrl_Type()
)
fsSwitchStormContrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSwitchStormContrl.setStatus("current")
_FsTrunkMemPrefix_ObjectIdentity = ObjectIdentity
fsTrunkMemPrefix = _FsTrunkMemPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 3)
)


class _FsTrunkMember_Type(DisplayString):
    """Custom type fsTrunkMember based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 82),
    )


_FsTrunkMember_Type.__name__ = "DisplayString"
_FsTrunkMember_Object = MibScalar
fsTrunkMember = _FsTrunkMember_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 3, 1),
    _FsTrunkMember_Type()
)
fsTrunkMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrunkMember.setStatus("current")
_FsSystem_ObjectIdentity = ObjectIdentity
fsSystem = _FsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4)
)
_FsSystemInfo_ObjectIdentity = ObjectIdentity
fsSystemInfo = _FsSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1)
)


class _FsSysVersion_Type(DisplayString):
    """Custom type fsSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsSysVersion_Type.__name__ = "DisplayString"
_FsSysVersion_Object = MibScalar
fsSysVersion = _FsSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1, 1),
    _FsSysVersion_Type()
)
fsSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSysVersion.setStatus("current")


class _FsSysCpuUsage_Type(Gauge32):
    """Custom type fsSysCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsSysCpuUsage_Type.__name__ = "Gauge32"
_FsSysCpuUsage_Object = MibScalar
fsSysCpuUsage = _FsSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1, 2),
    _FsSysCpuUsage_Type()
)
fsSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSysCpuUsage.setStatus("current")
_FsSysMemUsage_Type = Gauge32
_FsSysMemUsage_Object = MibScalar
fsSysMemUsage = _FsSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1, 3),
    _FsSysMemUsage_Type()
)
fsSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSysMemUsage.setStatus("current")
_FsSysMemCapacity_Type = Gauge32
_FsSysMemCapacity_Object = MibScalar
fsSysMemCapacity = _FsSysMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1, 4),
    _FsSysMemCapacity_Type()
)
fsSysMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSysMemCapacity.setStatus("current")
_FsSysDiskUsage_Type = Gauge32
_FsSysDiskUsage_Object = MibScalar
fsSysDiskUsage = _FsSysDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1, 5),
    _FsSysDiskUsage_Type()
)
fsSysDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSysDiskUsage.setStatus("current")
_FsSysDiskCapacity_Type = Gauge32
_FsSysDiskCapacity_Object = MibScalar
fsSysDiskCapacity = _FsSysDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 106, 4, 1, 6),
    _FsSysDiskCapacity_Type()
)
fsSysDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSysDiskCapacity.setStatus("current")
_FsModel_ObjectIdentity = ObjectIdentity
fsModel = _FsModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5)
)
_Fs24vm_ObjectIdentity = ObjectIdentity
fs24vm = _Fs24vm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 241)
)
_Fs108d_ObjectIdentity = ObjectIdentity
fs108d = _Fs108d_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1081)
)
_S108en_ObjectIdentity = ObjectIdentity
s108en = _S108en_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1082)
)
_S108ep_ObjectIdentity = ObjectIdentity
s108ep = _S108ep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1083)
)
_S108ef_ObjectIdentity = ObjectIdentity
s108ef = _S108ef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1084)
)
_S108dv_ObjectIdentity = ObjectIdentity
s108dv = _S108dv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1085)
)
_S108fn_ObjectIdentity = ObjectIdentity
s108fn = _S108fn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1086)
)
_S108fp_ObjectIdentity = ObjectIdentity
s108fp = _S108fp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1087)
)
_S108ff_ObjectIdentity = ObjectIdentity
s108ff = _S108ff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1088)
)
_Sm10gf_ObjectIdentity = ObjectIdentity
sm10gf = _Sm10gf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1102)
)
_Sr12dp_ObjectIdentity = ObjectIdentity
sr12dp = _Sr12dp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1121)
)
_S124dn_ObjectIdentity = ObjectIdentity
s124dn = _S124dn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1241)
)
_S124dp_ObjectIdentity = ObjectIdentity
s124dp = _S124dp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1242)
)
_Sr24dn_ObjectIdentity = ObjectIdentity
sr24dn = _Sr24dn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1243)
)
_S124en_ObjectIdentity = ObjectIdentity
s124en = _S124en_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1244)
)
_S124ep_ObjectIdentity = ObjectIdentity
s124ep = _S124ep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1245)
)
_S124ef_ObjectIdentity = ObjectIdentity
s124ef = _S124ef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1246)
)
_S148en_ObjectIdentity = ObjectIdentity
s148en = _S148en_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1247)
)
_S148ep_ObjectIdentity = ObjectIdentity
s148ep = _S148ep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1248)
)
_S124ff_ObjectIdentity = ObjectIdentity
s124ff = _S124ff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1249)
)
_S148fn_ObjectIdentity = ObjectIdentity
s148fn = _S148fn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1484)
)
_S148fp_ObjectIdentity = ObjectIdentity
s148fp = _S148fp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1485)
)
_S148ff_ObjectIdentity = ObjectIdentity
s148ff = _S148ff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 1486)
)
_Sr16fp_ObjectIdentity = ObjectIdentity
sr16fp = _Sr16fp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 2161)
)
_Fs224d_ObjectIdentity = ObjectIdentity
fs224d = _Fs224d_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 2241)
)
_S224df_ObjectIdentity = ObjectIdentity
s224df = _S224df_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 2242)
)
_S224en_ObjectIdentity = ObjectIdentity
s224en = _S224en_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 2243)
)
_S224ep_ObjectIdentity = ObjectIdentity
s224ep = _S224ep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 2244)
)
_S248dp_ObjectIdentity = ObjectIdentity
s248dp = _S248dp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 2481)
)
_S248df_ObjectIdentity = ObjectIdentity
s248df = _S248df_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 2482)
)
_S248dn_ObjectIdentity = ObjectIdentity
s248dn = _S248dn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 2483)
)
_S248ef_ObjectIdentity = ObjectIdentity
s248ef = _S248ef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 2484)
)
_S248ep_ObjectIdentity = ObjectIdentity
s248ep = _S248ep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 2485)
)
_S424dn_ObjectIdentity = ObjectIdentity
s424dn = _S424dn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 4241)
)
_S424dp_ObjectIdentity = ObjectIdentity
s424dp = _S424dp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 4242)
)
_S424df_ObjectIdentity = ObjectIdentity
s424df = _S424df_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 4243)
)
_S448dn_ObjectIdentity = ObjectIdentity
s448dn = _S448dn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 4482)
)
_S448df_ObjectIdentity = ObjectIdentity
s448df = _S448df_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 4483)
)
_S448dp_ObjectIdentity = ObjectIdentity
s448dp = _S448dp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 4484)
)
_S448en_ObjectIdentity = ObjectIdentity
s448en = _S448en_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 4485)
)
_S448ep_ObjectIdentity = ObjectIdentity
s448ep = _S448ep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 4486)
)
_S448ef_ObjectIdentity = ObjectIdentity
s448ef = _S448ef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 4487)
)
_S524df_ObjectIdentity = ObjectIdentity
s524df = _S524df_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 5241)
)
_S524dn_ObjectIdentity = ObjectIdentity
s524dn = _S524dn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 5242)
)
_S548df_ObjectIdentity = ObjectIdentity
s548df = _S548df_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 5481)
)
_S548dn_ObjectIdentity = ObjectIdentity
s548dn = _S548dn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 5482)
)
_S624fn_ObjectIdentity = ObjectIdentity
s624fn = _S624fn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 6241)
)
_S624ff_ObjectIdentity = ObjectIdentity
s624ff = _S624ff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 6242)
)
_S648fn_ObjectIdentity = ObjectIdentity
s648fn = _S648fn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 6481)
)
_S648ff_ObjectIdentity = ObjectIdentity
s648ff = _S648ff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 6482)
)
_Fs1d24_ObjectIdentity = ObjectIdentity
fs1d24 = _Fs1d24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 10241)
)
_Fs1e24_ObjectIdentity = ObjectIdentity
fs1e24 = _Fs1e24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 10242)
)
_St1e24_ObjectIdentity = ObjectIdentity
st1e24 = _St1e24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 10243)
)
_Tf1f24_ObjectIdentity = ObjectIdentity
tf1f24 = _Tf1f24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 10244)
)
_Fs1d48_ObjectIdentity = ObjectIdentity
fs1d48 = _Fs1d48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 10481)
)
_Fs1e48_ObjectIdentity = ObjectIdentity
fs1e48 = _Fs1e48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 10482)
)
_S124fn_ObjectIdentity = ObjectIdentity
s124fn = _S124fn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 12410)
)
_S124fp_ObjectIdentity = ObjectIdentity
s124fp = _S124fp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 12411)
)
_Sm24gn_ObjectIdentity = ObjectIdentity
sm24gn = _Sm24gn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 12412)
)
_Sm24gf_ObjectIdentity = ObjectIdentity
sm24gf = _Sm24gf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 12413)
)
_Fs2f48_ObjectIdentity = ObjectIdentity
fs2f48 = _Fs2f48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 20481)
)
_Fs3d32_ObjectIdentity = ObjectIdentity
fs3d32 = _Fs3d32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 30321)
)
_Fs3e32_ObjectIdentity = ObjectIdentity
fs3e32 = _Fs3e32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 30322)
)
_S424en_ObjectIdentity = ObjectIdentity
s424en = _S424en_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 42401)
)
_S424ep_ObjectIdentity = ObjectIdentity
s424ep = _S424ep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 42402)
)
_S424ef_ObjectIdentity = ObjectIdentity
s424ef = _S424ef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 42403)
)
_S424ei_ObjectIdentity = ObjectIdentity
s424ei = _S424ei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 42404)
)
_S426ef_ObjectIdentity = ObjectIdentity
s426ef = _S426ef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 42405)
)
_Sr24fp_ObjectIdentity = ObjectIdentity
sr24fp = _Sr24fp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 5, 42406)
)
_FsMibConformance_ObjectIdentity = ObjectIdentity
fsMibConformance = _FsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 106, 100)
)

# Managed Objects groups

fsSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 106, 100, 2)
)
fsSystemObjectGroup.setObjects(
      *(("FORTINET-FORTISWITCH-MIB", "fsSysVersion"),
        ("FORTINET-FORTISWITCH-MIB", "fsSysCpuUsage"),
        ("FORTINET-FORTISWITCH-MIB", "fsSysMemUsage"),
        ("FORTINET-FORTISWITCH-MIB", "fsSysMemCapacity"),
        ("FORTINET-FORTISWITCH-MIB", "fsSysDiskUsage"),
        ("FORTINET-FORTISWITCH-MIB", "fsSysDiskCapacity"))
)
if mibBuilder.loadTexts:
    fsSystemObjectGroup.setStatus("current")

fsTrunkObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 106, 100, 3)
)
fsTrunkObjectGroup.setObjects(
    ("FORTINET-FORTISWITCH-MIB", "fsTrunkMember")
)
if mibBuilder.loadTexts:
    fsTrunkObjectGroup.setStatus("current")


# Notification objects

fsTrapMemberDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 703)
)
fsTrapMemberDown.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsTrunkMember"))
)
if mibBuilder.loadTexts:
    fsTrapMemberDown.setStatus(
        "current"
    )

fsTrapMemberUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 704)
)
fsTrapMemberUp.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsTrunkMember"))
)
if mibBuilder.loadTexts:
    fsTrapMemberUp.setStatus(
        "current"
    )

fsTrapLlvViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 705)
)
fsTrapLlvViolation.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsLlvTrapMsg"))
)
if mibBuilder.loadTexts:
    fsTrapLlvViolation.setStatus(
        "current"
    )

fsTrapLearningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 706)
)
fsTrapLearningEvent.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("BRIDGE-MIB", "dot1dTpFdbAddress"),
        ("FORTINET-FORTISWITCH-MIB", "fsLearningTrapVid"),
        ("BRIDGE-MIB", "dot1dTpFdbPort"),
        ("FORTINET-FORTISWITCH-MIB", "fsLearningTrapType"))
)
if mibBuilder.loadTexts:
    fsTrapLearningEvent.setStatus(
        "current"
    )

fsTrapSensorFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 707)
)
fsTrapSensorFault.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsSensorName"),
        ("FORTINET-FORTISWITCH-MIB", "fsSensorType"))
)
if mibBuilder.loadTexts:
    fsTrapSensorFault.setStatus(
        "current"
    )

fsTrapSensorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 708)
)
fsTrapSensorAlarm.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsSensorName"),
        ("FORTINET-FORTISWITCH-MIB", "fsSensorType"),
        ("FORTINET-FORTISWITCH-MIB", "fsAlarmEventType"),
        ("FORTINET-FORTISWITCH-MIB", "fsAlarmThresholdValue"),
        ("FORTINET-FORTISWITCH-MIB", "fsAlarmThresholdUnits"))
)
if mibBuilder.loadTexts:
    fsTrapSensorAlarm.setStatus(
        "current"
    )

fsTrapFanDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 709)
)
fsTrapFanDetect.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsSensorIdx"),
        ("FORTINET-FORTISWITCH-MIB", "fsSensorFanEventType"))
)
if mibBuilder.loadTexts:
    fsTrapFanDetect.setStatus(
        "current"
    )

fsTrapPsuStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 710)
)
fsTrapPsuStatus.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsSensorIdx"),
        ("FORTINET-FORTISWITCH-MIB", "fsSensorPsuEventType"))
)
if mibBuilder.loadTexts:
    fsTrapPsuStatus.setStatus(
        "current"
    )

fsTrapStormControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 711)
)
fsTrapStormControl.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsSwitchStormContrl"))
)
if mibBuilder.loadTexts:
    fsTrapStormControl.setStatus(
        "current"
    )

fsTrapIpConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 801)
)
fsTrapIpConflict.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsIpAddress"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    fsTrapIpConflict.setStatus(
        "current"
    )

fsTrapTrunkMemberHBOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 802)
)
fsTrapTrunkMemberHBOutOfSync.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    fsTrapTrunkMemberHBOutOfSync.setStatus(
        "current"
    )

fsTrapStitch1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 901)
)
fsTrapStitch1.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsJsonString"))
)
if mibBuilder.loadTexts:
    fsTrapStitch1.setStatus(
        "current"
    )

fsTrapStitch2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 902)
)
fsTrapStitch2.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsJsonString"))
)
if mibBuilder.loadTexts:
    fsTrapStitch2.setStatus(
        "current"
    )

fsTrapStitch3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 903)
)
fsTrapStitch3.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsJsonString"))
)
if mibBuilder.loadTexts:
    fsTrapStitch3.setStatus(
        "current"
    )

fsTrapStitch4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 904)
)
fsTrapStitch4.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsJsonString"))
)
if mibBuilder.loadTexts:
    fsTrapStitch4.setStatus(
        "current"
    )

fsTrapStitch5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 106, 2, 0, 905)
)
fsTrapStitch5.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTISWITCH-MIB", "fsJsonString"))
)
if mibBuilder.loadTexts:
    fsTrapStitch5.setStatus(
        "current"
    )


# Notifications groups

fsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 106, 100, 1)
)
fsNotificationGroup.setObjects(
      *(("FORTINET-FORTISWITCH-MIB", "fsTrapMemberDown"),
        ("FORTINET-FORTISWITCH-MIB", "fsTrapMemberUp"))
)
if mibBuilder.loadTexts:
    fsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 106, 100, 100)
)
fsMIBCompliance.setObjects(
      *(("FORTINET-FORTISWITCH-MIB", "fsNotificationGroup"),
        ("FORTINET-FORTISWITCH-MIB", "fsSystemObjectGroup"),
        ("FORTINET-FORTISWITCH-MIB", "fsTrunkObjectGroup"))
)
if mibBuilder.loadTexts:
    fsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTISWITCH-MIB",
    **{"fnFortiSwitchMib": fnFortiSwitchMib,
       "fsCommon": fsCommon,
       "fsSys": fsSys,
       "fsSysSerial": fsSysSerial,
       "fsTraps": fsTraps,
       "fsTrapPrefix": fsTrapPrefix,
       "fsTrapMemberDown": fsTrapMemberDown,
       "fsTrapMemberUp": fsTrapMemberUp,
       "fsTrapLlvViolation": fsTrapLlvViolation,
       "fsTrapLearningEvent": fsTrapLearningEvent,
       "fsTrapSensorFault": fsTrapSensorFault,
       "fsTrapSensorAlarm": fsTrapSensorAlarm,
       "fsTrapFanDetect": fsTrapFanDetect,
       "fsTrapPsuStatus": fsTrapPsuStatus,
       "fsTrapStormControl": fsTrapStormControl,
       "fsTrapIpConflict": fsTrapIpConflict,
       "fsTrapTrunkMemberHBOutOfSync": fsTrapTrunkMemberHBOutOfSync,
       "fsTrapStitch1": fsTrapStitch1,
       "fsTrapStitch2": fsTrapStitch2,
       "fsTrapStitch3": fsTrapStitch3,
       "fsTrapStitch4": fsTrapStitch4,
       "fsTrapStitch5": fsTrapStitch5,
       "fsTrapObjects": fsTrapObjects,
       "fsLlvTrapMsg": fsLlvTrapMsg,
       "fsLearningTrapVid": fsLearningTrapVid,
       "fsLearningTrapType": fsLearningTrapType,
       "fsSensorName": fsSensorName,
       "fsSensorType": fsSensorType,
       "fsSensorIdx": fsSensorIdx,
       "fsSensorFanEventType": fsSensorFanEventType,
       "fsSensorPsuEventType": fsSensorPsuEventType,
       "fsAlarmEventType": fsAlarmEventType,
       "fsAlarmThresholdValue": fsAlarmThresholdValue,
       "fsAlarmThresholdUnits": fsAlarmThresholdUnits,
       "fsIpAddress": fsIpAddress,
       "fsJsonString": fsJsonString,
       "fsSwitchStormContrl": fsSwitchStormContrl,
       "fsTrunkMemPrefix": fsTrunkMemPrefix,
       "fsTrunkMember": fsTrunkMember,
       "fsSystem": fsSystem,
       "fsSystemInfo": fsSystemInfo,
       "fsSysVersion": fsSysVersion,
       "fsSysCpuUsage": fsSysCpuUsage,
       "fsSysMemUsage": fsSysMemUsage,
       "fsSysMemCapacity": fsSysMemCapacity,
       "fsSysDiskUsage": fsSysDiskUsage,
       "fsSysDiskCapacity": fsSysDiskCapacity,
       "fsModel": fsModel,
       "fs24vm": fs24vm,
       "fs108d": fs108d,
       "s108en": s108en,
       "s108ep": s108ep,
       "s108ef": s108ef,
       "s108dv": s108dv,
       "s108fn": s108fn,
       "s108fp": s108fp,
       "s108ff": s108ff,
       "sm10gf": sm10gf,
       "sr12dp": sr12dp,
       "s124dn": s124dn,
       "s124dp": s124dp,
       "sr24dn": sr24dn,
       "s124en": s124en,
       "s124ep": s124ep,
       "s124ef": s124ef,
       "s148en": s148en,
       "s148ep": s148ep,
       "s124ff": s124ff,
       "s148fn": s148fn,
       "s148fp": s148fp,
       "s148ff": s148ff,
       "sr16fp": sr16fp,
       "fs224d": fs224d,
       "s224df": s224df,
       "s224en": s224en,
       "s224ep": s224ep,
       "s248dp": s248dp,
       "s248df": s248df,
       "s248dn": s248dn,
       "s248ef": s248ef,
       "s248ep": s248ep,
       "s424dn": s424dn,
       "s424dp": s424dp,
       "s424df": s424df,
       "s448dn": s448dn,
       "s448df": s448df,
       "s448dp": s448dp,
       "s448en": s448en,
       "s448ep": s448ep,
       "s448ef": s448ef,
       "s524df": s524df,
       "s524dn": s524dn,
       "s548df": s548df,
       "s548dn": s548dn,
       "s624fn": s624fn,
       "s624ff": s624ff,
       "s648fn": s648fn,
       "s648ff": s648ff,
       "fs1d24": fs1d24,
       "fs1e24": fs1e24,
       "st1e24": st1e24,
       "tf1f24": tf1f24,
       "fs1d48": fs1d48,
       "fs1e48": fs1e48,
       "s124fn": s124fn,
       "s124fp": s124fp,
       "sm24gn": sm24gn,
       "sm24gf": sm24gf,
       "fs2f48": fs2f48,
       "fs3d32": fs3d32,
       "fs3e32": fs3e32,
       "s424en": s424en,
       "s424ep": s424ep,
       "s424ef": s424ef,
       "s424ei": s424ei,
       "s426ef": s426ef,
       "sr24fp": sr24fp,
       "fsMibConformance": fsMibConformance,
       "fsNotificationGroup": fsNotificationGroup,
       "fsSystemObjectGroup": fsSystemObjectGroup,
       "fsTrunkObjectGroup": fsTrunkObjectGroup,
       "fsMIBCompliance": fsMIBCompliance}
)
