# SNMP MIB module (PAN-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\paloaltonetworks\PAN-COMMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:16 2025
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

(panCommonMib,
 panModules) = mibBuilder.importSymbols(
    "PAN-GLOBAL-REG",
    "panCommonMib",
    "panModules")

(TcChassisType,) = mibBuilder.importSymbols(
    "PAN-GLOBAL-TC",
    "TcChassisType")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

panCommonMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 3)
)
if mibBuilder.loadTexts:
    panCommonMibModule.setRevisions(
        ("2014-06-30 00:00",
         "2014-09-04 00:00",
         "2014-03-06 00:00",
         "2013-03-01 00:00",
         "2011-02-09 16:10")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FloatValue(TextualConvention, OctetString):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



# MIB Managed Objects in the order of their OIDs

_PanCommonConfMib_ObjectIdentity = ObjectIdentity
panCommonConfMib = _PanCommonConfMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 1)
)
if mibBuilder.loadTexts:
    panCommonConfMib.setStatus("current")
_PanCommonObjs_ObjectIdentity = ObjectIdentity
panCommonObjs = _PanCommonObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2)
)
if mibBuilder.loadTexts:
    panCommonObjs.setStatus("current")
_PanSys_ObjectIdentity = ObjectIdentity
panSys = _PanSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    panSys.setStatus("current")
_PanSysSwVersion_Type = DisplayString
_PanSysSwVersion_Object = MibScalar
panSysSwVersion = _PanSysSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 1),
    _PanSysSwVersion_Type()
)
panSysSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysSwVersion.setStatus("current")
_PanSysHwVersion_Type = DisplayString
_PanSysHwVersion_Object = MibScalar
panSysHwVersion = _PanSysHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 2),
    _PanSysHwVersion_Type()
)
panSysHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysHwVersion.setStatus("current")
_PanSysSerialNumber_Type = DisplayString
_PanSysSerialNumber_Object = MibScalar
panSysSerialNumber = _PanSysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 3),
    _PanSysSerialNumber_Type()
)
panSysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysSerialNumber.setStatus("current")
_PanSysTimeZoneOffset_Type = Integer32
_PanSysTimeZoneOffset_Object = MibScalar
panSysTimeZoneOffset = _PanSysTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 4),
    _PanSysTimeZoneOffset_Type()
)
panSysTimeZoneOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysTimeZoneOffset.setStatus("current")
_PanSysDaylightSaving_Type = TruthValue
_PanSysDaylightSaving_Object = MibScalar
panSysDaylightSaving = _PanSysDaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 5),
    _PanSysDaylightSaving_Type()
)
panSysDaylightSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysDaylightSaving.setStatus("current")
_PanSysVpnClientVersion_Type = DisplayString
_PanSysVpnClientVersion_Object = MibScalar
panSysVpnClientVersion = _PanSysVpnClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 6),
    _PanSysVpnClientVersion_Type()
)
panSysVpnClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysVpnClientVersion.setStatus("current")
_PanSysAppVersion_Type = DisplayString
_PanSysAppVersion_Object = MibScalar
panSysAppVersion = _PanSysAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 7),
    _PanSysAppVersion_Type()
)
panSysAppVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysAppVersion.setStatus("current")
_PanSysAvVersion_Type = DisplayString
_PanSysAvVersion_Object = MibScalar
panSysAvVersion = _PanSysAvVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 8),
    _PanSysAvVersion_Type()
)
panSysAvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysAvVersion.setStatus("current")
_PanSysThreatVersion_Type = DisplayString
_PanSysThreatVersion_Object = MibScalar
panSysThreatVersion = _PanSysThreatVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 9),
    _PanSysThreatVersion_Type()
)
panSysThreatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysThreatVersion.setStatus("current")
_PanSysUrlFilteringVersion_Type = DisplayString
_PanSysUrlFilteringVersion_Object = MibScalar
panSysUrlFilteringVersion = _PanSysUrlFilteringVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 10),
    _PanSysUrlFilteringVersion_Type()
)
panSysUrlFilteringVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysUrlFilteringVersion.setStatus("current")
_PanSysHAState_Type = DisplayString
_PanSysHAState_Object = MibScalar
panSysHAState = _PanSysHAState_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 11),
    _PanSysHAState_Type()
)
panSysHAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysHAState.setStatus("current")
_PanSysHAPeerState_Type = DisplayString
_PanSysHAPeerState_Object = MibScalar
panSysHAPeerState = _PanSysHAPeerState_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 12),
    _PanSysHAPeerState_Type()
)
panSysHAPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysHAPeerState.setStatus("current")
_PanSysHAMode_Type = DisplayString
_PanSysHAMode_Object = MibScalar
panSysHAMode = _PanSysHAMode_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 13),
    _PanSysHAMode_Type()
)
panSysHAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysHAMode.setStatus("current")
_PanSysUrlFilteringDatabase_Type = DisplayString
_PanSysUrlFilteringDatabase_Object = MibScalar
panSysUrlFilteringDatabase = _PanSysUrlFilteringDatabase_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 14),
    _PanSysUrlFilteringDatabase_Type()
)
panSysUrlFilteringDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysUrlFilteringDatabase.setStatus("current")
_PanSysGlobalProtectClientVersion_Type = DisplayString
_PanSysGlobalProtectClientVersion_Object = MibScalar
panSysGlobalProtectClientVersion = _PanSysGlobalProtectClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 15),
    _PanSysGlobalProtectClientVersion_Type()
)
panSysGlobalProtectClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysGlobalProtectClientVersion.setStatus("current")
_PanSysOpswatDatafileVersion_Type = DisplayString
_PanSysOpswatDatafileVersion_Object = MibScalar
panSysOpswatDatafileVersion = _PanSysOpswatDatafileVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 16),
    _PanSysOpswatDatafileVersion_Type()
)
panSysOpswatDatafileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysOpswatDatafileVersion.setStatus("current")
_PanSysWildfireVersion_Type = DisplayString
_PanSysWildfireVersion_Object = MibScalar
panSysWildfireVersion = _PanSysWildfireVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 17),
    _PanSysWildfireVersion_Type()
)
panSysWildfireVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysWildfireVersion.setStatus("current")
_PanSysWildfirePrivateCloudVersion_Type = DisplayString
_PanSysWildfirePrivateCloudVersion_Object = MibScalar
panSysWildfirePrivateCloudVersion = _PanSysWildfirePrivateCloudVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 18),
    _PanSysWildfirePrivateCloudVersion_Type()
)
panSysWildfirePrivateCloudVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysWildfirePrivateCloudVersion.setStatus("current")
_PanGlobalCounters_ObjectIdentity = ObjectIdentity
panGlobalCounters = _PanGlobalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19)
)
if mibBuilder.loadTexts:
    panGlobalCounters.setStatus("current")
_PanAhoSw_Type = Counter64
_PanAhoSw_Object = MibScalar
panAhoSw = _PanAhoSw_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 1),
    _PanAhoSw_Type()
)
panAhoSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panAhoSw.setStatus("current")
_PanDfaSw_Type = Counter64
_PanDfaSw_Object = MibScalar
panDfaSw = _PanDfaSw_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 2),
    _PanDfaSw_Type()
)
panDfaSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDfaSw.setStatus("current")
_PanFlowHostServiceAllow_Type = Counter64
_PanFlowHostServiceAllow_Object = MibScalar
panFlowHostServiceAllow = _PanFlowHostServiceAllow_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 3),
    _PanFlowHostServiceAllow_Type()
)
panFlowHostServiceAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowHostServiceAllow.setStatus("current")
_PanHaPathmonSent_Type = Counter64
_PanHaPathmonSent_Object = MibScalar
panHaPathmonSent = _PanHaPathmonSent_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 4),
    _PanHaPathmonSent_Type()
)
panHaPathmonSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panHaPathmonSent.setStatus("current")
_PanAhoFpga_Type = Counter64
_PanAhoFpga_Object = MibScalar
panAhoFpga = _PanAhoFpga_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 5),
    _PanAhoFpga_Type()
)
panAhoFpga.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panAhoFpga.setStatus("current")
_PanDfaFpga_Type = Counter64
_PanDfaFpga_Object = MibScalar
panDfaFpga = _PanDfaFpga_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 6),
    _PanDfaFpga_Type()
)
panDfaFpga.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDfaFpga.setStatus("current")
_PanFpgaPkt_Type = Counter64
_PanFpgaPkt_Object = MibScalar
panFpgaPkt = _PanFpgaPkt_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 7),
    _PanFpgaPkt_Type()
)
panFpgaPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFpgaPkt.setStatus("current")
_PanGlobalCountersDOSCounters_ObjectIdentity = ObjectIdentity
panGlobalCountersDOSCounters = _PanGlobalCountersDOSCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8)
)
if mibBuilder.loadTexts:
    panGlobalCountersDOSCounters.setStatus("current")
_PanFlowDosAgMaxSessLimit_Type = Counter64
_PanFlowDosAgMaxSessLimit_Object = MibScalar
panFlowDosAgMaxSessLimit = _PanFlowDosAgMaxSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 1),
    _PanFlowDosAgMaxSessLimit_Type()
)
panFlowDosAgMaxSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosAgMaxSessLimit.setStatus("current")
_PanFlowDosBlkNumEntries_Type = Counter64
_PanFlowDosBlkNumEntries_Object = MibScalar
panFlowDosBlkNumEntries = _PanFlowDosBlkNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 2),
    _PanFlowDosBlkNumEntries_Type()
)
panFlowDosBlkNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosBlkNumEntries.setStatus("current")
_PanFlowDosClMaxSessLimit_Type = Counter64
_PanFlowDosClMaxSessLimit_Object = MibScalar
panFlowDosClMaxSessLimit = _PanFlowDosClMaxSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 3),
    _PanFlowDosClMaxSessLimit_Type()
)
panFlowDosClMaxSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosClMaxSessLimit.setStatus("current")
_PanFlowDosClSyncookieAckErr_Type = Counter64
_PanFlowDosClSyncookieAckErr_Object = MibScalar
panFlowDosClSyncookieAckErr = _PanFlowDosClSyncookieAckErr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 4),
    _PanFlowDosClSyncookieAckErr_Type()
)
panFlowDosClSyncookieAckErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosClSyncookieAckErr.setStatus("current")
_PanFlowDosClSyncookieAckRcv_Type = Counter64
_PanFlowDosClSyncookieAckRcv_Object = MibScalar
panFlowDosClSyncookieAckRcv = _PanFlowDosClSyncookieAckRcv_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 5),
    _PanFlowDosClSyncookieAckRcv_Type()
)
panFlowDosClSyncookieAckRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosClSyncookieAckRcv.setStatus("current")
_PanFlowDosClSyncookieBlkDur_Type = Counter64
_PanFlowDosClSyncookieBlkDur_Object = MibScalar
panFlowDosClSyncookieBlkDur = _PanFlowDosClSyncookieBlkDur_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 6),
    _PanFlowDosClSyncookieBlkDur_Type()
)
panFlowDosClSyncookieBlkDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosClSyncookieBlkDur.setStatus("current")
_PanFlowDosClSyncookieMax_Type = Counter64
_PanFlowDosClSyncookieMax_Object = MibScalar
panFlowDosClSyncookieMax = _PanFlowDosClSyncookieMax_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 7),
    _PanFlowDosClSyncookieMax_Type()
)
panFlowDosClSyncookieMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosClSyncookieMax.setStatus("current")
_PanFlowDosClSyncookieSent_Type = Counter64
_PanFlowDosClSyncookieSent_Object = MibScalar
panFlowDosClSyncookieSent = _PanFlowDosClSyncookieSent_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 8),
    _PanFlowDosClSyncookieSent_Type()
)
panFlowDosClSyncookieSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosClSyncookieSent.setStatus("current")
_PanFlowMeterVsysThrottle_Type = Counter64
_PanFlowMeterVsysThrottle_Object = MibScalar
panFlowMeterVsysThrottle = _PanFlowMeterVsysThrottle_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 9),
    _PanFlowMeterVsysThrottle_Type()
)
panFlowMeterVsysThrottle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowMeterVsysThrottle.setStatus("current")
_PanFlowPolicyDeny_Type = Counter64
_PanFlowPolicyDeny_Object = MibScalar
panFlowPolicyDeny = _PanFlowPolicyDeny_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 10),
    _PanFlowPolicyDeny_Type()
)
panFlowPolicyDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowPolicyDeny.setStatus("current")
_PanFlowPolicyNat_Type = Counter64
_PanFlowPolicyNat_Object = MibScalar
panFlowPolicyNat = _PanFlowPolicyNat_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 11),
    _PanFlowPolicyNat_Type()
)
panFlowPolicyNat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowPolicyNat.setStatus("current")
_PanFlowScanDrop_Type = Counter64
_PanFlowScanDrop_Object = MibScalar
panFlowScanDrop = _PanFlowScanDrop_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 12),
    _PanFlowScanDrop_Type()
)
panFlowScanDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowScanDrop.setStatus("current")
_PanFlowDosDropIpBlocked_Type = Counter64
_PanFlowDosDropIpBlocked_Object = MibScalar
panFlowDosDropIpBlocked = _PanFlowDosDropIpBlocked_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 13),
    _PanFlowDosDropIpBlocked_Type()
)
panFlowDosDropIpBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosDropIpBlocked.setStatus("current")
_PanFlowDosRedIcmp_Type = Counter64
_PanFlowDosRedIcmp_Object = MibScalar
panFlowDosRedIcmp = _PanFlowDosRedIcmp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 14),
    _PanFlowDosRedIcmp_Type()
)
panFlowDosRedIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRedIcmp.setStatus("current")
_PanFlowDosRedIcmp6_Type = Counter64
_PanFlowDosRedIcmp6_Object = MibScalar
panFlowDosRedIcmp6 = _PanFlowDosRedIcmp6_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 15),
    _PanFlowDosRedIcmp6_Type()
)
panFlowDosRedIcmp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRedIcmp6.setStatus("current")
_PanFlowDosRedIp_Type = Counter64
_PanFlowDosRedIp_Object = MibScalar
panFlowDosRedIp = _PanFlowDosRedIp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 16),
    _PanFlowDosRedIp_Type()
)
panFlowDosRedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRedIp.setStatus("current")
_PanFlowDosRedTcp_Type = Counter64
_PanFlowDosRedTcp_Object = MibScalar
panFlowDosRedTcp = _PanFlowDosRedTcp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 17),
    _PanFlowDosRedTcp_Type()
)
panFlowDosRedTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRedTcp.setStatus("current")
_PanFlowDosRedUdp_Type = Counter64
_PanFlowDosRedUdp_Object = MibScalar
panFlowDosRedUdp = _PanFlowDosRedUdp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 18),
    _PanFlowDosRedUdp_Type()
)
panFlowDosRedUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRedUdp.setStatus("current")
_PanFlowDosRuleAgBlkDur_Type = Counter64
_PanFlowDosRuleAgBlkDur_Object = MibScalar
panFlowDosRuleAgBlkDur = _PanFlowDosRuleAgBlkDur_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 19),
    _PanFlowDosRuleAgBlkDur_Type()
)
panFlowDosRuleAgBlkDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleAgBlkDur.setStatus("current")
_PanFlowDosRuleAgRedAct_Type = Counter64
_PanFlowDosRuleAgRedAct_Object = MibScalar
panFlowDosRuleAgRedAct = _PanFlowDosRuleAgRedAct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 20),
    _PanFlowDosRuleAgRedAct_Type()
)
panFlowDosRuleAgRedAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleAgRedAct.setStatus("current")
_PanFlowDosRuleAgRedMax_Type = Counter64
_PanFlowDosRuleAgRedMax_Object = MibScalar
panFlowDosRuleAgRedMax = _PanFlowDosRuleAgRedMax_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 21),
    _PanFlowDosRuleAgRedMax_Type()
)
panFlowDosRuleAgRedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleAgRedMax.setStatus("current")
_PanFlowDosRuleDeny_Type = Counter64
_PanFlowDosRuleDeny_Object = MibScalar
panFlowDosRuleDeny = _PanFlowDosRuleDeny_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 22),
    _PanFlowDosRuleDeny_Type()
)
panFlowDosRuleDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDeny.setStatus("current")
_PanFlowDosRuleDrop_Type = Counter64
_PanFlowDosRuleDrop_Object = MibScalar
panFlowDosRuleDrop = _PanFlowDosRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 23),
    _PanFlowDosRuleDrop_Type()
)
panFlowDosRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDrop.setStatus("current")
_PanFlowDosRuleDropAggr_Type = Counter64
_PanFlowDosRuleDropAggr_Object = MibScalar
panFlowDosRuleDropAggr = _PanFlowDosRuleDropAggr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 24),
    _PanFlowDosRuleDropAggr_Type()
)
panFlowDosRuleDropAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDropAggr.setStatus("current")
_PanFlowDosRuleDropClBlkDur_Type = Counter64
_PanFlowDosRuleDropClBlkDur_Object = MibScalar
panFlowDosRuleDropClBlkDur = _PanFlowDosRuleDropClBlkDur_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 25),
    _PanFlowDosRuleDropClBlkDur_Type()
)
panFlowDosRuleDropClBlkDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDropClBlkDur.setStatus("current")
_PanFlowDosRuleDropClRedAct_Type = Counter64
_PanFlowDosRuleDropClRedAct_Object = MibScalar
panFlowDosRuleDropClRedAct = _PanFlowDosRuleDropClRedAct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 26),
    _PanFlowDosRuleDropClRedAct_Type()
)
panFlowDosRuleDropClRedAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDropClRedAct.setStatus("current")
_PanFlowDosRuleDropClRedMax_Type = Counter64
_PanFlowDosRuleDropClRedMax_Object = MibScalar
panFlowDosRuleDropClRedMax = _PanFlowDosRuleDropClRedMax_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 27),
    _PanFlowDosRuleDropClRedMax_Type()
)
panFlowDosRuleDropClRedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDropClRedMax.setStatus("current")
_PanFlowDosRuleDropClassified_Type = Counter64
_PanFlowDosRuleDropClassified_Object = MibScalar
panFlowDosRuleDropClassified = _PanFlowDosRuleDropClassified_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 28),
    _PanFlowDosRuleDropClassified_Type()
)
panFlowDosRuleDropClassified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDropClassified.setStatus("current")
_PanFlowDosSyncookieBlkDur_Type = Counter64
_PanFlowDosSyncookieBlkDur_Object = MibScalar
panFlowDosSyncookieBlkDur = _PanFlowDosSyncookieBlkDur_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 29),
    _PanFlowDosSyncookieBlkDur_Type()
)
panFlowDosSyncookieBlkDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosSyncookieBlkDur.setStatus("current")
_PanFlowDosSyncookieMax_Type = Counter64
_PanFlowDosSyncookieMax_Object = MibScalar
panFlowDosSyncookieMax = _PanFlowDosSyncookieMax_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 30),
    _PanFlowDosSyncookieMax_Type()
)
panFlowDosSyncookieMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosSyncookieMax.setStatus("current")
_PanFlowDosZoneRedAct_Type = Counter64
_PanFlowDosZoneRedAct_Object = MibScalar
panFlowDosZoneRedAct = _PanFlowDosZoneRedAct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 31),
    _PanFlowDosZoneRedAct_Type()
)
panFlowDosZoneRedAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosZoneRedAct.setStatus("current")
_PanFlowDosZoneRedMax_Type = Counter64
_PanFlowDosZoneRedMax_Object = MibScalar
panFlowDosZoneRedMax = _PanFlowDosZoneRedMax_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 32),
    _PanFlowDosZoneRedMax_Type()
)
panFlowDosZoneRedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosZoneRedMax.setStatus("current")
_PanFlowDosBlkSwEntries_Type = Counter64
_PanFlowDosBlkSwEntries_Object = MibScalar
panFlowDosBlkSwEntries = _PanFlowDosBlkSwEntries_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 33),
    _PanFlowDosBlkSwEntries_Type()
)
panFlowDosBlkSwEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosBlkSwEntries.setStatus("current")
_PanFlowDosBlkHwEntries_Type = Counter64
_PanFlowDosBlkHwEntries_Object = MibScalar
panFlowDosBlkHwEntries = _PanFlowDosBlkHwEntries_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 34),
    _PanFlowDosBlkHwEntries_Type()
)
panFlowDosBlkHwEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosBlkHwEntries.setStatus("current")
_PanFlowDosSyncookieNotTcpSyn_Type = Counter64
_PanFlowDosSyncookieNotTcpSyn_Object = MibScalar
panFlowDosSyncookieNotTcpSyn = _PanFlowDosSyncookieNotTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 35),
    _PanFlowDosSyncookieNotTcpSyn_Type()
)
panFlowDosSyncookieNotTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosSyncookieNotTcpSyn.setStatus("current")
_PanFlowDosSyncookieNotTcpSynAck_Type = Counter64
_PanFlowDosSyncookieNotTcpSynAck_Object = MibScalar
panFlowDosSyncookieNotTcpSynAck = _PanFlowDosSyncookieNotTcpSynAck_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 36),
    _PanFlowDosSyncookieNotTcpSynAck_Type()
)
panFlowDosSyncookieNotTcpSynAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosSyncookieNotTcpSynAck.setStatus("current")
_PanFlowDosPfIpspoof_Type = Counter64
_PanFlowDosPfIpspoof_Object = MibScalar
panFlowDosPfIpspoof = _PanFlowDosPfIpspoof_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 37),
    _PanFlowDosPfIpspoof_Type()
)
panFlowDosPfIpspoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfIpspoof.setStatus("current")
_PanFlowDosPfIpfrag_Type = Counter64
_PanFlowDosPfIpfrag_Object = MibScalar
panFlowDosPfIpfrag = _PanFlowDosPfIpfrag_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 38),
    _PanFlowDosPfIpfrag_Type()
)
panFlowDosPfIpfrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfIpfrag.setStatus("current")
_PanFlowDosPfPing0_Type = Counter64
_PanFlowDosPfPing0_Object = MibScalar
panFlowDosPfPing0 = _PanFlowDosPfPing0_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 39),
    _PanFlowDosPfPing0_Type()
)
panFlowDosPfPing0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfPing0.setStatus("current")
_PanFlowDosPfIcmpfrag_Type = Counter64
_PanFlowDosPfIcmpfrag_Object = MibScalar
panFlowDosPfIcmpfrag = _PanFlowDosPfIcmpfrag_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 40),
    _PanFlowDosPfIcmpfrag_Type()
)
panFlowDosPfIcmpfrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfIcmpfrag.setStatus("current")
_PanFlowDosPfIcmplpkt_Type = Counter64
_PanFlowDosPfIcmplpkt_Object = MibScalar
panFlowDosPfIcmplpkt = _PanFlowDosPfIcmplpkt_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 41),
    _PanFlowDosPfIcmplpkt_Type()
)
panFlowDosPfIcmplpkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfIcmplpkt.setStatus("current")
_PanFlowDosPfIcmperr_Type = Counter64
_PanFlowDosPfIcmperr_Object = MibScalar
panFlowDosPfIcmperr = _PanFlowDosPfIcmperr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 42),
    _PanFlowDosPfIcmperr_Type()
)
panFlowDosPfIcmperr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfIcmperr.setStatus("current")
_PanFlowDosPfNoreplyttl_Type = Counter64
_PanFlowDosPfNoreplyttl_Object = MibScalar
panFlowDosPfNoreplyttl = _PanFlowDosPfNoreplyttl_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 43),
    _PanFlowDosPfNoreplyttl_Type()
)
panFlowDosPfNoreplyttl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfNoreplyttl.setStatus("current")
_PanFlowDosPfNoreplyneedfrag_Type = Counter64
_PanFlowDosPfNoreplyneedfrag_Object = MibScalar
panFlowDosPfNoreplyneedfrag = _PanFlowDosPfNoreplyneedfrag_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 44),
    _PanFlowDosPfNoreplyneedfrag_Type()
)
panFlowDosPfNoreplyneedfrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfNoreplyneedfrag.setStatus("current")
_PanFlowDosPfStrictsource_Type = Counter64
_PanFlowDosPfStrictsource_Object = MibScalar
panFlowDosPfStrictsource = _PanFlowDosPfStrictsource_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 45),
    _PanFlowDosPfStrictsource_Type()
)
panFlowDosPfStrictsource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfStrictsource.setStatus("current")
_PanFlowDosPfLoosesource_Type = Counter64
_PanFlowDosPfLoosesource_Object = MibScalar
panFlowDosPfLoosesource = _PanFlowDosPfLoosesource_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 46),
    _PanFlowDosPfLoosesource_Type()
)
panFlowDosPfLoosesource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfLoosesource.setStatus("current")
_PanFlowDosPfTimestamp_Type = Counter64
_PanFlowDosPfTimestamp_Object = MibScalar
panFlowDosPfTimestamp = _PanFlowDosPfTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 47),
    _PanFlowDosPfTimestamp_Type()
)
panFlowDosPfTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfTimestamp.setStatus("current")
_PanFlowDosPfRecordroute_Type = Counter64
_PanFlowDosPfRecordroute_Object = MibScalar
panFlowDosPfRecordroute = _PanFlowDosPfRecordroute_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 48),
    _PanFlowDosPfRecordroute_Type()
)
panFlowDosPfRecordroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfRecordroute.setStatus("current")
_PanFlowDosPfSecurity_Type = Counter64
_PanFlowDosPfSecurity_Object = MibScalar
panFlowDosPfSecurity = _PanFlowDosPfSecurity_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 49),
    _PanFlowDosPfSecurity_Type()
)
panFlowDosPfSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfSecurity.setStatus("current")
_PanFlowDosPfSatnetid_Type = Counter64
_PanFlowDosPfSatnetid_Object = MibScalar
panFlowDosPfSatnetid = _PanFlowDosPfSatnetid_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 50),
    _PanFlowDosPfSatnetid_Type()
)
panFlowDosPfSatnetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfSatnetid.setStatus("current")
_PanFlowDosPfUnknown_Type = Counter64
_PanFlowDosPfUnknown_Object = MibScalar
panFlowDosPfUnknown = _PanFlowDosPfUnknown_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 51),
    _PanFlowDosPfUnknown_Type()
)
panFlowDosPfUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfUnknown.setStatus("current")
_PanFlowDosPfBadoption_Type = Counter64
_PanFlowDosPfBadoption_Object = MibScalar
panFlowDosPfBadoption = _PanFlowDosPfBadoption_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 52),
    _PanFlowDosPfBadoption_Type()
)
panFlowDosPfBadoption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfBadoption.setStatus("current")
_PanFlowDosPfTcpoverlappingmismatch_Type = Counter64
_PanFlowDosPfTcpoverlappingmismatch_Object = MibScalar
panFlowDosPfTcpoverlappingmismatch = _PanFlowDosPfTcpoverlappingmismatch_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 53),
    _PanFlowDosPfTcpoverlappingmismatch_Type()
)
panFlowDosPfTcpoverlappingmismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfTcpoverlappingmismatch.setStatus("current")
_PanFlowDosPfStrictip_Type = Counter64
_PanFlowDosPfStrictip_Object = MibScalar
panFlowDosPfStrictip = _PanFlowDosPfStrictip_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 54),
    _PanFlowDosPfStrictip_Type()
)
panFlowDosPfStrictip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfStrictip.setStatus("current")
_PanFlowDosPfTcpsplithandshake_Type = Counter64
_PanFlowDosPfTcpsplithandshake_Object = MibScalar
panFlowDosPfTcpsplithandshake = _PanFlowDosPfTcpsplithandshake_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 55),
    _PanFlowDosPfTcpsplithandshake_Type()
)
panFlowDosPfTcpsplithandshake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfTcpsplithandshake.setStatus("current")
_PanFlowDosPfTcpsyndata_Type = Counter64
_PanFlowDosPfTcpsyndata_Object = MibScalar
panFlowDosPfTcpsyndata = _PanFlowDosPfTcpsyndata_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 56),
    _PanFlowDosPfTcpsyndata_Type()
)
panFlowDosPfTcpsyndata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfTcpsyndata.setStatus("current")
_PanFlowDosPfTcpsynackdata_Type = Counter64
_PanFlowDosPfTcpsynackdata_Object = MibScalar
panFlowDosPfTcpsynackdata = _PanFlowDosPfTcpsynackdata_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 57),
    _PanFlowDosPfTcpsynackdata_Type()
)
panFlowDosPfTcpsynackdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPfTcpsynackdata.setStatus("current")
_PanFlowDosIp6Route0_Type = Counter64
_PanFlowDosIp6Route0_Object = MibScalar
panFlowDosIp6Route0 = _PanFlowDosIp6Route0_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 58),
    _PanFlowDosIp6Route0_Type()
)
panFlowDosIp6Route0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6Route0.setStatus("current")
_PanFlowDosIp6Route1_Type = Counter64
_PanFlowDosIp6Route1_Object = MibScalar
panFlowDosIp6Route1 = _PanFlowDosIp6Route1_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 59),
    _PanFlowDosIp6Route1_Type()
)
panFlowDosIp6Route1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6Route1.setStatus("current")
_PanFlowDosIp6Route3_Type = Counter64
_PanFlowDosIp6Route3_Object = MibScalar
panFlowDosIp6Route3 = _PanFlowDosIp6Route3_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 60),
    _PanFlowDosIp6Route3_Type()
)
panFlowDosIp6Route3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6Route3.setStatus("current")
_PanFlowDosIp6Route4to252_Type = Counter64
_PanFlowDosIp6Route4to252_Object = MibScalar
panFlowDosIp6Route4to252 = _PanFlowDosIp6Route4to252_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 61),
    _PanFlowDosIp6Route4to252_Type()
)
panFlowDosIp6Route4to252.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6Route4to252.setStatus("current")
_PanFlowDosIp6Route253_Type = Counter64
_PanFlowDosIp6Route253_Object = MibScalar
panFlowDosIp6Route253 = _PanFlowDosIp6Route253_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 62),
    _PanFlowDosIp6Route253_Type()
)
panFlowDosIp6Route253.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6Route253.setStatus("current")
_PanFlowDosIp6Route254_Type = Counter64
_PanFlowDosIp6Route254_Object = MibScalar
panFlowDosIp6Route254 = _PanFlowDosIp6Route254_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 63),
    _PanFlowDosIp6Route254_Type()
)
panFlowDosIp6Route254.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6Route254.setStatus("current")
_PanFlowDosIp6Route255_Type = Counter64
_PanFlowDosIp6Route255_Object = MibScalar
panFlowDosIp6Route255 = _PanFlowDosIp6Route255_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 64),
    _PanFlowDosIp6Route255_Type()
)
panFlowDosIp6Route255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6Route255.setStatus("current")
_PanFlowDosIp6Ip4cmpt_Type = Counter64
_PanFlowDosIp6Ip4cmpt_Object = MibScalar
panFlowDosIp6Ip4cmpt = _PanFlowDosIp6Ip4cmpt_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 65),
    _PanFlowDosIp6Ip4cmpt_Type()
)
panFlowDosIp6Ip4cmpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6Ip4cmpt.setStatus("current")
_PanFlowDosIp6Acast_Type = Counter64
_PanFlowDosIp6Acast_Object = MibScalar
panFlowDosIp6Acast = _PanFlowDosIp6Acast_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 66),
    _PanFlowDosIp6Acast_Type()
)
panFlowDosIp6Acast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6Acast.setStatus("current")
_PanFlowDosIp6OptionsInvalidIPv6_Type = Counter64
_PanFlowDosIp6OptionsInvalidIPv6_Object = MibScalar
panFlowDosIp6OptionsInvalidIPv6 = _PanFlowDosIp6OptionsInvalidIPv6_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 67),
    _PanFlowDosIp6OptionsInvalidIPv6_Type()
)
panFlowDosIp6OptionsInvalidIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6OptionsInvalidIPv6.setStatus("current")
_PanFlowDosIp6Icmpv6ErrorInvalid_Type = Counter64
_PanFlowDosIp6Icmpv6ErrorInvalid_Object = MibScalar
panFlowDosIp6Icmpv6ErrorInvalid = _PanFlowDosIp6Icmpv6ErrorInvalid_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 68),
    _PanFlowDosIp6Icmpv6ErrorInvalid_Type()
)
panFlowDosIp6Icmpv6ErrorInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6Icmpv6ErrorInvalid.setStatus("current")
_PanFlowDosIp6NeedlessIpv6FragHdr_Type = Counter64
_PanFlowDosIp6NeedlessIpv6FragHdr_Object = MibScalar
panFlowDosIp6NeedlessIpv6FragHdr = _PanFlowDosIp6NeedlessIpv6FragHdr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 69),
    _PanFlowDosIp6NeedlessIpv6FragHdr_Type()
)
panFlowDosIp6NeedlessIpv6FragHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6NeedlessIpv6FragHdr.setStatus("current")
_PanFlowDosIp6RsvdSet_Type = Counter64
_PanFlowDosIp6RsvdSet_Object = MibScalar
panFlowDosIp6RsvdSet = _PanFlowDosIp6RsvdSet_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 70),
    _PanFlowDosIp6RsvdSet_Type()
)
panFlowDosIp6RsvdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6RsvdSet.setStatus("current")
_PanFlowDosIPv6ExtHdrHopByHop_Type = Counter64
_PanFlowDosIPv6ExtHdrHopByHop_Object = MibScalar
panFlowDosIPv6ExtHdrHopByHop = _PanFlowDosIPv6ExtHdrHopByHop_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 71),
    _PanFlowDosIPv6ExtHdrHopByHop_Type()
)
panFlowDosIPv6ExtHdrHopByHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIPv6ExtHdrHopByHop.setStatus("current")
_PanFlowDosip6IPv6ExtHdrRouting_Type = Counter64
_PanFlowDosip6IPv6ExtHdrRouting_Object = MibScalar
panFlowDosip6IPv6ExtHdrRouting = _PanFlowDosip6IPv6ExtHdrRouting_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 72),
    _PanFlowDosip6IPv6ExtHdrRouting_Type()
)
panFlowDosip6IPv6ExtHdrRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosip6IPv6ExtHdrRouting.setStatus("current")
_PanFlowDosIp6IPv6ExtHdrDestOpt_Type = Counter64
_PanFlowDosIp6IPv6ExtHdrDestOpt_Object = MibScalar
panFlowDosIp6IPv6ExtHdrDestOpt = _PanFlowDosIp6IPv6ExtHdrDestOpt_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 73),
    _PanFlowDosIp6IPv6ExtHdrDestOpt_Type()
)
panFlowDosIp6IPv6ExtHdrDestOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosIp6IPv6ExtHdrDestOpt.setStatus("current")
_PanFlowDosPbpDrop_Type = Counter64
_PanFlowDosPbpDrop_Object = MibScalar
panFlowDosPbpDrop = _PanFlowDosPbpDrop_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 74),
    _PanFlowDosPbpDrop_Type()
)
panFlowDosPbpDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosPbpDrop.setStatus("current")
_PanFlowDosCurrSessIncrFailed_Type = Counter64
_PanFlowDosCurrSessIncrFailed_Object = MibScalar
panFlowDosCurrSessIncrFailed = _PanFlowDosCurrSessIncrFailed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 75),
    _PanFlowDosCurrSessIncrFailed_Type()
)
panFlowDosCurrSessIncrFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosCurrSessIncrFailed.setStatus("current")
_PanFlowDosCurrSessDecrFailed_Type = Counter64
_PanFlowDosCurrSessDecrFailed_Object = MibScalar
panFlowDosCurrSessDecrFailed = _PanFlowDosCurrSessDecrFailed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 76),
    _PanFlowDosCurrSessDecrFailed_Type()
)
panFlowDosCurrSessDecrFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosCurrSessDecrFailed.setStatus("current")
_PanGlobalCountersDropCounters_ObjectIdentity = ObjectIdentity
panGlobalCountersDropCounters = _PanGlobalCountersDropCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9)
)
if mibBuilder.loadTexts:
    panGlobalCountersDropCounters.setStatus("current")
_PanFlowFwdL3TtlZero_Type = Counter64
_PanFlowFwdL3TtlZero_Object = MibScalar
panFlowFwdL3TtlZero = _PanFlowFwdL3TtlZero_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 1),
    _PanFlowFwdL3TtlZero_Type()
)
panFlowFwdL3TtlZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowFwdL3TtlZero.setStatus("current")
_PanFlowMeterHostThrottle_Type = Counter64
_PanFlowMeterHostThrottle_Object = MibScalar
panFlowMeterHostThrottle = _PanFlowMeterHostThrottle_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 2),
    _PanFlowMeterHostThrottle_Type()
)
panFlowMeterHostThrottle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowMeterHostThrottle.setStatus("current")
_PanFlowHostServiceDeny_Type = Counter64
_PanFlowHostServiceDeny_Object = MibScalar
panFlowHostServiceDeny = _PanFlowHostServiceDeny_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 3),
    _PanFlowHostServiceDeny_Type()
)
panFlowHostServiceDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowHostServiceDeny.setStatus("current")
_PanFlowHostServiceUnknown_Type = Counter64
_PanFlowHostServiceUnknown_Object = MibScalar
panFlowHostServiceUnknown = _PanFlowHostServiceUnknown_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 4),
    _PanFlowHostServiceUnknown_Type()
)
panFlowHostServiceUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowHostServiceUnknown.setStatus("current")
_PanPktAllocFailure_Type = Counter64
_PanPktAllocFailure_Object = MibScalar
panPktAllocFailure = _PanPktAllocFailure_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 5),
    _PanPktAllocFailure_Type()
)
panPktAllocFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panPktAllocFailure.setStatus("current")
_PanPktAllocFailureCos_Type = Counter64
_PanPktAllocFailureCos_Object = MibScalar
panPktAllocFailureCos = _PanPktAllocFailureCos_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 6),
    _PanPktAllocFailureCos_Type()
)
panPktAllocFailureCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panPktAllocFailureCos.setStatus("current")
_PanSessionDiscard_Type = Counter64
_PanSessionDiscard_Object = MibScalar
panSessionDiscard = _PanSessionDiscard_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 7),
    _PanSessionDiscard_Type()
)
panSessionDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionDiscard.setStatus("current")
_PanGlobalCountersIPFragmentationCounters_ObjectIdentity = ObjectIdentity
panGlobalCountersIPFragmentationCounters = _PanGlobalCountersIPFragmentationCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 10)
)
if mibBuilder.loadTexts:
    panGlobalCountersIPFragmentationCounters.setStatus("current")
_PanFlowIpfragFragErr_Type = Counter64
_PanFlowIpfragFragErr_Object = MibScalar
panFlowIpfragFragErr = _PanFlowIpfragFragErr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 10, 1),
    _PanFlowIpfragFragErr_Type()
)
panFlowIpfragFragErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowIpfragFragErr.setStatus("current")
_PanFlowIpfragRecv_Type = Counter64
_PanFlowIpfragRecv_Object = MibScalar
panFlowIpfragRecv = _PanFlowIpfragRecv_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 10, 2),
    _PanFlowIpfragRecv_Type()
)
panFlowIpfragRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowIpfragRecv.setStatus("current")
_PanGlobalCountersTCPState_ObjectIdentity = ObjectIdentity
panGlobalCountersTCPState = _PanGlobalCountersTCPState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11)
)
if mibBuilder.loadTexts:
    panGlobalCountersTCPState.setStatus("current")
_PanTcpAllocWqeFailed_Type = Counter64
_PanTcpAllocWqeFailed_Object = MibScalar
panTcpAllocWqeFailed = _PanTcpAllocWqeFailed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 1),
    _PanTcpAllocWqeFailed_Type()
)
panTcpAllocWqeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panTcpAllocWqeFailed.setStatus("current")
_PanTcpDeny_Type = Counter64
_PanTcpDeny_Object = MibScalar
panTcpDeny = _PanTcpDeny_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 2),
    _PanTcpDeny_Type()
)
panTcpDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panTcpDeny.setStatus("current")
_PanTcpDropOutOfWnd_Type = Counter64
_PanTcpDropOutOfWnd_Object = MibScalar
panTcpDropOutOfWnd = _PanTcpDropOutOfWnd_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 3),
    _PanTcpDropOutOfWnd_Type()
)
panTcpDropOutOfWnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panTcpDropOutOfWnd.setStatus("current")
_PanTcpDropPacket_Type = Counter64
_PanTcpDropPacket_Object = MibScalar
panTcpDropPacket = _PanTcpDropPacket_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 4),
    _PanTcpDropPacket_Type()
)
panTcpDropPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panTcpDropPacket.setStatus("current")
_PanFlowActionClose_Type = Counter64
_PanFlowActionClose_Object = MibScalar
panFlowActionClose = _PanFlowActionClose_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 5),
    _PanFlowActionClose_Type()
)
panFlowActionClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowActionClose.setStatus("current")
_PanFlowActionReset_Type = Counter64
_PanFlowActionReset_Object = MibScalar
panFlowActionReset = _PanFlowActionReset_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 6),
    _PanFlowActionReset_Type()
)
panFlowActionReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowActionReset.setStatus("current")
_PanFlowTcpNonSyn_Type = Counter64
_PanFlowTcpNonSyn_Object = MibScalar
panFlowTcpNonSyn = _PanFlowTcpNonSyn_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 7),
    _PanFlowTcpNonSyn_Type()
)
panFlowTcpNonSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowTcpNonSyn.setStatus("current")
_PanTcpExceedSegLimit_Type = Counter64
_PanTcpExceedSegLimit_Object = MibScalar
panTcpExceedSegLimit = _PanTcpExceedSegLimit_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 8),
    _PanTcpExceedSegLimit_Type()
)
panTcpExceedSegLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panTcpExceedSegLimit.setStatus("current")
_PanGlobalCountersTunnelInspect_ObjectIdentity = ObjectIdentity
panGlobalCountersTunnelInspect = _PanGlobalCountersTunnelInspect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 12)
)
if mibBuilder.loadTexts:
    panGlobalCountersTunnelInspect.setStatus("current")
_PanFlowTciGreDecapSuccess_Type = Counter64
_PanFlowTciGreDecapSuccess_Object = MibScalar
panFlowTciGreDecapSuccess = _PanFlowTciGreDecapSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 12, 1),
    _PanFlowTciGreDecapSuccess_Type()
)
panFlowTciGreDecapSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowTciGreDecapSuccess.setStatus("current")
_PanFlowTciGreDecapFailed_Type = Counter64
_PanFlowTciGreDecapFailed_Object = MibScalar
panFlowTciGreDecapFailed = _PanFlowTciGreDecapFailed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 12, 2),
    _PanFlowTciGreDecapFailed_Type()
)
panFlowTciGreDecapFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowTciGreDecapFailed.setStatus("current")
_PanFlowTciGreDecapUnknown_Type = Counter64
_PanFlowTciGreDecapUnknown_Object = MibScalar
panFlowTciGreDecapUnknown = _PanFlowTciGreDecapUnknown_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 12, 3),
    _PanFlowTciGreDecapUnknown_Type()
)
panFlowTciGreDecapUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowTciGreDecapUnknown.setStatus("current")
_PanFlowTciIpsecDecapSuccess_Type = Counter64
_PanFlowTciIpsecDecapSuccess_Object = MibScalar
panFlowTciIpsecDecapSuccess = _PanFlowTciIpsecDecapSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 12, 4),
    _PanFlowTciIpsecDecapSuccess_Type()
)
panFlowTciIpsecDecapSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowTciIpsecDecapSuccess.setStatus("current")
_PanFlowTciIpsecDecapFailed_Type = Counter64
_PanFlowTciIpsecDecapFailed_Object = MibScalar
panFlowTciIpsecDecapFailed = _PanFlowTciIpsecDecapFailed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 12, 5),
    _PanFlowTciIpsecDecapFailed_Type()
)
panFlowTciIpsecDecapFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowTciIpsecDecapFailed.setStatus("current")
_PanFlowTciIpsecDecapUnknown_Type = Counter64
_PanFlowTciIpsecDecapUnknown_Object = MibScalar
panFlowTciIpsecDecapUnknown = _PanFlowTciIpsecDecapUnknown_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 12, 6),
    _PanFlowTciIpsecDecapUnknown_Type()
)
panFlowTciIpsecDecapUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowTciIpsecDecapUnknown.setStatus("current")
_PanFlowTciGtpDecapSuccess_Type = Counter64
_PanFlowTciGtpDecapSuccess_Object = MibScalar
panFlowTciGtpDecapSuccess = _PanFlowTciGtpDecapSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 12, 7),
    _PanFlowTciGtpDecapSuccess_Type()
)
panFlowTciGtpDecapSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowTciGtpDecapSuccess.setStatus("current")
_PanFlowTciGtpDecapFailed_Type = Counter64
_PanFlowTciGtpDecapFailed_Object = MibScalar
panFlowTciGtpDecapFailed = _PanFlowTciGtpDecapFailed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 12, 8),
    _PanFlowTciGtpDecapFailed_Type()
)
panFlowTciGtpDecapFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowTciGtpDecapFailed.setStatus("current")
_PanFlowTciGtpDecapUnknown_Type = Counter64
_PanFlowTciGtpDecapUnknown_Object = MibScalar
panFlowTciGtpDecapUnknown = _PanFlowTciGtpDecapUnknown_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 12, 9),
    _PanFlowTciGtpDecapUnknown_Type()
)
panFlowTciGtpDecapUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowTciGtpDecapUnknown.setStatus("current")
_PanSysAppReleaseDate_Type = DisplayString
_PanSysAppReleaseDate_Object = MibScalar
panSysAppReleaseDate = _PanSysAppReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 20),
    _PanSysAppReleaseDate_Type()
)
panSysAppReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysAppReleaseDate.setStatus("current")
_PanSysThreatReleaseDate_Type = DisplayString
_PanSysThreatReleaseDate_Object = MibScalar
panSysThreatReleaseDate = _PanSysThreatReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 21),
    _PanSysThreatReleaseDate_Type()
)
panSysThreatReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysThreatReleaseDate.setStatus("current")
_PanSysAvReleaseDate_Type = DisplayString
_PanSysAvReleaseDate_Object = MibScalar
panSysAvReleaseDate = _PanSysAvReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 22),
    _PanSysAvReleaseDate_Type()
)
panSysAvReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysAvReleaseDate.setStatus("current")
_PanSysWfReleaseDate_Type = DisplayString
_PanSysWfReleaseDate_Object = MibScalar
panSysWfReleaseDate = _PanSysWfReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 23),
    _PanSysWfReleaseDate_Type()
)
panSysWfReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysWfReleaseDate.setStatus("current")
_PanChassis_ObjectIdentity = ObjectIdentity
panChassis = _PanChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    panChassis.setStatus("current")
_PanChassisType_Type = DisplayString
_PanChassisType_Object = MibScalar
panChassisType = _PanChassisType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 2, 1),
    _PanChassisType_Type()
)
panChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panChassisType.setStatus("current")
_PanMSeriesMode_Type = DisplayString
_PanMSeriesMode_Object = MibScalar
panMSeriesMode = _PanMSeriesMode_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 2, 2),
    _PanMSeriesMode_Type()
)
panMSeriesMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panMSeriesMode.setStatus("current")
_PanSession_ObjectIdentity = ObjectIdentity
panSession = _PanSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    panSession.setStatus("current")
_PanSessionUtilization_Type = Integer32
_PanSessionUtilization_Object = MibScalar
panSessionUtilization = _PanSessionUtilization_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 1),
    _PanSessionUtilization_Type()
)
panSessionUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionUtilization.setStatus("current")
_PanSessionMax_Type = Integer32
_PanSessionMax_Object = MibScalar
panSessionMax = _PanSessionMax_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 2),
    _PanSessionMax_Type()
)
panSessionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionMax.setStatus("current")
_PanSessionActive_Type = Integer32
_PanSessionActive_Object = MibScalar
panSessionActive = _PanSessionActive_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 3),
    _PanSessionActive_Type()
)
panSessionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionActive.setStatus("current")
_PanSessionActiveTcp_Type = Integer32
_PanSessionActiveTcp_Object = MibScalar
panSessionActiveTcp = _PanSessionActiveTcp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 4),
    _PanSessionActiveTcp_Type()
)
panSessionActiveTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionActiveTcp.setStatus("current")
_PanSessionActiveUdp_Type = Integer32
_PanSessionActiveUdp_Object = MibScalar
panSessionActiveUdp = _PanSessionActiveUdp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 5),
    _PanSessionActiveUdp_Type()
)
panSessionActiveUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionActiveUdp.setStatus("current")
_PanSessionActiveICMP_Type = Integer32
_PanSessionActiveICMP_Object = MibScalar
panSessionActiveICMP = _PanSessionActiveICMP_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 6),
    _PanSessionActiveICMP_Type()
)
panSessionActiveICMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionActiveICMP.setStatus("current")
_PanSessionActiveSslProxy_Type = Integer32
_PanSessionActiveSslProxy_Object = MibScalar
panSessionActiveSslProxy = _PanSessionActiveSslProxy_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 7),
    _PanSessionActiveSslProxy_Type()
)
panSessionActiveSslProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionActiveSslProxy.setStatus("current")
_PanSessionSslProxyUtilization_Type = Integer32
_PanSessionSslProxyUtilization_Object = MibScalar
panSessionSslProxyUtilization = _PanSessionSslProxyUtilization_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 8),
    _PanSessionSslProxyUtilization_Type()
)
panSessionSslProxyUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionSslProxyUtilization.setStatus("current")
_PanVsysTable_Object = MibTable
panVsysTable = _PanVsysTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9)
)
if mibBuilder.loadTexts:
    panVsysTable.setStatus("current")
_PanVsysEntry_Object = MibTableRow
panVsysEntry = _PanVsysEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1)
)
panVsysEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panVsysId"),
)
if mibBuilder.loadTexts:
    panVsysEntry.setStatus("current")
_PanVsysId_Type = Integer32
_PanVsysId_Object = MibTableColumn
panVsysId = _PanVsysId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1, 1),
    _PanVsysId_Type()
)
panVsysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVsysId.setStatus("current")
_PanVsysName_Type = DisplayString
_PanVsysName_Object = MibTableColumn
panVsysName = _PanVsysName_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1, 2),
    _PanVsysName_Type()
)
panVsysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVsysName.setStatus("current")
_PanVsysSessionUtilizationPct_Type = Integer32
_PanVsysSessionUtilizationPct_Object = MibTableColumn
panVsysSessionUtilizationPct = _PanVsysSessionUtilizationPct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1, 3),
    _PanVsysSessionUtilizationPct_Type()
)
panVsysSessionUtilizationPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVsysSessionUtilizationPct.setStatus("current")
_PanVsysActiveSessions_Type = Integer32
_PanVsysActiveSessions_Object = MibTableColumn
panVsysActiveSessions = _PanVsysActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1, 4),
    _PanVsysActiveSessions_Type()
)
panVsysActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVsysActiveSessions.setStatus("current")
_PanVsysMaxSessions_Type = Integer32
_PanVsysMaxSessions_Object = MibTableColumn
panVsysMaxSessions = _PanVsysMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1, 5),
    _PanVsysMaxSessions_Type()
)
panVsysMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVsysMaxSessions.setStatus("current")
_PanVsysActiveTcpCps_Type = Integer32
_PanVsysActiveTcpCps_Object = MibTableColumn
panVsysActiveTcpCps = _PanVsysActiveTcpCps_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1, 6),
    _PanVsysActiveTcpCps_Type()
)
panVsysActiveTcpCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVsysActiveTcpCps.setStatus("current")
_PanVsysActiveUdpCps_Type = Integer32
_PanVsysActiveUdpCps_Object = MibTableColumn
panVsysActiveUdpCps = _PanVsysActiveUdpCps_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1, 7),
    _PanVsysActiveUdpCps_Type()
)
panVsysActiveUdpCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVsysActiveUdpCps.setStatus("current")
_PanVsysActiveOtherIpCps_Type = Integer32
_PanVsysActiveOtherIpCps_Object = MibTableColumn
panVsysActiveOtherIpCps = _PanVsysActiveOtherIpCps_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1, 8),
    _PanVsysActiveOtherIpCps_Type()
)
panVsysActiveOtherIpCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVsysActiveOtherIpCps.setStatus("current")
_PanZoneTable_Object = MibTable
panZoneTable = _PanZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 10)
)
if mibBuilder.loadTexts:
    panZoneTable.setStatus("current")
_PanZoneEntry_Object = MibTableRow
panZoneEntry = _PanZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 10, 1)
)
panZoneEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    panZoneEntry.setStatus("current")
_PanZoneName_Type = DisplayString
_PanZoneName_Object = MibTableColumn
panZoneName = _PanZoneName_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 10, 1, 1),
    _PanZoneName_Type()
)
panZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panZoneName.setStatus("current")
_PanZoneActiveTcpCps_Type = Unsigned32
_PanZoneActiveTcpCps_Object = MibTableColumn
panZoneActiveTcpCps = _PanZoneActiveTcpCps_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 10, 1, 2),
    _PanZoneActiveTcpCps_Type()
)
panZoneActiveTcpCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panZoneActiveTcpCps.setStatus("current")
_PanZoneActiveUdpCps_Type = Unsigned32
_PanZoneActiveUdpCps_Object = MibTableColumn
panZoneActiveUdpCps = _PanZoneActiveUdpCps_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 10, 1, 3),
    _PanZoneActiveUdpCps_Type()
)
panZoneActiveUdpCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panZoneActiveUdpCps.setStatus("current")
_PanZoneActiveOtherIpCps_Type = Unsigned32
_PanZoneActiveOtherIpCps_Object = MibTableColumn
panZoneActiveOtherIpCps = _PanZoneActiveOtherIpCps_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 10, 1, 4),
    _PanZoneActiveOtherIpCps_Type()
)
panZoneActiveOtherIpCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panZoneActiveOtherIpCps.setStatus("current")
_PanIfTable_Object = MibTable
panIfTable = _PanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 11)
)
if mibBuilder.loadTexts:
    panIfTable.setStatus("current")
_PanIfEntry_Object = MibTableRow
panIfEntry = _PanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 11, 1)
)
panIfEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    panIfEntry.setStatus("current")
_IfIndex_Type = Unsigned32
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 11, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndex.setStatus("current")
_IfDescr_Type = DisplayString
_IfDescr_Object = MibTableColumn
ifDescr = _IfDescr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 11, 1, 2),
    _IfDescr_Type()
)
ifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDescr.setStatus("current")
_PanIfActiveTcpCps_Type = Unsigned32
_PanIfActiveTcpCps_Object = MibTableColumn
panIfActiveTcpCps = _PanIfActiveTcpCps_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 11, 1, 3),
    _PanIfActiveTcpCps_Type()
)
panIfActiveTcpCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panIfActiveTcpCps.setStatus("current")
_PanIfActiveUdpCps_Type = Unsigned32
_PanIfActiveUdpCps_Object = MibTableColumn
panIfActiveUdpCps = _PanIfActiveUdpCps_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 11, 1, 4),
    _PanIfActiveUdpCps_Type()
)
panIfActiveUdpCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panIfActiveUdpCps.setStatus("current")
_PanIfActiveOtherIpCps_Type = Unsigned32
_PanIfActiveOtherIpCps_Object = MibTableColumn
panIfActiveOtherIpCps = _PanIfActiveOtherIpCps_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 11, 1, 5),
    _PanIfActiveOtherIpCps_Type()
)
panIfActiveOtherIpCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panIfActiveOtherIpCps.setStatus("current")
_PanMgmt_ObjectIdentity = ObjectIdentity
panMgmt = _PanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    panMgmt.setStatus("current")
_PanMgmtPanoramaConnected_Type = DisplayString
_PanMgmtPanoramaConnected_Object = MibScalar
panMgmtPanoramaConnected = _PanMgmtPanoramaConnected_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 4, 1),
    _PanMgmtPanoramaConnected_Type()
)
panMgmtPanoramaConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panMgmtPanoramaConnected.setStatus("current")
_PanMgmtPanorama2Connected_Type = DisplayString
_PanMgmtPanorama2Connected_Object = MibScalar
panMgmtPanorama2Connected = _PanMgmtPanorama2Connected_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 4, 2),
    _PanMgmtPanorama2Connected_Type()
)
panMgmtPanorama2Connected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panMgmtPanorama2Connected.setStatus("current")
_PanGlobalProtect_ObjectIdentity = ObjectIdentity
panGlobalProtect = _PanGlobalProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    panGlobalProtect.setStatus("current")
_PanGPGatewayUtilization_ObjectIdentity = ObjectIdentity
panGPGatewayUtilization = _PanGPGatewayUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    panGPGatewayUtilization.setStatus("current")
_PanGPGWUtilizationPct_Type = Integer32
_PanGPGWUtilizationPct_Object = MibScalar
panGPGWUtilizationPct = _PanGPGWUtilizationPct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 5, 1, 1),
    _PanGPGWUtilizationPct_Type()
)
panGPGWUtilizationPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panGPGWUtilizationPct.setStatus("current")
_PanGPGWUtilizationMaxTunnels_Type = Integer32
_PanGPGWUtilizationMaxTunnels_Object = MibScalar
panGPGWUtilizationMaxTunnels = _PanGPGWUtilizationMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 5, 1, 2),
    _PanGPGWUtilizationMaxTunnels_Type()
)
panGPGWUtilizationMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panGPGWUtilizationMaxTunnels.setStatus("current")
_PanGPGWUtilizationActiveTunnels_Type = Integer32
_PanGPGWUtilizationActiveTunnels_Object = MibScalar
panGPGWUtilizationActiveTunnels = _PanGPGWUtilizationActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 5, 1, 3),
    _PanGPGWUtilizationActiveTunnels_Type()
)
panGPGWUtilizationActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panGPGWUtilizationActiveTunnels.setStatus("current")
_PanLogCollector_ObjectIdentity = ObjectIdentity
panLogCollector = _PanLogCollector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    panLogCollector.setStatus("current")
_PanLcStat_ObjectIdentity = ObjectIdentity
panLcStat = _PanLcStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    panLcStat.setStatus("current")
_PanLcLogRate_Type = Unsigned32
_PanLcLogRate_Object = MibScalar
panLcLogRate = _PanLcLogRate_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 1),
    _PanLcLogRate_Type()
)
panLcLogRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogRate.setStatus("current")
_PanLcLogDuration_ObjectIdentity = ObjectIdentity
panLcLogDuration = _PanLcLogDuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2)
)
if mibBuilder.loadTexts:
    panLcLogDuration.setStatus("deprecated")
_PanLcLogDurationTraffic_Type = Unsigned32
_PanLcLogDurationTraffic_Object = MibScalar
panLcLogDurationTraffic = _PanLcLogDurationTraffic_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 1),
    _PanLcLogDurationTraffic_Type()
)
panLcLogDurationTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationTraffic.setStatus("deprecated")
_PanLcLogDurationConfig_Type = Unsigned32
_PanLcLogDurationConfig_Object = MibScalar
panLcLogDurationConfig = _PanLcLogDurationConfig_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 2),
    _PanLcLogDurationConfig_Type()
)
panLcLogDurationConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationConfig.setStatus("deprecated")
_PanLcLogDurationSystem_Type = Unsigned32
_PanLcLogDurationSystem_Object = MibScalar
panLcLogDurationSystem = _PanLcLogDurationSystem_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 3),
    _PanLcLogDurationSystem_Type()
)
panLcLogDurationSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationSystem.setStatus("deprecated")
_PanLcLogDurationThreat_Type = Unsigned32
_PanLcLogDurationThreat_Object = MibScalar
panLcLogDurationThreat = _PanLcLogDurationThreat_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 4),
    _PanLcLogDurationThreat_Type()
)
panLcLogDurationThreat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationThreat.setStatus("deprecated")
_PanLcLogDurationAppstat_Type = Unsigned32
_PanLcLogDurationAppstat_Object = MibScalar
panLcLogDurationAppstat = _PanLcLogDurationAppstat_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 5),
    _PanLcLogDurationAppstat_Type()
)
panLcLogDurationAppstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationAppstat.setStatus("deprecated")
_PanLcLogDurationTrsum_Type = Unsigned32
_PanLcLogDurationTrsum_Object = MibScalar
panLcLogDurationTrsum = _PanLcLogDurationTrsum_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 6),
    _PanLcLogDurationTrsum_Type()
)
panLcLogDurationTrsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationTrsum.setStatus("deprecated")
_PanLcLogDurationThsum_Type = Unsigned32
_PanLcLogDurationThsum_Object = MibScalar
panLcLogDurationThsum = _PanLcLogDurationThsum_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 7),
    _PanLcLogDurationThsum_Type()
)
panLcLogDurationThsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationThsum.setStatus("deprecated")
_PanLcLogDurationEvent_Type = Unsigned32
_PanLcLogDurationEvent_Object = MibScalar
panLcLogDurationEvent = _PanLcLogDurationEvent_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 8),
    _PanLcLogDurationEvent_Type()
)
panLcLogDurationEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationEvent.setStatus("deprecated")
_PanLcLogDurationAlarm_Type = Unsigned32
_PanLcLogDurationAlarm_Object = MibScalar
panLcLogDurationAlarm = _PanLcLogDurationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 9),
    _PanLcLogDurationAlarm_Type()
)
panLcLogDurationAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationAlarm.setStatus("deprecated")
_PanLcLogDurationHipmatch_Type = Unsigned32
_PanLcLogDurationHipmatch_Object = MibScalar
panLcLogDurationHipmatch = _PanLcLogDurationHipmatch_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 10),
    _PanLcLogDurationHipmatch_Type()
)
panLcLogDurationHipmatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationHipmatch.setStatus("deprecated")
_PanLcLogDurationUserid_Type = Unsigned32
_PanLcLogDurationUserid_Object = MibScalar
panLcLogDurationUserid = _PanLcLogDurationUserid_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 11),
    _PanLcLogDurationUserid_Type()
)
panLcLogDurationUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationUserid.setStatus("deprecated")
_PanLcDiskUsageTable_Object = MibTable
panLcDiskUsageTable = _PanLcDiskUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 3)
)
if mibBuilder.loadTexts:
    panLcDiskUsageTable.setStatus("deprecated")
_PanLcDiskUsageEntry_Object = MibTableRow
panLcDiskUsageEntry = _PanLcDiskUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 3, 1)
)
panLcDiskUsageEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panLcDiskUsageId"),
)
if mibBuilder.loadTexts:
    panLcDiskUsageEntry.setStatus("deprecated")
_PanLcDiskUsageId_Type = Integer32
_PanLcDiskUsageId_Object = MibTableColumn
panLcDiskUsageId = _PanLcDiskUsageId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 3, 1, 1),
    _PanLcDiskUsageId_Type()
)
panLcDiskUsageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskUsageId.setStatus("deprecated")
_PanLcDiskUsage_Type = Unsigned32
_PanLcDiskUsage_Object = MibTableColumn
panLcDiskUsage = _PanLcDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 3, 1, 2),
    _PanLcDiskUsage_Type()
)
panLcDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskUsage.setStatus("deprecated")
_PanLcLogUsageTable_Object = MibTable
panLcLogUsageTable = _PanLcLogUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 4)
)
if mibBuilder.loadTexts:
    panLcLogUsageTable.setStatus("current")
_PanLcLogUsageEntry_Object = MibTableRow
panLcLogUsageEntry = _PanLcLogUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 4, 1)
)
panLcLogUsageEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panLcLogType"),
)
if mibBuilder.loadTexts:
    panLcLogUsageEntry.setStatus("current")
_PanLcLogType_Type = DisplayString
_PanLcLogType_Object = MibTableColumn
panLcLogType = _PanLcLogType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 4, 1, 1),
    _PanLcLogType_Type()
)
panLcLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogType.setStatus("current")
_PanLcDiskUsageDiskSpacePct_Type = DisplayString
_PanLcDiskUsageDiskSpacePct_Object = MibTableColumn
panLcDiskUsageDiskSpacePct = _PanLcDiskUsageDiskSpacePct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 4, 1, 2),
    _PanLcDiskUsageDiskSpacePct_Type()
)
panLcDiskUsageDiskSpacePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskUsageDiskSpacePct.setStatus("current")
_PanLcDiskUsageRetention_Type = Unsigned32
_PanLcDiskUsageRetention_Object = MibTableColumn
panLcDiskUsageRetention = _PanLcDiskUsageRetention_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 4, 1, 3),
    _PanLcDiskUsageRetention_Type()
)
panLcDiskUsageRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskUsageRetention.setStatus("current")
_PanLcDiskQuotaPct_Type = DisplayString
_PanLcDiskQuotaPct_Object = MibTableColumn
panLcDiskQuotaPct = _PanLcDiskQuotaPct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 4, 1, 4),
    _PanLcDiskQuotaPct_Type()
)
panLcDiskQuotaPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskQuotaPct.setStatus("current")
_PanLocalLogUsageTable_Object = MibTable
panLocalLogUsageTable = _PanLocalLogUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 5)
)
if mibBuilder.loadTexts:
    panLocalLogUsageTable.setStatus("current")
_PanLocalLogUsageEntry_Object = MibTableRow
panLocalLogUsageEntry = _PanLocalLogUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 5, 1)
)
panLocalLogUsageEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panLcLogType"),
)
if mibBuilder.loadTexts:
    panLocalLogUsageEntry.setStatus("current")
_PanLocalLogType_Type = DisplayString
_PanLocalLogType_Object = MibTableColumn
panLocalLogType = _PanLocalLogType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 5, 1, 1),
    _PanLocalLogType_Type()
)
panLocalLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLocalLogType.setStatus("current")
_PanLocalDiskUsageDiskSpace_Type = DisplayString
_PanLocalDiskUsageDiskSpace_Object = MibTableColumn
panLocalDiskUsageDiskSpace = _PanLocalDiskUsageDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 5, 1, 2),
    _PanLocalDiskUsageDiskSpace_Type()
)
panLocalDiskUsageDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLocalDiskUsageDiskSpace.setStatus("current")
_PanLocalDiskUsageRetention_Type = Unsigned32
_PanLocalDiskUsageRetention_Object = MibTableColumn
panLocalDiskUsageRetention = _PanLocalDiskUsageRetention_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 5, 1, 3),
    _PanLocalDiskUsageRetention_Type()
)
panLocalDiskUsageRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLocalDiskUsageRetention.setStatus("current")
_PanLocalDiskQuota_Type = DisplayString
_PanLocalDiskQuota_Object = MibTableColumn
panLocalDiskQuota = _PanLocalDiskQuota_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 5, 1, 4),
    _PanLocalDiskQuota_Type()
)
panLocalDiskQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLocalDiskQuota.setStatus("current")
_PanLocalDiskQuotaPct_Type = DisplayString
_PanLocalDiskQuotaPct_Object = MibTableColumn
panLocalDiskQuotaPct = _PanLocalDiskQuotaPct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 5, 1, 5),
    _PanLocalDiskQuotaPct_Type()
)
panLocalDiskQuotaPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLocalDiskQuotaPct.setStatus("current")
_PanLcDiskIOPSTable_Object = MibTable
panLcDiskIOPSTable = _PanLcDiskIOPSTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 6)
)
if mibBuilder.loadTexts:
    panLcDiskIOPSTable.setStatus("current")
_PanLcDiskIOPSEntry_Object = MibTableRow
panLcDiskIOPSEntry = _PanLcDiskIOPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 6, 1)
)
panLcDiskIOPSEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panLcDiskIOPSId"),
)
if mibBuilder.loadTexts:
    panLcDiskIOPSEntry.setStatus("current")
_PanLcDiskIOPSId_Type = DisplayString
_PanLcDiskIOPSId_Object = MibTableColumn
panLcDiskIOPSId = _PanLcDiskIOPSId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 6, 1, 1),
    _PanLcDiskIOPSId_Type()
)
panLcDiskIOPSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskIOPSId.setStatus("current")
_PanLcDiskIORead5min_Type = Counter64
_PanLcDiskIORead5min_Object = MibTableColumn
panLcDiskIORead5min = _PanLcDiskIORead5min_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 6, 1, 2),
    _PanLcDiskIORead5min_Type()
)
panLcDiskIORead5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskIORead5min.setStatus("current")
_PanLcDiskIOWrite5min_Type = Counter64
_PanLcDiskIOWrite5min_Object = MibTableColumn
panLcDiskIOWrite5min = _PanLcDiskIOWrite5min_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 6, 1, 3),
    _PanLcDiskIOWrite5min_Type()
)
panLcDiskIOWrite5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskIOWrite5min.setStatus("current")
_PanLcIsRedundancyMember_Type = TruthValue
_PanLcIsRedundancyMember_Object = MibScalar
panLcIsRedundancyMember = _PanLcIsRedundancyMember_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 2),
    _PanLcIsRedundancyMember_Type()
)
panLcIsRedundancyMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcIsRedundancyMember.setStatus("current")
_PanLcLogFwdStatsTable_Object = MibTable
panLcLogFwdStatsTable = _PanLcLogFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    panLcLogFwdStatsTable.setStatus("current")
_PanLcLogFwdStatsEntry_Object = MibTableRow
panLcLogFwdStatsEntry = _PanLcLogFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 3, 1)
)
panLcLogFwdStatsEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panLcLogFwdStatsTableType"),
)
if mibBuilder.loadTexts:
    panLcLogFwdStatsEntry.setStatus("current")
_PanLcLogFwdStatsTableType_Type = DisplayString
_PanLcLogFwdStatsTableType_Object = MibTableColumn
panLcLogFwdStatsTableType = _PanLcLogFwdStatsTableType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 3, 1, 1),
    _PanLcLogFwdStatsTableType_Type()
)
panLcLogFwdStatsTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogFwdStatsTableType.setStatus("current")
_PanLcLogFwdStatsTableEnqueueCount_Type = Counter64
_PanLcLogFwdStatsTableEnqueueCount_Object = MibTableColumn
panLcLogFwdStatsTableEnqueueCount = _PanLcLogFwdStatsTableEnqueueCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 3, 1, 2),
    _PanLcLogFwdStatsTableEnqueueCount_Type()
)
panLcLogFwdStatsTableEnqueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogFwdStatsTableEnqueueCount.setStatus("current")
_PanLcLogFwdStatsTableSendCount_Type = Counter64
_PanLcLogFwdStatsTableSendCount_Object = MibTableColumn
panLcLogFwdStatsTableSendCount = _PanLcLogFwdStatsTableSendCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 3, 1, 3),
    _PanLcLogFwdStatsTableSendCount_Type()
)
panLcLogFwdStatsTableSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogFwdStatsTableSendCount.setStatus("current")
_PanLcLogFwdStatsTableDropCount_Type = Counter64
_PanLcLogFwdStatsTableDropCount_Object = MibTableColumn
panLcLogFwdStatsTableDropCount = _PanLcLogFwdStatsTableDropCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 3, 1, 4),
    _PanLcLogFwdStatsTableDropCount_Type()
)
panLcLogFwdStatsTableDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogFwdStatsTableDropCount.setStatus("current")
_PanLcLogFwdStatsTableQueueDepth_Type = Counter64
_PanLcLogFwdStatsTableQueueDepth_Object = MibTableColumn
panLcLogFwdStatsTableQueueDepth = _PanLcLogFwdStatsTableQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 3, 1, 5),
    _PanLcLogFwdStatsTableQueueDepth_Type()
)
panLcLogFwdStatsTableQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogFwdStatsTableQueueDepth.setStatus("current")
_PanLcLoggingConnectedDeviceTable_Object = MibTable
panLcLoggingConnectedDeviceTable = _PanLcLoggingConnectedDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    panLcLoggingConnectedDeviceTable.setStatus("current")
_PanLcLoggingConnectedDeviceEntry_Object = MibTableRow
panLcLoggingConnectedDeviceEntry = _PanLcLoggingConnectedDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 4, 1)
)
panLcLoggingConnectedDeviceEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panLcLoggingConnectedDeviceConnectionId"),
)
if mibBuilder.loadTexts:
    panLcLoggingConnectedDeviceEntry.setStatus("current")
_PanLcLoggingConnectedDeviceName_Type = DisplayString
_PanLcLoggingConnectedDeviceName_Object = MibTableColumn
panLcLoggingConnectedDeviceName = _PanLcLoggingConnectedDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 4, 1, 1),
    _PanLcLoggingConnectedDeviceName_Type()
)
panLcLoggingConnectedDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLoggingConnectedDeviceName.setStatus("current")
_PanLcLoggingConnectedDeviceConnectionId_Type = DisplayString
_PanLcLoggingConnectedDeviceConnectionId_Object = MibTableColumn
panLcLoggingConnectedDeviceConnectionId = _PanLcLoggingConnectedDeviceConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 4, 1, 2),
    _PanLcLoggingConnectedDeviceConnectionId_Type()
)
panLcLoggingConnectedDeviceConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLoggingConnectedDeviceConnectionId.setStatus("current")
_PanLcLoggingConnectedIdLogRate_Type = Unsigned32
_PanLcLoggingConnectedIdLogRate_Object = MibTableColumn
panLcLoggingConnectedIdLogRate = _PanLcLoggingConnectedIdLogRate_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 4, 1, 3),
    _PanLcLoggingConnectedIdLogRate_Type()
)
panLcLoggingConnectedIdLogRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLoggingConnectedIdLogRate.setStatus("current")
_PanLcLoggingDeviceTable_Object = MibTable
panLcLoggingDeviceTable = _PanLcLoggingDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 5)
)
if mibBuilder.loadTexts:
    panLcLoggingDeviceTable.setStatus("current")
_PanLcLoggingDeviceEntry_Object = MibTableRow
panLcLoggingDeviceEntry = _PanLcLoggingDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 5, 1)
)
panLcLoggingDeviceEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panLcLoggingDeviceConnectionId"),
    (0, "PAN-COMMON-MIB", "panLcLoggingLogType"),
)
if mibBuilder.loadTexts:
    panLcLoggingDeviceEntry.setStatus("current")
_PanLcLoggingDeviceConnectionId_Type = DisplayString
_PanLcLoggingDeviceConnectionId_Object = MibTableColumn
panLcLoggingDeviceConnectionId = _PanLcLoggingDeviceConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 5, 1, 1),
    _PanLcLoggingDeviceConnectionId_Type()
)
panLcLoggingDeviceConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLoggingDeviceConnectionId.setStatus("current")
_PanLcLoggingLogType_Type = DisplayString
_PanLcLoggingLogType_Object = MibTableColumn
panLcLoggingLogType = _PanLcLoggingLogType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 5, 1, 2),
    _PanLcLoggingLogType_Type()
)
panLcLoggingLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLoggingLogType.setStatus("current")
_PanLcLogTypeLastLogRecd_Type = TimeStamp
_PanLcLogTypeLastLogRecd_Object = MibTableColumn
panLcLogTypeLastLogRecd = _PanLcLogTypeLastLogRecd_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 5, 1, 3),
    _PanLcLogTypeLastLogRecd_Type()
)
panLcLogTypeLastLogRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogTypeLastLogRecd.setStatus("current")
_PanLcLogTypeLastSeqNumRecd_Type = Counter64
_PanLcLogTypeLastSeqNumRecd_Object = MibTableColumn
panLcLogTypeLastSeqNumRecd = _PanLcLogTypeLastSeqNumRecd_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 5, 1, 4),
    _PanLcLogTypeLastSeqNumRecd_Type()
)
panLcLogTypeLastSeqNumRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogTypeLastSeqNumRecd.setStatus("current")
_PanLcLogTypeLastLogGen_Type = TimeStamp
_PanLcLogTypeLastLogGen_Object = MibTableColumn
panLcLogTypeLastLogGen = _PanLcLogTypeLastLogGen_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 5, 1, 5),
    _PanLcLogTypeLastLogGen_Type()
)
panLcLogTypeLastLogGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogTypeLastLogGen.setStatus("current")
_PanDeviceLogging_ObjectIdentity = ObjectIdentity
panDeviceLogging = _PanDeviceLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    panDeviceLogging.setStatus("current")
_PanDeviceLoggingLogRate_ObjectIdentity = ObjectIdentity
panDeviceLoggingLogRate = _PanDeviceLoggingLogRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    panDeviceLoggingLogRate.setStatus("current")
_PanDeviceIncomingLogRate_Type = Unsigned32
_PanDeviceIncomingLogRate_Object = MibScalar
panDeviceIncomingLogRate = _PanDeviceIncomingLogRate_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 1, 1),
    _PanDeviceIncomingLogRate_Type()
)
panDeviceIncomingLogRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceIncomingLogRate.setStatus("current")
_PanDeviceWriteLogRate_Type = Unsigned32
_PanDeviceWriteLogRate_Object = MibScalar
panDeviceWriteLogRate = _PanDeviceWriteLogRate_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 1, 2),
    _PanDeviceWriteLogRate_Type()
)
panDeviceWriteLogRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceWriteLogRate.setStatus("current")
_PanDeviceLoggingLogTypeStatTable_Object = MibTable
panDeviceLoggingLogTypeStatTable = _PanDeviceLoggingLogTypeStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    panDeviceLoggingLogTypeStatTable.setStatus("current")
_PanDeviceLoggingLogTypeStatEntry_Object = MibTableRow
panDeviceLoggingLogTypeStatEntry = _PanDeviceLoggingLogTypeStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 2, 1)
)
panDeviceLoggingLogTypeStatEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panDeviceLoggingDevice"),
    (0, "PAN-COMMON-MIB", "panDeviceLoggingLogType"),
)
if mibBuilder.loadTexts:
    panDeviceLoggingLogTypeStatEntry.setStatus("current")
_PanDeviceLoggingDevice_Type = DisplayString
_PanDeviceLoggingDevice_Object = MibTableColumn
panDeviceLoggingDevice = _PanDeviceLoggingDevice_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 2, 1, 1),
    _PanDeviceLoggingDevice_Type()
)
panDeviceLoggingDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingDevice.setStatus("current")
_PanDeviceLoggingDeviceIndex_Type = Integer32
_PanDeviceLoggingDeviceIndex_Object = MibTableColumn
panDeviceLoggingDeviceIndex = _PanDeviceLoggingDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 2, 1, 2),
    _PanDeviceLoggingDeviceIndex_Type()
)
panDeviceLoggingDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingDeviceIndex.setStatus("current")
_PanDeviceLoggingLogType_Type = DisplayString
_PanDeviceLoggingLogType_Object = MibTableColumn
panDeviceLoggingLogType = _PanDeviceLoggingLogType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 2, 1, 3),
    _PanDeviceLoggingLogType_Type()
)
panDeviceLoggingLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingLogType.setStatus("current")
_PanDeviceLoggingLogLastLogCreated_Type = TimeStamp
_PanDeviceLoggingLogLastLogCreated_Object = MibTableColumn
panDeviceLoggingLogLastLogCreated = _PanDeviceLoggingLogLastLogCreated_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 2, 1, 4),
    _PanDeviceLoggingLogLastLogCreated_Type()
)
panDeviceLoggingLogLastLogCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingLogLastLogCreated.setStatus("current")
_PanDeviceLoggingLogLastLogFwded_Type = TimeStamp
_PanDeviceLoggingLogLastLogFwded_Object = MibTableColumn
panDeviceLoggingLogLastLogFwded = _PanDeviceLoggingLogLastLogFwded_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 2, 1, 5),
    _PanDeviceLoggingLogLastLogFwded_Type()
)
panDeviceLoggingLogLastLogFwded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingLogLastLogFwded.setStatus("current")
_PanDeviceLoggingLogLastSeqNumberFwded_Type = Counter64
_PanDeviceLoggingLogLastSeqNumberFwded_Object = MibTableColumn
panDeviceLoggingLogLastSeqNumberFwded = _PanDeviceLoggingLogLastSeqNumberFwded_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 2, 1, 6),
    _PanDeviceLoggingLogLastSeqNumberFwded_Type()
)
panDeviceLoggingLogLastSeqNumberFwded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingLogLastSeqNumberFwded.setStatus("current")
_PanDeviceLoggingLogLastSeqNumberAck_Type = Counter64
_PanDeviceLoggingLogLastSeqNumberAck_Object = MibTableColumn
panDeviceLoggingLogLastSeqNumberAck = _PanDeviceLoggingLogLastSeqNumberAck_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 2, 1, 7),
    _PanDeviceLoggingLogLastSeqNumberAck_Type()
)
panDeviceLoggingLogLastSeqNumberAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingLogLastSeqNumberAck.setStatus("current")
_PanDeviceLoggingLogTotalLogsFwded_Type = Counter64
_PanDeviceLoggingLogTotalLogsFwded_Object = MibTableColumn
panDeviceLoggingLogTotalLogsFwded = _PanDeviceLoggingLogTotalLogsFwded_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 2, 1, 8),
    _PanDeviceLoggingLogTotalLogsFwded_Type()
)
panDeviceLoggingLogTotalLogsFwded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingLogTotalLogsFwded.setStatus("current")
_PanDeviceLoggingLogUsageTable_Object = MibTable
panDeviceLoggingLogUsageTable = _PanDeviceLoggingLogUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    panDeviceLoggingLogUsageTable.setStatus("current")
_PanDeviceLoggingLogUsageEntry_Object = MibTableRow
panDeviceLoggingLogUsageEntry = _PanDeviceLoggingLogUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 3, 1)
)
panDeviceLoggingLogUsageEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panDeviceLoggingLogUsageLogType"),
)
if mibBuilder.loadTexts:
    panDeviceLoggingLogUsageEntry.setStatus("current")
_PanDeviceLoggingLogUsageLogType_Type = DisplayString
_PanDeviceLoggingLogUsageLogType_Object = MibTableColumn
panDeviceLoggingLogUsageLogType = _PanDeviceLoggingLogUsageLogType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 3, 1, 1),
    _PanDeviceLoggingLogUsageLogType_Type()
)
panDeviceLoggingLogUsageLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingLogUsageLogType.setStatus("current")
_PanDeviceLoggingDiskUsageDiskSpace_Type = DisplayString
_PanDeviceLoggingDiskUsageDiskSpace_Object = MibTableColumn
panDeviceLoggingDiskUsageDiskSpace = _PanDeviceLoggingDiskUsageDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 3, 1, 2),
    _PanDeviceLoggingDiskUsageDiskSpace_Type()
)
panDeviceLoggingDiskUsageDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingDiskUsageDiskSpace.setStatus("current")
_PanDeviceLoggingDiskUsageRetention_Type = Unsigned32
_PanDeviceLoggingDiskUsageRetention_Object = MibTableColumn
panDeviceLoggingDiskUsageRetention = _PanDeviceLoggingDiskUsageRetention_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 3, 1, 3),
    _PanDeviceLoggingDiskUsageRetention_Type()
)
panDeviceLoggingDiskUsageRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingDiskUsageRetention.setStatus("current")
_PanDeviceLoggingDiskQuotaPct_Type = DisplayString
_PanDeviceLoggingDiskQuotaPct_Object = MibTableColumn
panDeviceLoggingDiskQuotaPct = _PanDeviceLoggingDiskQuotaPct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 3, 1, 4),
    _PanDeviceLoggingDiskQuotaPct_Type()
)
panDeviceLoggingDiskQuotaPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingDiskQuotaPct.setStatus("current")
_PanDeviceLoggingDiskQuota_Type = DisplayString
_PanDeviceLoggingDiskQuota_Object = MibTableColumn
panDeviceLoggingDiskQuota = _PanDeviceLoggingDiskQuota_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 3, 1, 5),
    _PanDeviceLoggingDiskQuota_Type()
)
panDeviceLoggingDiskQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingDiskQuota.setStatus("current")
_PanDeviceLoggingExtFwd_ObjectIdentity = ObjectIdentity
panDeviceLoggingExtFwd = _PanDeviceLoggingExtFwd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 4)
)
if mibBuilder.loadTexts:
    panDeviceLoggingExtFwd.setStatus("current")
_PanDeviceLoggingExtFwdCount_Type = Counter64
_PanDeviceLoggingExtFwdCount_Object = MibScalar
panDeviceLoggingExtFwdCount = _PanDeviceLoggingExtFwdCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 4, 1),
    _PanDeviceLoggingExtFwdCount_Type()
)
panDeviceLoggingExtFwdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingExtFwdCount.setStatus("current")
_PanDeviceLoggingExtFwdQueueDrop_Type = Counter64
_PanDeviceLoggingExtFwdQueueDrop_Object = MibScalar
panDeviceLoggingExtFwdQueueDrop = _PanDeviceLoggingExtFwdQueueDrop_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 4, 2),
    _PanDeviceLoggingExtFwdQueueDrop_Type()
)
panDeviceLoggingExtFwdQueueDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingExtFwdQueueDrop.setStatus("current")
_PanDeviceLoggingExtFwdStatsSendErr_Type = Counter64
_PanDeviceLoggingExtFwdStatsSendErr_Object = MibScalar
panDeviceLoggingExtFwdStatsSendErr = _PanDeviceLoggingExtFwdStatsSendErr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 4, 3),
    _PanDeviceLoggingExtFwdStatsSendErr_Type()
)
panDeviceLoggingExtFwdStatsSendErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingExtFwdStatsSendErr.setStatus("current")
_PanDeviceLoggingExtFwdStatsTable_Object = MibTable
panDeviceLoggingExtFwdStatsTable = _PanDeviceLoggingExtFwdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 4, 4)
)
if mibBuilder.loadTexts:
    panDeviceLoggingExtFwdStatsTable.setStatus("current")
_PanDeviceLoggingExtFwdStatsEntry_Object = MibTableRow
panDeviceLoggingExtFwdStatsEntry = _PanDeviceLoggingExtFwdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 4, 4, 1)
)
panDeviceLoggingExtFwdStatsEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panDeviceLoggingExtFwdStatsTableType"),
)
if mibBuilder.loadTexts:
    panDeviceLoggingExtFwdStatsEntry.setStatus("current")
_PanDeviceLoggingExtFwdStatsTableType_Type = DisplayString
_PanDeviceLoggingExtFwdStatsTableType_Object = MibTableColumn
panDeviceLoggingExtFwdStatsTableType = _PanDeviceLoggingExtFwdStatsTableType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 4, 4, 1, 1),
    _PanDeviceLoggingExtFwdStatsTableType_Type()
)
panDeviceLoggingExtFwdStatsTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingExtFwdStatsTableType.setStatus("current")
_PanDeviceLoggingExtFwdStatsTableEnqueueCount_Type = Counter64
_PanDeviceLoggingExtFwdStatsTableEnqueueCount_Object = MibTableColumn
panDeviceLoggingExtFwdStatsTableEnqueueCount = _PanDeviceLoggingExtFwdStatsTableEnqueueCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 4, 4, 1, 2),
    _PanDeviceLoggingExtFwdStatsTableEnqueueCount_Type()
)
panDeviceLoggingExtFwdStatsTableEnqueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingExtFwdStatsTableEnqueueCount.setStatus("current")
_PanDeviceLoggingExtFwdStatsTableSendCount_Type = Counter64
_PanDeviceLoggingExtFwdStatsTableSendCount_Object = MibTableColumn
panDeviceLoggingExtFwdStatsTableSendCount = _PanDeviceLoggingExtFwdStatsTableSendCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 4, 4, 1, 3),
    _PanDeviceLoggingExtFwdStatsTableSendCount_Type()
)
panDeviceLoggingExtFwdStatsTableSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingExtFwdStatsTableSendCount.setStatus("current")
_PanDeviceLoggingExtFwdStatsTableDropCount_Type = Counter64
_PanDeviceLoggingExtFwdStatsTableDropCount_Object = MibTableColumn
panDeviceLoggingExtFwdStatsTableDropCount = _PanDeviceLoggingExtFwdStatsTableDropCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 4, 4, 1, 4),
    _PanDeviceLoggingExtFwdStatsTableDropCount_Type()
)
panDeviceLoggingExtFwdStatsTableDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingExtFwdStatsTableDropCount.setStatus("current")
_PanDeviceLoggingExtFwdStatsTableQueueDepth_Type = Counter64
_PanDeviceLoggingExtFwdStatsTableQueueDepth_Object = MibTableColumn
panDeviceLoggingExtFwdStatsTableQueueDepth = _PanDeviceLoggingExtFwdStatsTableQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 4, 4, 1, 5),
    _PanDeviceLoggingExtFwdStatsTableQueueDepth_Type()
)
panDeviceLoggingExtFwdStatsTableQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingExtFwdStatsTableQueueDepth.setStatus("current")
_PanDeviceLoggingExtFwdStatsTable1minAvgSendRate_Type = Unsigned32
_PanDeviceLoggingExtFwdStatsTable1minAvgSendRate_Object = MibTableColumn
panDeviceLoggingExtFwdStatsTable1minAvgSendRate = _PanDeviceLoggingExtFwdStatsTable1minAvgSendRate_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 4, 4, 1, 6),
    _PanDeviceLoggingExtFwdStatsTable1minAvgSendRate_Type()
)
panDeviceLoggingExtFwdStatsTable1minAvgSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingExtFwdStatsTable1minAvgSendRate.setStatus("current")
_PanDeviceLoggingCollectorConnectionTable_Object = MibTable
panDeviceLoggingCollectorConnectionTable = _PanDeviceLoggingCollectorConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 5)
)
if mibBuilder.loadTexts:
    panDeviceLoggingCollectorConnectionTable.setStatus("current")
_PanDeviceLoggingCollectorConnectionEntry_Object = MibTableRow
panDeviceLoggingCollectorConnectionEntry = _PanDeviceLoggingCollectorConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 5, 1)
)
panDeviceLoggingCollectorConnectionEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panDeviceLoggingCollectorConnectionIP"),
)
if mibBuilder.loadTexts:
    panDeviceLoggingCollectorConnectionEntry.setStatus("current")
_PanDeviceLoggingCollectorConnectionType_Type = DisplayString
_PanDeviceLoggingCollectorConnectionType_Object = MibTableColumn
panDeviceLoggingCollectorConnectionType = _PanDeviceLoggingCollectorConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 5, 1, 1),
    _PanDeviceLoggingCollectorConnectionType_Type()
)
panDeviceLoggingCollectorConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingCollectorConnectionType.setStatus("current")
_PanDeviceLoggingCollectorConnectionIP_Type = DisplayString
_PanDeviceLoggingCollectorConnectionIP_Object = MibTableColumn
panDeviceLoggingCollectorConnectionIP = _PanDeviceLoggingCollectorConnectionIP_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 5, 1, 2),
    _PanDeviceLoggingCollectorConnectionIP_Type()
)
panDeviceLoggingCollectorConnectionIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingCollectorConnectionIP.setStatus("current")
_PanDeviceLoggingCollectorConnectionHostname_Type = DisplayString
_PanDeviceLoggingCollectorConnectionHostname_Object = MibTableColumn
panDeviceLoggingCollectorConnectionHostname = _PanDeviceLoggingCollectorConnectionHostname_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 5, 1, 3),
    _PanDeviceLoggingCollectorConnectionHostname_Type()
)
panDeviceLoggingCollectorConnectionHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingCollectorConnectionHostname.setStatus("current")
_PanDeviceLoggingCollectorConnectionStatus_Type = DisplayString
_PanDeviceLoggingCollectorConnectionStatus_Object = MibTableColumn
panDeviceLoggingCollectorConnectionStatus = _PanDeviceLoggingCollectorConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 7, 5, 1, 4),
    _PanDeviceLoggingCollectorConnectionStatus_Type()
)
panDeviceLoggingCollectorConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDeviceLoggingCollectorConnectionStatus.setStatus("current")
_PanSSLBroker_ObjectIdentity = ObjectIdentity
panSSLBroker = _PanSSLBroker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    panSSLBroker.setStatus("current")
_PanSSLBrokerStatsTable_Object = MibTable
panSSLBrokerStatsTable = _PanSSLBrokerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    panSSLBrokerStatsTable.setStatus("current")
_PanSSLBrokerStatsEntry_Object = MibTableRow
panSSLBrokerStatsEntry = _PanSSLBrokerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 8, 1, 1)
)
panSSLBrokerStatsEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "index"),
)
if mibBuilder.loadTexts:
    panSSLBrokerStatsEntry.setStatus("current")
_Index_Type = Integer32
_Index_Object = MibTableColumn
index = _Index_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 8, 1, 1, 1),
    _Index_Type()
)
index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    index.setStatus("current")
_ChainName_Type = DisplayString
_ChainName_Object = MibTableColumn
chainName = _ChainName_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 8, 1, 1, 2),
    _ChainName_Type()
)
chainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chainName.setStatus("current")
_AvgLatency_Type = Integer32
_AvgLatency_Object = MibTableColumn
avgLatency = _AvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 8, 1, 1, 3),
    _AvgLatency_Type()
)
avgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgLatency.setStatus("current")
_SessionCount_Type = Integer32
_SessionCount_Object = MibTableColumn
sessionCount = _SessionCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 8, 1, 1, 4),
    _SessionCount_Type()
)
sessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCount.setStatus("current")
_PanCommonEvents_ObjectIdentity = ObjectIdentity
panCommonEvents = _PanCommonEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3)
)
if mibBuilder.loadTexts:
    panCommonEvents.setStatus("current")
_PanCommonEventObjs_ObjectIdentity = ObjectIdentity
panCommonEventObjs = _PanCommonEventObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    panCommonEventObjs.setStatus("current")
_PanCommonEventDescr_Type = DisplayString
_PanCommonEventDescr_Object = MibScalar
panCommonEventDescr = _PanCommonEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 1),
    _PanCommonEventDescr_Type()
)
panCommonEventDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCommonEventDescr.setStatus("current")
_PanCommonEventEvents_ObjectIdentity = ObjectIdentity
panCommonEventEvents = _PanCommonEventEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    panCommonEventEvents.setStatus("current")
_PanCommonEventEventsV2_ObjectIdentity = ObjectIdentity
panCommonEventEventsV2 = _PanCommonEventEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0)
)
if mibBuilder.loadTexts:
    panCommonEventEventsV2.setStatus("current")

# Managed Objects groups


# Notification objects

panCommonEventLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1)
)
panCommonEventLog.setObjects(
    ("PAN-COMMON-MIB", "panCommonEventDescr")
)
if mibBuilder.loadTexts:
    panCommonEventLog.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAN-COMMON-MIB",
    **{"FloatValue": FloatValue,
       "panCommonMibModule": panCommonMibModule,
       "panCommonConfMib": panCommonConfMib,
       "panCommonObjs": panCommonObjs,
       "panSys": panSys,
       "panSysSwVersion": panSysSwVersion,
       "panSysHwVersion": panSysHwVersion,
       "panSysSerialNumber": panSysSerialNumber,
       "panSysTimeZoneOffset": panSysTimeZoneOffset,
       "panSysDaylightSaving": panSysDaylightSaving,
       "panSysVpnClientVersion": panSysVpnClientVersion,
       "panSysAppVersion": panSysAppVersion,
       "panSysAvVersion": panSysAvVersion,
       "panSysThreatVersion": panSysThreatVersion,
       "panSysUrlFilteringVersion": panSysUrlFilteringVersion,
       "panSysHAState": panSysHAState,
       "panSysHAPeerState": panSysHAPeerState,
       "panSysHAMode": panSysHAMode,
       "panSysUrlFilteringDatabase": panSysUrlFilteringDatabase,
       "panSysGlobalProtectClientVersion": panSysGlobalProtectClientVersion,
       "panSysOpswatDatafileVersion": panSysOpswatDatafileVersion,
       "panSysWildfireVersion": panSysWildfireVersion,
       "panSysWildfirePrivateCloudVersion": panSysWildfirePrivateCloudVersion,
       "panGlobalCounters": panGlobalCounters,
       "panAhoSw": panAhoSw,
       "panDfaSw": panDfaSw,
       "panFlowHostServiceAllow": panFlowHostServiceAllow,
       "panHaPathmonSent": panHaPathmonSent,
       "panAhoFpga": panAhoFpga,
       "panDfaFpga": panDfaFpga,
       "panFpgaPkt": panFpgaPkt,
       "panGlobalCountersDOSCounters": panGlobalCountersDOSCounters,
       "panFlowDosAgMaxSessLimit": panFlowDosAgMaxSessLimit,
       "panFlowDosBlkNumEntries": panFlowDosBlkNumEntries,
       "panFlowDosClMaxSessLimit": panFlowDosClMaxSessLimit,
       "panFlowDosClSyncookieAckErr": panFlowDosClSyncookieAckErr,
       "panFlowDosClSyncookieAckRcv": panFlowDosClSyncookieAckRcv,
       "panFlowDosClSyncookieBlkDur": panFlowDosClSyncookieBlkDur,
       "panFlowDosClSyncookieMax": panFlowDosClSyncookieMax,
       "panFlowDosClSyncookieSent": panFlowDosClSyncookieSent,
       "panFlowMeterVsysThrottle": panFlowMeterVsysThrottle,
       "panFlowPolicyDeny": panFlowPolicyDeny,
       "panFlowPolicyNat": panFlowPolicyNat,
       "panFlowScanDrop": panFlowScanDrop,
       "panFlowDosDropIpBlocked": panFlowDosDropIpBlocked,
       "panFlowDosRedIcmp": panFlowDosRedIcmp,
       "panFlowDosRedIcmp6": panFlowDosRedIcmp6,
       "panFlowDosRedIp": panFlowDosRedIp,
       "panFlowDosRedTcp": panFlowDosRedTcp,
       "panFlowDosRedUdp": panFlowDosRedUdp,
       "panFlowDosRuleAgBlkDur": panFlowDosRuleAgBlkDur,
       "panFlowDosRuleAgRedAct": panFlowDosRuleAgRedAct,
       "panFlowDosRuleAgRedMax": panFlowDosRuleAgRedMax,
       "panFlowDosRuleDeny": panFlowDosRuleDeny,
       "panFlowDosRuleDrop": panFlowDosRuleDrop,
       "panFlowDosRuleDropAggr": panFlowDosRuleDropAggr,
       "panFlowDosRuleDropClBlkDur": panFlowDosRuleDropClBlkDur,
       "panFlowDosRuleDropClRedAct": panFlowDosRuleDropClRedAct,
       "panFlowDosRuleDropClRedMax": panFlowDosRuleDropClRedMax,
       "panFlowDosRuleDropClassified": panFlowDosRuleDropClassified,
       "panFlowDosSyncookieBlkDur": panFlowDosSyncookieBlkDur,
       "panFlowDosSyncookieMax": panFlowDosSyncookieMax,
       "panFlowDosZoneRedAct": panFlowDosZoneRedAct,
       "panFlowDosZoneRedMax": panFlowDosZoneRedMax,
       "panFlowDosBlkSwEntries": panFlowDosBlkSwEntries,
       "panFlowDosBlkHwEntries": panFlowDosBlkHwEntries,
       "panFlowDosSyncookieNotTcpSyn": panFlowDosSyncookieNotTcpSyn,
       "panFlowDosSyncookieNotTcpSynAck": panFlowDosSyncookieNotTcpSynAck,
       "panFlowDosPfIpspoof": panFlowDosPfIpspoof,
       "panFlowDosPfIpfrag": panFlowDosPfIpfrag,
       "panFlowDosPfPing0": panFlowDosPfPing0,
       "panFlowDosPfIcmpfrag": panFlowDosPfIcmpfrag,
       "panFlowDosPfIcmplpkt": panFlowDosPfIcmplpkt,
       "panFlowDosPfIcmperr": panFlowDosPfIcmperr,
       "panFlowDosPfNoreplyttl": panFlowDosPfNoreplyttl,
       "panFlowDosPfNoreplyneedfrag": panFlowDosPfNoreplyneedfrag,
       "panFlowDosPfStrictsource": panFlowDosPfStrictsource,
       "panFlowDosPfLoosesource": panFlowDosPfLoosesource,
       "panFlowDosPfTimestamp": panFlowDosPfTimestamp,
       "panFlowDosPfRecordroute": panFlowDosPfRecordroute,
       "panFlowDosPfSecurity": panFlowDosPfSecurity,
       "panFlowDosPfSatnetid": panFlowDosPfSatnetid,
       "panFlowDosPfUnknown": panFlowDosPfUnknown,
       "panFlowDosPfBadoption": panFlowDosPfBadoption,
       "panFlowDosPfTcpoverlappingmismatch": panFlowDosPfTcpoverlappingmismatch,
       "panFlowDosPfStrictip": panFlowDosPfStrictip,
       "panFlowDosPfTcpsplithandshake": panFlowDosPfTcpsplithandshake,
       "panFlowDosPfTcpsyndata": panFlowDosPfTcpsyndata,
       "panFlowDosPfTcpsynackdata": panFlowDosPfTcpsynackdata,
       "panFlowDosIp6Route0": panFlowDosIp6Route0,
       "panFlowDosIp6Route1": panFlowDosIp6Route1,
       "panFlowDosIp6Route3": panFlowDosIp6Route3,
       "panFlowDosIp6Route4to252": panFlowDosIp6Route4to252,
       "panFlowDosIp6Route253": panFlowDosIp6Route253,
       "panFlowDosIp6Route254": panFlowDosIp6Route254,
       "panFlowDosIp6Route255": panFlowDosIp6Route255,
       "panFlowDosIp6Ip4cmpt": panFlowDosIp6Ip4cmpt,
       "panFlowDosIp6Acast": panFlowDosIp6Acast,
       "panFlowDosIp6OptionsInvalidIPv6": panFlowDosIp6OptionsInvalidIPv6,
       "panFlowDosIp6Icmpv6ErrorInvalid": panFlowDosIp6Icmpv6ErrorInvalid,
       "panFlowDosIp6NeedlessIpv6FragHdr": panFlowDosIp6NeedlessIpv6FragHdr,
       "panFlowDosIp6RsvdSet": panFlowDosIp6RsvdSet,
       "panFlowDosIPv6ExtHdrHopByHop": panFlowDosIPv6ExtHdrHopByHop,
       "panFlowDosip6IPv6ExtHdrRouting": panFlowDosip6IPv6ExtHdrRouting,
       "panFlowDosIp6IPv6ExtHdrDestOpt": panFlowDosIp6IPv6ExtHdrDestOpt,
       "panFlowDosPbpDrop": panFlowDosPbpDrop,
       "panFlowDosCurrSessIncrFailed": panFlowDosCurrSessIncrFailed,
       "panFlowDosCurrSessDecrFailed": panFlowDosCurrSessDecrFailed,
       "panGlobalCountersDropCounters": panGlobalCountersDropCounters,
       "panFlowFwdL3TtlZero": panFlowFwdL3TtlZero,
       "panFlowMeterHostThrottle": panFlowMeterHostThrottle,
       "panFlowHostServiceDeny": panFlowHostServiceDeny,
       "panFlowHostServiceUnknown": panFlowHostServiceUnknown,
       "panPktAllocFailure": panPktAllocFailure,
       "panPktAllocFailureCos": panPktAllocFailureCos,
       "panSessionDiscard": panSessionDiscard,
       "panGlobalCountersIPFragmentationCounters": panGlobalCountersIPFragmentationCounters,
       "panFlowIpfragFragErr": panFlowIpfragFragErr,
       "panFlowIpfragRecv": panFlowIpfragRecv,
       "panGlobalCountersTCPState": panGlobalCountersTCPState,
       "panTcpAllocWqeFailed": panTcpAllocWqeFailed,
       "panTcpDeny": panTcpDeny,
       "panTcpDropOutOfWnd": panTcpDropOutOfWnd,
       "panTcpDropPacket": panTcpDropPacket,
       "panFlowActionClose": panFlowActionClose,
       "panFlowActionReset": panFlowActionReset,
       "panFlowTcpNonSyn": panFlowTcpNonSyn,
       "panTcpExceedSegLimit": panTcpExceedSegLimit,
       "panGlobalCountersTunnelInspect": panGlobalCountersTunnelInspect,
       "panFlowTciGreDecapSuccess": panFlowTciGreDecapSuccess,
       "panFlowTciGreDecapFailed": panFlowTciGreDecapFailed,
       "panFlowTciGreDecapUnknown": panFlowTciGreDecapUnknown,
       "panFlowTciIpsecDecapSuccess": panFlowTciIpsecDecapSuccess,
       "panFlowTciIpsecDecapFailed": panFlowTciIpsecDecapFailed,
       "panFlowTciIpsecDecapUnknown": panFlowTciIpsecDecapUnknown,
       "panFlowTciGtpDecapSuccess": panFlowTciGtpDecapSuccess,
       "panFlowTciGtpDecapFailed": panFlowTciGtpDecapFailed,
       "panFlowTciGtpDecapUnknown": panFlowTciGtpDecapUnknown,
       "panSysAppReleaseDate": panSysAppReleaseDate,
       "panSysThreatReleaseDate": panSysThreatReleaseDate,
       "panSysAvReleaseDate": panSysAvReleaseDate,
       "panSysWfReleaseDate": panSysWfReleaseDate,
       "panChassis": panChassis,
       "panChassisType": panChassisType,
       "panMSeriesMode": panMSeriesMode,
       "panSession": panSession,
       "panSessionUtilization": panSessionUtilization,
       "panSessionMax": panSessionMax,
       "panSessionActive": panSessionActive,
       "panSessionActiveTcp": panSessionActiveTcp,
       "panSessionActiveUdp": panSessionActiveUdp,
       "panSessionActiveICMP": panSessionActiveICMP,
       "panSessionActiveSslProxy": panSessionActiveSslProxy,
       "panSessionSslProxyUtilization": panSessionSslProxyUtilization,
       "panVsysTable": panVsysTable,
       "panVsysEntry": panVsysEntry,
       "panVsysId": panVsysId,
       "panVsysName": panVsysName,
       "panVsysSessionUtilizationPct": panVsysSessionUtilizationPct,
       "panVsysActiveSessions": panVsysActiveSessions,
       "panVsysMaxSessions": panVsysMaxSessions,
       "panVsysActiveTcpCps": panVsysActiveTcpCps,
       "panVsysActiveUdpCps": panVsysActiveUdpCps,
       "panVsysActiveOtherIpCps": panVsysActiveOtherIpCps,
       "panZoneTable": panZoneTable,
       "panZoneEntry": panZoneEntry,
       "panZoneName": panZoneName,
       "panZoneActiveTcpCps": panZoneActiveTcpCps,
       "panZoneActiveUdpCps": panZoneActiveUdpCps,
       "panZoneActiveOtherIpCps": panZoneActiveOtherIpCps,
       "panIfTable": panIfTable,
       "panIfEntry": panIfEntry,
       "ifIndex": ifIndex,
       "ifDescr": ifDescr,
       "panIfActiveTcpCps": panIfActiveTcpCps,
       "panIfActiveUdpCps": panIfActiveUdpCps,
       "panIfActiveOtherIpCps": panIfActiveOtherIpCps,
       "panMgmt": panMgmt,
       "panMgmtPanoramaConnected": panMgmtPanoramaConnected,
       "panMgmtPanorama2Connected": panMgmtPanorama2Connected,
       "panGlobalProtect": panGlobalProtect,
       "panGPGatewayUtilization": panGPGatewayUtilization,
       "panGPGWUtilizationPct": panGPGWUtilizationPct,
       "panGPGWUtilizationMaxTunnels": panGPGWUtilizationMaxTunnels,
       "panGPGWUtilizationActiveTunnels": panGPGWUtilizationActiveTunnels,
       "panLogCollector": panLogCollector,
       "panLcStat": panLcStat,
       "panLcLogRate": panLcLogRate,
       "panLcLogDuration": panLcLogDuration,
       "panLcLogDurationTraffic": panLcLogDurationTraffic,
       "panLcLogDurationConfig": panLcLogDurationConfig,
       "panLcLogDurationSystem": panLcLogDurationSystem,
       "panLcLogDurationThreat": panLcLogDurationThreat,
       "panLcLogDurationAppstat": panLcLogDurationAppstat,
       "panLcLogDurationTrsum": panLcLogDurationTrsum,
       "panLcLogDurationThsum": panLcLogDurationThsum,
       "panLcLogDurationEvent": panLcLogDurationEvent,
       "panLcLogDurationAlarm": panLcLogDurationAlarm,
       "panLcLogDurationHipmatch": panLcLogDurationHipmatch,
       "panLcLogDurationUserid": panLcLogDurationUserid,
       "panLcDiskUsageTable": panLcDiskUsageTable,
       "panLcDiskUsageEntry": panLcDiskUsageEntry,
       "panLcDiskUsageId": panLcDiskUsageId,
       "panLcDiskUsage": panLcDiskUsage,
       "panLcLogUsageTable": panLcLogUsageTable,
       "panLcLogUsageEntry": panLcLogUsageEntry,
       "panLcLogType": panLcLogType,
       "panLcDiskUsageDiskSpacePct": panLcDiskUsageDiskSpacePct,
       "panLcDiskUsageRetention": panLcDiskUsageRetention,
       "panLcDiskQuotaPct": panLcDiskQuotaPct,
       "panLocalLogUsageTable": panLocalLogUsageTable,
       "panLocalLogUsageEntry": panLocalLogUsageEntry,
       "panLocalLogType": panLocalLogType,
       "panLocalDiskUsageDiskSpace": panLocalDiskUsageDiskSpace,
       "panLocalDiskUsageRetention": panLocalDiskUsageRetention,
       "panLocalDiskQuota": panLocalDiskQuota,
       "panLocalDiskQuotaPct": panLocalDiskQuotaPct,
       "panLcDiskIOPSTable": panLcDiskIOPSTable,
       "panLcDiskIOPSEntry": panLcDiskIOPSEntry,
       "panLcDiskIOPSId": panLcDiskIOPSId,
       "panLcDiskIORead5min": panLcDiskIORead5min,
       "panLcDiskIOWrite5min": panLcDiskIOWrite5min,
       "panLcIsRedundancyMember": panLcIsRedundancyMember,
       "panLcLogFwdStatsTable": panLcLogFwdStatsTable,
       "panLcLogFwdStatsEntry": panLcLogFwdStatsEntry,
       "panLcLogFwdStatsTableType": panLcLogFwdStatsTableType,
       "panLcLogFwdStatsTableEnqueueCount": panLcLogFwdStatsTableEnqueueCount,
       "panLcLogFwdStatsTableSendCount": panLcLogFwdStatsTableSendCount,
       "panLcLogFwdStatsTableDropCount": panLcLogFwdStatsTableDropCount,
       "panLcLogFwdStatsTableQueueDepth": panLcLogFwdStatsTableQueueDepth,
       "panLcLoggingConnectedDeviceTable": panLcLoggingConnectedDeviceTable,
       "panLcLoggingConnectedDeviceEntry": panLcLoggingConnectedDeviceEntry,
       "panLcLoggingConnectedDeviceName": panLcLoggingConnectedDeviceName,
       "panLcLoggingConnectedDeviceConnectionId": panLcLoggingConnectedDeviceConnectionId,
       "panLcLoggingConnectedIdLogRate": panLcLoggingConnectedIdLogRate,
       "panLcLoggingDeviceTable": panLcLoggingDeviceTable,
       "panLcLoggingDeviceEntry": panLcLoggingDeviceEntry,
       "panLcLoggingDeviceConnectionId": panLcLoggingDeviceConnectionId,
       "panLcLoggingLogType": panLcLoggingLogType,
       "panLcLogTypeLastLogRecd": panLcLogTypeLastLogRecd,
       "panLcLogTypeLastSeqNumRecd": panLcLogTypeLastSeqNumRecd,
       "panLcLogTypeLastLogGen": panLcLogTypeLastLogGen,
       "panDeviceLogging": panDeviceLogging,
       "panDeviceLoggingLogRate": panDeviceLoggingLogRate,
       "panDeviceIncomingLogRate": panDeviceIncomingLogRate,
       "panDeviceWriteLogRate": panDeviceWriteLogRate,
       "panDeviceLoggingLogTypeStatTable": panDeviceLoggingLogTypeStatTable,
       "panDeviceLoggingLogTypeStatEntry": panDeviceLoggingLogTypeStatEntry,
       "panDeviceLoggingDevice": panDeviceLoggingDevice,
       "panDeviceLoggingDeviceIndex": panDeviceLoggingDeviceIndex,
       "panDeviceLoggingLogType": panDeviceLoggingLogType,
       "panDeviceLoggingLogLastLogCreated": panDeviceLoggingLogLastLogCreated,
       "panDeviceLoggingLogLastLogFwded": panDeviceLoggingLogLastLogFwded,
       "panDeviceLoggingLogLastSeqNumberFwded": panDeviceLoggingLogLastSeqNumberFwded,
       "panDeviceLoggingLogLastSeqNumberAck": panDeviceLoggingLogLastSeqNumberAck,
       "panDeviceLoggingLogTotalLogsFwded": panDeviceLoggingLogTotalLogsFwded,
       "panDeviceLoggingLogUsageTable": panDeviceLoggingLogUsageTable,
       "panDeviceLoggingLogUsageEntry": panDeviceLoggingLogUsageEntry,
       "panDeviceLoggingLogUsageLogType": panDeviceLoggingLogUsageLogType,
       "panDeviceLoggingDiskUsageDiskSpace": panDeviceLoggingDiskUsageDiskSpace,
       "panDeviceLoggingDiskUsageRetention": panDeviceLoggingDiskUsageRetention,
       "panDeviceLoggingDiskQuotaPct": panDeviceLoggingDiskQuotaPct,
       "panDeviceLoggingDiskQuota": panDeviceLoggingDiskQuota,
       "panDeviceLoggingExtFwd": panDeviceLoggingExtFwd,
       "panDeviceLoggingExtFwdCount": panDeviceLoggingExtFwdCount,
       "panDeviceLoggingExtFwdQueueDrop": panDeviceLoggingExtFwdQueueDrop,
       "panDeviceLoggingExtFwdStatsSendErr": panDeviceLoggingExtFwdStatsSendErr,
       "panDeviceLoggingExtFwdStatsTable": panDeviceLoggingExtFwdStatsTable,
       "panDeviceLoggingExtFwdStatsEntry": panDeviceLoggingExtFwdStatsEntry,
       "panDeviceLoggingExtFwdStatsTableType": panDeviceLoggingExtFwdStatsTableType,
       "panDeviceLoggingExtFwdStatsTableEnqueueCount": panDeviceLoggingExtFwdStatsTableEnqueueCount,
       "panDeviceLoggingExtFwdStatsTableSendCount": panDeviceLoggingExtFwdStatsTableSendCount,
       "panDeviceLoggingExtFwdStatsTableDropCount": panDeviceLoggingExtFwdStatsTableDropCount,
       "panDeviceLoggingExtFwdStatsTableQueueDepth": panDeviceLoggingExtFwdStatsTableQueueDepth,
       "panDeviceLoggingExtFwdStatsTable1minAvgSendRate": panDeviceLoggingExtFwdStatsTable1minAvgSendRate,
       "panDeviceLoggingCollectorConnectionTable": panDeviceLoggingCollectorConnectionTable,
       "panDeviceLoggingCollectorConnectionEntry": panDeviceLoggingCollectorConnectionEntry,
       "panDeviceLoggingCollectorConnectionType": panDeviceLoggingCollectorConnectionType,
       "panDeviceLoggingCollectorConnectionIP": panDeviceLoggingCollectorConnectionIP,
       "panDeviceLoggingCollectorConnectionHostname": panDeviceLoggingCollectorConnectionHostname,
       "panDeviceLoggingCollectorConnectionStatus": panDeviceLoggingCollectorConnectionStatus,
       "panSSLBroker": panSSLBroker,
       "panSSLBrokerStatsTable": panSSLBrokerStatsTable,
       "panSSLBrokerStatsEntry": panSSLBrokerStatsEntry,
       "index": index,
       "chainName": chainName,
       "avgLatency": avgLatency,
       "sessionCount": sessionCount,
       "panCommonEvents": panCommonEvents,
       "panCommonEventObjs": panCommonEventObjs,
       "panCommonEventDescr": panCommonEventDescr,
       "panCommonEventEvents": panCommonEventEvents,
       "panCommonEventEventsV2": panCommonEventEventsV2,
       "panCommonEventLog": panCommonEventLog}
)
