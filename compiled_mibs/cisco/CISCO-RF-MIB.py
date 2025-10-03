# SNMP MIB module (CISCO-RF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCO-RF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:27:18 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
 PhysAddress,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoRFMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 176)
)
if mibBuilder.loadTexts:
    ciscoRFMIB.setRevisions(
        ("2005-09-01 00:00",
         "2004-04-01 00:00",
         "2004-02-04 00:00",
         "2003-10-02 00:00",
         "2002-01-07 00:00",
         "2001-07-20 00:00",
         "2001-06-26 00:00",
         "2001-04-03 09:45")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RFState(TextualConvention, Integer32):
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
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("notKnown", 1),
          ("disabled", 2),
          ("initialization", 3),
          ("negotiation", 4),
          ("standbyCold", 5),
          ("standbyColdConfig", 6),
          ("standbyColdFileSys", 7),
          ("standbyColdBulk", 8),
          ("standbyHot", 9),
          ("activeFast", 10),
          ("activeDrain", 11),
          ("activePreconfig", 12),
          ("activePostconfig", 13),
          ("active", 14),
          ("activeExtraload", 15),
          ("activeHandback", 16))
    )



class RFMode(TextualConvention, Integer32):
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
        *(("nonRedundant", 1),
          ("staticLoadShareNonRedundant", 2),
          ("dynamicLoadShareNonRedundant", 3),
          ("staticLoadShareRedundant", 4),
          ("dynamicLoadShareRedundant", 5),
          ("coldStandbyRedundant", 6),
          ("warmStandbyRedundant", 7),
          ("hotStandbyRedundant", 8))
    )



class RFAction(TextualConvention, Integer32):
    status = "current"
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
        *(("noAction", 0),
          ("reloadPeer", 1),
          ("reloadShelf", 2),
          ("switchActivity", 3),
          ("forceSwitchActivity", 4))
    )



class RFSwactReasonType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("none", 2),
          ("notKnown", 3),
          ("userInitiated", 4),
          ("userForced", 5),
          ("activeUnitFailed", 6),
          ("activeUnitRemoved", 7))
    )



class RFUnitIdentifier(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class RFIssuState(TextualConvention, Integer32):
    status = "deprecated"
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
        *(("unset", 0),
          ("init", 1),
          ("loadVersion", 2),
          ("runVersion", 3),
          ("commitVersion", 4))
    )



class RFIssuStateRev1(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("systemReset", 1),
          ("loadVersion", 3),
          ("loadVersionSwitchover", 4),
          ("runVersion", 6),
          ("runVersionSwitchover", 7),
          ("commitVersion", 9))
    )



class RFClientStatus(TextualConvention, Integer32):
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
        *(("noStatus", 1),
          ("clientNotRedundant", 2),
          ("clientRedundancyInProgress", 3),
          ("clientRedundant", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoRFMIBObjects_ObjectIdentity = ObjectIdentity
ciscoRFMIBObjects = _CiscoRFMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1)
)
_CRFStatus_ObjectIdentity = ObjectIdentity
cRFStatus = _CRFStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1)
)
_CRFStatusUnitId_Type = RFUnitIdentifier
_CRFStatusUnitId_Object = MibScalar
cRFStatusUnitId = _CRFStatusUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 1),
    _CRFStatusUnitId_Type()
)
cRFStatusUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusUnitId.setStatus("current")
_CRFStatusUnitState_Type = RFState
_CRFStatusUnitState_Object = MibScalar
cRFStatusUnitState = _CRFStatusUnitState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 2),
    _CRFStatusUnitState_Type()
)
cRFStatusUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusUnitState.setStatus("current")
_CRFStatusPeerUnitId_Type = RFUnitIdentifier
_CRFStatusPeerUnitId_Object = MibScalar
cRFStatusPeerUnitId = _CRFStatusPeerUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 3),
    _CRFStatusPeerUnitId_Type()
)
cRFStatusPeerUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusPeerUnitId.setStatus("current")
_CRFStatusPeerUnitState_Type = RFState
_CRFStatusPeerUnitState_Object = MibScalar
cRFStatusPeerUnitState = _CRFStatusPeerUnitState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 4),
    _CRFStatusPeerUnitState_Type()
)
cRFStatusPeerUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusPeerUnitState.setStatus("current")
_CRFStatusPrimaryMode_Type = TruthValue
_CRFStatusPrimaryMode_Object = MibScalar
cRFStatusPrimaryMode = _CRFStatusPrimaryMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 5),
    _CRFStatusPrimaryMode_Type()
)
cRFStatusPrimaryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusPrimaryMode.setStatus("current")
_CRFStatusDuplexMode_Type = TruthValue
_CRFStatusDuplexMode_Object = MibScalar
cRFStatusDuplexMode = _CRFStatusDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 6),
    _CRFStatusDuplexMode_Type()
)
cRFStatusDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusDuplexMode.setStatus("current")
_CRFStatusManualSwactInhibit_Type = TruthValue
_CRFStatusManualSwactInhibit_Object = MibScalar
cRFStatusManualSwactInhibit = _CRFStatusManualSwactInhibit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 7),
    _CRFStatusManualSwactInhibit_Type()
)
cRFStatusManualSwactInhibit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusManualSwactInhibit.setStatus("current")
_CRFStatusLastSwactReasonCode_Type = RFSwactReasonType
_CRFStatusLastSwactReasonCode_Object = MibScalar
cRFStatusLastSwactReasonCode = _CRFStatusLastSwactReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 8),
    _CRFStatusLastSwactReasonCode_Type()
)
cRFStatusLastSwactReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusLastSwactReasonCode.setStatus("current")
_CRFStatusFailoverTime_Type = TimeStamp
_CRFStatusFailoverTime_Object = MibScalar
cRFStatusFailoverTime = _CRFStatusFailoverTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 9),
    _CRFStatusFailoverTime_Type()
)
cRFStatusFailoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusFailoverTime.setStatus("current")
_CRFStatusPeerStandByEntryTime_Type = TimeStamp
_CRFStatusPeerStandByEntryTime_Object = MibScalar
cRFStatusPeerStandByEntryTime = _CRFStatusPeerStandByEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 10),
    _CRFStatusPeerStandByEntryTime_Type()
)
cRFStatusPeerStandByEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusPeerStandByEntryTime.setStatus("current")
_CRFStatusRFModeCapsTable_Object = MibTable
cRFStatusRFModeCapsTable = _CRFStatusRFModeCapsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cRFStatusRFModeCapsTable.setStatus("current")
_CRFStatusRFModeCapsEntry_Object = MibTableRow
cRFStatusRFModeCapsEntry = _CRFStatusRFModeCapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 11, 1)
)
cRFStatusRFModeCapsEntry.setIndexNames(
    (0, "CISCO-RF-MIB", "cRFStatusRFModeCapsMode"),
)
if mibBuilder.loadTexts:
    cRFStatusRFModeCapsEntry.setStatus("current")
_CRFStatusRFModeCapsMode_Type = RFMode
_CRFStatusRFModeCapsMode_Object = MibTableColumn
cRFStatusRFModeCapsMode = _CRFStatusRFModeCapsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 11, 1, 1),
    _CRFStatusRFModeCapsMode_Type()
)
cRFStatusRFModeCapsMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cRFStatusRFModeCapsMode.setStatus("current")
_CRFStatusRFModeCapsModeDescr_Type = SnmpAdminString
_CRFStatusRFModeCapsModeDescr_Object = MibTableColumn
cRFStatusRFModeCapsModeDescr = _CRFStatusRFModeCapsModeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 11, 1, 2),
    _CRFStatusRFModeCapsModeDescr_Type()
)
cRFStatusRFModeCapsModeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusRFModeCapsModeDescr.setStatus("current")
_CRFStatusIssuState_Type = RFIssuState
_CRFStatusIssuState_Object = MibScalar
cRFStatusIssuState = _CRFStatusIssuState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 12),
    _CRFStatusIssuState_Type()
)
cRFStatusIssuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusIssuState.setStatus("deprecated")
_CRFStatusIssuStateRev1_Type = RFIssuStateRev1
_CRFStatusIssuStateRev1_Object = MibScalar
cRFStatusIssuStateRev1 = _CRFStatusIssuStateRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 13),
    _CRFStatusIssuStateRev1_Type()
)
cRFStatusIssuStateRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusIssuStateRev1.setStatus("current")
_CRFStatusIssuFromVersion_Type = SnmpAdminString
_CRFStatusIssuFromVersion_Object = MibScalar
cRFStatusIssuFromVersion = _CRFStatusIssuFromVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 14),
    _CRFStatusIssuFromVersion_Type()
)
cRFStatusIssuFromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusIssuFromVersion.setStatus("current")
_CRFStatusIssuToVersion_Type = SnmpAdminString
_CRFStatusIssuToVersion_Object = MibScalar
cRFStatusIssuToVersion = _CRFStatusIssuToVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 1, 15),
    _CRFStatusIssuToVersion_Type()
)
cRFStatusIssuToVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusIssuToVersion.setStatus("current")
_CRFCfg_ObjectIdentity = ObjectIdentity
cRFCfg = _CRFCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2)
)
_CRFCfgSplitMode_Type = TruthValue
_CRFCfgSplitMode_Object = MibScalar
cRFCfgSplitMode = _CRFCfgSplitMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 1),
    _CRFCfgSplitMode_Type()
)
cRFCfgSplitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRFCfgSplitMode.setStatus("deprecated")
_CRFCfgKeepaliveThresh_Type = Unsigned32
_CRFCfgKeepaliveThresh_Object = MibScalar
cRFCfgKeepaliveThresh = _CRFCfgKeepaliveThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 2),
    _CRFCfgKeepaliveThresh_Type()
)
cRFCfgKeepaliveThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRFCfgKeepaliveThresh.setStatus("current")
_CRFCfgKeepaliveThreshMin_Type = Unsigned32
_CRFCfgKeepaliveThreshMin_Object = MibScalar
cRFCfgKeepaliveThreshMin = _CRFCfgKeepaliveThreshMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 3),
    _CRFCfgKeepaliveThreshMin_Type()
)
cRFCfgKeepaliveThreshMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFCfgKeepaliveThreshMin.setStatus("current")
_CRFCfgKeepaliveThreshMax_Type = Unsigned32
_CRFCfgKeepaliveThreshMax_Object = MibScalar
cRFCfgKeepaliveThreshMax = _CRFCfgKeepaliveThreshMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 4),
    _CRFCfgKeepaliveThreshMax_Type()
)
cRFCfgKeepaliveThreshMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFCfgKeepaliveThreshMax.setStatus("current")
_CRFCfgKeepaliveTimer_Type = Unsigned32
_CRFCfgKeepaliveTimer_Object = MibScalar
cRFCfgKeepaliveTimer = _CRFCfgKeepaliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 5),
    _CRFCfgKeepaliveTimer_Type()
)
cRFCfgKeepaliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRFCfgKeepaliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    cRFCfgKeepaliveTimer.setUnits("milliseconds")
_CRFCfgKeepaliveTimerMin_Type = Unsigned32
_CRFCfgKeepaliveTimerMin_Object = MibScalar
cRFCfgKeepaliveTimerMin = _CRFCfgKeepaliveTimerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 6),
    _CRFCfgKeepaliveTimerMin_Type()
)
cRFCfgKeepaliveTimerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFCfgKeepaliveTimerMin.setStatus("current")
if mibBuilder.loadTexts:
    cRFCfgKeepaliveTimerMin.setUnits("milliseconds")
_CRFCfgKeepaliveTimerMax_Type = Unsigned32
_CRFCfgKeepaliveTimerMax_Object = MibScalar
cRFCfgKeepaliveTimerMax = _CRFCfgKeepaliveTimerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 7),
    _CRFCfgKeepaliveTimerMax_Type()
)
cRFCfgKeepaliveTimerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFCfgKeepaliveTimerMax.setStatus("current")
if mibBuilder.loadTexts:
    cRFCfgKeepaliveTimerMax.setUnits("milliseconds")
_CRFCfgNotifTimer_Type = Unsigned32
_CRFCfgNotifTimer_Object = MibScalar
cRFCfgNotifTimer = _CRFCfgNotifTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 8),
    _CRFCfgNotifTimer_Type()
)
cRFCfgNotifTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRFCfgNotifTimer.setStatus("current")
if mibBuilder.loadTexts:
    cRFCfgNotifTimer.setUnits("milliseconds")
_CRFCfgNotifTimerMin_Type = Unsigned32
_CRFCfgNotifTimerMin_Object = MibScalar
cRFCfgNotifTimerMin = _CRFCfgNotifTimerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 9),
    _CRFCfgNotifTimerMin_Type()
)
cRFCfgNotifTimerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFCfgNotifTimerMin.setStatus("current")
if mibBuilder.loadTexts:
    cRFCfgNotifTimerMin.setUnits("milliseconds")
_CRFCfgNotifTimerMax_Type = Unsigned32
_CRFCfgNotifTimerMax_Object = MibScalar
cRFCfgNotifTimerMax = _CRFCfgNotifTimerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 10),
    _CRFCfgNotifTimerMax_Type()
)
cRFCfgNotifTimerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFCfgNotifTimerMax.setStatus("current")
if mibBuilder.loadTexts:
    cRFCfgNotifTimerMax.setUnits("milliseconds")
_CRFCfgAdminAction_Type = RFAction
_CRFCfgAdminAction_Object = MibScalar
cRFCfgAdminAction = _CRFCfgAdminAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 11),
    _CRFCfgAdminAction_Type()
)
cRFCfgAdminAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRFCfgAdminAction.setStatus("current")


class _CRFCfgNotifsEnabled_Type(TruthValue):
    """Custom type cRFCfgNotifsEnabled based on TruthValue"""
    defaultValue = 2


_CRFCfgNotifsEnabled_Type.__name__ = "TruthValue"
_CRFCfgNotifsEnabled_Object = MibScalar
cRFCfgNotifsEnabled = _CRFCfgNotifsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 12),
    _CRFCfgNotifsEnabled_Type()
)
cRFCfgNotifsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRFCfgNotifsEnabled.setStatus("current")
_CRFCfgMaintenanceMode_Type = TruthValue
_CRFCfgMaintenanceMode_Object = MibScalar
cRFCfgMaintenanceMode = _CRFCfgMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 13),
    _CRFCfgMaintenanceMode_Type()
)
cRFCfgMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRFCfgMaintenanceMode.setStatus("current")
_CRFCfgRedundancyMode_Type = RFMode
_CRFCfgRedundancyMode_Object = MibScalar
cRFCfgRedundancyMode = _CRFCfgRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 14),
    _CRFCfgRedundancyMode_Type()
)
cRFCfgRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRFCfgRedundancyMode.setStatus("current")
_CRFCfgRedundancyModeDescr_Type = SnmpAdminString
_CRFCfgRedundancyModeDescr_Object = MibScalar
cRFCfgRedundancyModeDescr = _CRFCfgRedundancyModeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 15),
    _CRFCfgRedundancyModeDescr_Type()
)
cRFCfgRedundancyModeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFCfgRedundancyModeDescr.setStatus("current")
_CRFCfgRedundancyOperMode_Type = RFMode
_CRFCfgRedundancyOperMode_Object = MibScalar
cRFCfgRedundancyOperMode = _CRFCfgRedundancyOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 2, 16),
    _CRFCfgRedundancyOperMode_Type()
)
cRFCfgRedundancyOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFCfgRedundancyOperMode.setStatus("current")
_CRFHistory_ObjectIdentity = ObjectIdentity
cRFHistory = _CRFHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3)
)


class _CRFHistoryTableMaxLength_Type(Unsigned32):
    """Custom type cRFHistoryTableMaxLength based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_CRFHistoryTableMaxLength_Type.__name__ = "Unsigned32"
_CRFHistoryTableMaxLength_Object = MibScalar
cRFHistoryTableMaxLength = _CRFHistoryTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 1),
    _CRFHistoryTableMaxLength_Type()
)
cRFHistoryTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRFHistoryTableMaxLength.setStatus("current")
_CRFHistorySwitchOverTable_Object = MibTable
cRFHistorySwitchOverTable = _CRFHistorySwitchOverTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cRFHistorySwitchOverTable.setStatus("current")
_CRFHistorySwitchOverEntry_Object = MibTableRow
cRFHistorySwitchOverEntry = _CRFHistorySwitchOverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2, 1)
)
cRFHistorySwitchOverEntry.setIndexNames(
    (0, "CISCO-RF-MIB", "cRFHistorySwitchOverIndex"),
)
if mibBuilder.loadTexts:
    cRFHistorySwitchOverEntry.setStatus("current")


class _CRFHistorySwitchOverIndex_Type(Unsigned32):
    """Custom type cRFHistorySwitchOverIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CRFHistorySwitchOverIndex_Type.__name__ = "Unsigned32"
_CRFHistorySwitchOverIndex_Object = MibTableColumn
cRFHistorySwitchOverIndex = _CRFHistorySwitchOverIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2, 1, 1),
    _CRFHistorySwitchOverIndex_Type()
)
cRFHistorySwitchOverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cRFHistorySwitchOverIndex.setStatus("current")
_CRFHistoryPrevActiveUnitId_Type = RFUnitIdentifier
_CRFHistoryPrevActiveUnitId_Object = MibTableColumn
cRFHistoryPrevActiveUnitId = _CRFHistoryPrevActiveUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2, 1, 2),
    _CRFHistoryPrevActiveUnitId_Type()
)
cRFHistoryPrevActiveUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFHistoryPrevActiveUnitId.setStatus("current")
_CRFHistoryCurrActiveUnitId_Type = RFUnitIdentifier
_CRFHistoryCurrActiveUnitId_Object = MibTableColumn
cRFHistoryCurrActiveUnitId = _CRFHistoryCurrActiveUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2, 1, 3),
    _CRFHistoryCurrActiveUnitId_Type()
)
cRFHistoryCurrActiveUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFHistoryCurrActiveUnitId.setStatus("current")
_CRFHistorySwitchOverReason_Type = RFSwactReasonType
_CRFHistorySwitchOverReason_Object = MibTableColumn
cRFHistorySwitchOverReason = _CRFHistorySwitchOverReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2, 1, 4),
    _CRFHistorySwitchOverReason_Type()
)
cRFHistorySwitchOverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFHistorySwitchOverReason.setStatus("current")
_CRFHistorySwactTime_Type = DateAndTime
_CRFHistorySwactTime_Object = MibTableColumn
cRFHistorySwactTime = _CRFHistorySwactTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 2, 1, 5),
    _CRFHistorySwactTime_Type()
)
cRFHistorySwactTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFHistorySwactTime.setStatus("current")
_CRFHistoryColdStarts_Type = Counter32
_CRFHistoryColdStarts_Object = MibScalar
cRFHistoryColdStarts = _CRFHistoryColdStarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 3),
    _CRFHistoryColdStarts_Type()
)
cRFHistoryColdStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFHistoryColdStarts.setStatus("current")
_CRFHistoryStandByAvailTime_Type = TimeInterval
_CRFHistoryStandByAvailTime_Object = MibScalar
cRFHistoryStandByAvailTime = _CRFHistoryStandByAvailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 3, 4),
    _CRFHistoryStandByAvailTime_Type()
)
cRFHistoryStandByAvailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFHistoryStandByAvailTime.setStatus("current")
_CRFClient_ObjectIdentity = ObjectIdentity
cRFClient = _CRFClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4)
)
_CRFStatusRFClientTable_Object = MibTable
cRFStatusRFClientTable = _CRFStatusRFClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cRFStatusRFClientTable.setStatus("current")
_CRFStatusRFClientEntry_Object = MibTableRow
cRFStatusRFClientEntry = _CRFStatusRFClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1, 1)
)
cRFStatusRFClientEntry.setIndexNames(
    (0, "CISCO-RF-MIB", "cRFStatusRFClientID"),
)
if mibBuilder.loadTexts:
    cRFStatusRFClientEntry.setStatus("current")


class _CRFStatusRFClientID_Type(Unsigned32):
    """Custom type cRFStatusRFClientID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CRFStatusRFClientID_Type.__name__ = "Unsigned32"
_CRFStatusRFClientID_Object = MibTableColumn
cRFStatusRFClientID = _CRFStatusRFClientID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1, 1, 1),
    _CRFStatusRFClientID_Type()
)
cRFStatusRFClientID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cRFStatusRFClientID.setStatus("current")
_CRFStatusRFClientDescr_Type = SnmpAdminString
_CRFStatusRFClientDescr_Object = MibTableColumn
cRFStatusRFClientDescr = _CRFStatusRFClientDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1, 1, 2),
    _CRFStatusRFClientDescr_Type()
)
cRFStatusRFClientDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusRFClientDescr.setStatus("current")
_CRFStatusRFClientSeq_Type = Unsigned32
_CRFStatusRFClientSeq_Object = MibTableColumn
cRFStatusRFClientSeq = _CRFStatusRFClientSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1, 1, 3),
    _CRFStatusRFClientSeq_Type()
)
cRFStatusRFClientSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusRFClientSeq.setStatus("current")
_CRFStatusRFClientRedTime_Type = Unsigned32
_CRFStatusRFClientRedTime_Object = MibTableColumn
cRFStatusRFClientRedTime = _CRFStatusRFClientRedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1, 1, 4),
    _CRFStatusRFClientRedTime_Type()
)
cRFStatusRFClientRedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusRFClientRedTime.setStatus("current")
if mibBuilder.loadTexts:
    cRFStatusRFClientRedTime.setUnits("milliseconds")
_CRFStatusRFClientStatus_Type = RFClientStatus
_CRFStatusRFClientStatus_Object = MibTableColumn
cRFStatusRFClientStatus = _CRFStatusRFClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 1, 4, 1, 1, 5),
    _CRFStatusRFClientStatus_Type()
)
cRFStatusRFClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRFStatusRFClientStatus.setStatus("current")
_CiscoRFMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoRFMIBNotificationsPrefix = _CiscoRFMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 2)
)
_CiscoRFMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoRFMIBNotifications = _CiscoRFMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 2, 0)
)
_CiscoRFMIBConformance_ObjectIdentity = ObjectIdentity
ciscoRFMIBConformance = _CiscoRFMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3)
)
_CiscoRFMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoRFMIBCompliances = _CiscoRFMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1)
)
_CiscoRFMIBGroups_ObjectIdentity = ObjectIdentity
ciscoRFMIBGroups = _CiscoRFMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2)
)

# Managed Objects groups

ciscoRFStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 1)
)
ciscoRFStatusGroup.setObjects(
      *(("CISCO-RF-MIB", "cRFStatusUnitId"),
        ("CISCO-RF-MIB", "cRFStatusUnitState"),
        ("CISCO-RF-MIB", "cRFStatusPeerUnitId"),
        ("CISCO-RF-MIB", "cRFStatusPeerUnitState"),
        ("CISCO-RF-MIB", "cRFStatusPrimaryMode"),
        ("CISCO-RF-MIB", "cRFStatusDuplexMode"),
        ("CISCO-RF-MIB", "cRFStatusManualSwactInhibit"),
        ("CISCO-RF-MIB", "cRFStatusLastSwactReasonCode"))
)
if mibBuilder.loadTexts:
    ciscoRFStatusGroup.setStatus("deprecated")

ciscoRFConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 2)
)
ciscoRFConfigGroup.setObjects(
      *(("CISCO-RF-MIB", "cRFCfgSplitMode"),
        ("CISCO-RF-MIB", "cRFCfgKeepaliveThresh"),
        ("CISCO-RF-MIB", "cRFCfgKeepaliveThreshMin"),
        ("CISCO-RF-MIB", "cRFCfgKeepaliveThreshMax"),
        ("CISCO-RF-MIB", "cRFCfgKeepaliveTimer"),
        ("CISCO-RF-MIB", "cRFCfgKeepaliveTimerMin"),
        ("CISCO-RF-MIB", "cRFCfgKeepaliveTimerMax"),
        ("CISCO-RF-MIB", "cRFCfgNotifTimer"),
        ("CISCO-RF-MIB", "cRFCfgNotifTimerMin"),
        ("CISCO-RF-MIB", "cRFCfgNotifTimerMax"),
        ("CISCO-RF-MIB", "cRFCfgAdminAction"),
        ("CISCO-RF-MIB", "cRFCfgNotifsEnabled"),
        ("CISCO-RF-MIB", "cRFCfgRedundancyMode"),
        ("CISCO-RF-MIB", "cRFCfgRedundancyModeDescr"))
)
if mibBuilder.loadTexts:
    ciscoRFConfigGroup.setStatus("deprecated")

ciscoRFConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 4)
)
ciscoRFConfigGroupRev1.setObjects(
      *(("CISCO-RF-MIB", "cRFCfgKeepaliveThresh"),
        ("CISCO-RF-MIB", "cRFCfgKeepaliveThreshMin"),
        ("CISCO-RF-MIB", "cRFCfgKeepaliveThreshMax"),
        ("CISCO-RF-MIB", "cRFCfgKeepaliveTimer"),
        ("CISCO-RF-MIB", "cRFCfgKeepaliveTimerMin"),
        ("CISCO-RF-MIB", "cRFCfgKeepaliveTimerMax"),
        ("CISCO-RF-MIB", "cRFCfgNotifTimer"),
        ("CISCO-RF-MIB", "cRFCfgNotifTimerMin"),
        ("CISCO-RF-MIB", "cRFCfgNotifTimerMax"),
        ("CISCO-RF-MIB", "cRFCfgAdminAction"),
        ("CISCO-RF-MIB", "cRFCfgNotifsEnabled"),
        ("CISCO-RF-MIB", "cRFCfgMaintenanceMode"),
        ("CISCO-RF-MIB", "cRFCfgRedundancyMode"),
        ("CISCO-RF-MIB", "cRFCfgRedundancyModeDescr"))
)
if mibBuilder.loadTexts:
    ciscoRFConfigGroupRev1.setStatus("current")

ciscoRFStatusGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 5)
)
ciscoRFStatusGroupRev1.setObjects(
      *(("CISCO-RF-MIB", "cRFStatusUnitId"),
        ("CISCO-RF-MIB", "cRFStatusUnitState"),
        ("CISCO-RF-MIB", "cRFStatusPeerUnitId"),
        ("CISCO-RF-MIB", "cRFStatusPeerUnitState"),
        ("CISCO-RF-MIB", "cRFStatusPrimaryMode"),
        ("CISCO-RF-MIB", "cRFStatusDuplexMode"),
        ("CISCO-RF-MIB", "cRFStatusManualSwactInhibit"),
        ("CISCO-RF-MIB", "cRFStatusLastSwactReasonCode"),
        ("CISCO-RF-MIB", "cRFStatusFailoverTime"),
        ("CISCO-RF-MIB", "cRFStatusPeerStandByEntryTime"))
)
if mibBuilder.loadTexts:
    ciscoRFStatusGroupRev1.setStatus("current")

ciscoRFHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 6)
)
ciscoRFHistoryGroup.setObjects(
      *(("CISCO-RF-MIB", "cRFHistoryPrevActiveUnitId"),
        ("CISCO-RF-MIB", "cRFHistoryCurrActiveUnitId"),
        ("CISCO-RF-MIB", "cRFHistorySwitchOverReason"),
        ("CISCO-RF-MIB", "cRFHistorySwactTime"),
        ("CISCO-RF-MIB", "cRFHistoryColdStarts"),
        ("CISCO-RF-MIB", "cRFHistoryStandByAvailTime"),
        ("CISCO-RF-MIB", "cRFHistoryTableMaxLength"))
)
if mibBuilder.loadTexts:
    ciscoRFHistoryGroup.setStatus("current")

ciscoRFConfigRFOperModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 7)
)
ciscoRFConfigRFOperModeGroup.setObjects(
    ("CISCO-RF-MIB", "cRFCfgRedundancyOperMode")
)
if mibBuilder.loadTexts:
    ciscoRFConfigRFOperModeGroup.setStatus("current")

ciscoRFStatusRFModeCapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 8)
)
ciscoRFStatusRFModeCapsGroup.setObjects(
    ("CISCO-RF-MIB", "cRFStatusRFModeCapsModeDescr")
)
if mibBuilder.loadTexts:
    ciscoRFStatusRFModeCapsGroup.setStatus("current")

ciscoRFIssuStateObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 11)
)
ciscoRFIssuStateObjGroup.setObjects(
    ("CISCO-RF-MIB", "cRFStatusIssuState")
)
if mibBuilder.loadTexts:
    ciscoRFIssuStateObjGroup.setStatus("deprecated")

ciscoRFIssuStateObjGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 12)
)
ciscoRFIssuStateObjGroupRev1.setObjects(
      *(("CISCO-RF-MIB", "cRFStatusIssuStateRev1"),
        ("CISCO-RF-MIB", "cRFStatusIssuFromVersion"),
        ("CISCO-RF-MIB", "cRFStatusIssuToVersion"))
)
if mibBuilder.loadTexts:
    ciscoRFIssuStateObjGroupRev1.setStatus("current")

ciscoRFStatusClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 13)
)
ciscoRFStatusClientGroup.setObjects(
      *(("CISCO-RF-MIB", "cRFStatusRFClientDescr"),
        ("CISCO-RF-MIB", "cRFStatusRFClientSeq"),
        ("CISCO-RF-MIB", "cRFStatusRFClientRedTime"),
        ("CISCO-RF-MIB", "cRFStatusRFClientStatus"))
)
if mibBuilder.loadTexts:
    ciscoRFStatusClientGroup.setStatus("current")


# Notification objects

ciscoRFSwactNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 2, 0, 1)
)
ciscoRFSwactNotif.setObjects(
      *(("CISCO-RF-MIB", "cRFStatusUnitId"),
        ("SNMPv2-MIB", "sysUpTime"),
        ("CISCO-RF-MIB", "cRFStatusLastSwactReasonCode"))
)
if mibBuilder.loadTexts:
    ciscoRFSwactNotif.setStatus(
        "current"
    )

ciscoRFProgressionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 2, 0, 2)
)
ciscoRFProgressionNotif.setObjects(
      *(("CISCO-RF-MIB", "cRFStatusUnitId"),
        ("CISCO-RF-MIB", "cRFStatusUnitState"),
        ("CISCO-RF-MIB", "cRFStatusPeerUnitId"),
        ("CISCO-RF-MIB", "cRFStatusPeerUnitState"))
)
if mibBuilder.loadTexts:
    ciscoRFProgressionNotif.setStatus(
        "current"
    )

ciscoRFIssuStateNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 2, 0, 3)
)
ciscoRFIssuStateNotif.setObjects(
      *(("CISCO-RF-MIB", "cRFStatusUnitId"),
        ("CISCO-RF-MIB", "cRFStatusUnitState"),
        ("CISCO-RF-MIB", "cRFStatusIssuState"))
)
if mibBuilder.loadTexts:
    ciscoRFIssuStateNotif.setStatus(
        "deprecated"
    )

ciscoRFIssuStateNotifRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 2, 0, 4)
)
ciscoRFIssuStateNotifRev1.setObjects(
      *(("CISCO-RF-MIB", "cRFStatusIssuStateRev1"),
        ("CISCO-RF-MIB", "cRFStatusIssuFromVersion"),
        ("CISCO-RF-MIB", "cRFStatusIssuToVersion"),
        ("CISCO-RF-MIB", "cRFStatusLastSwactReasonCode"))
)
if mibBuilder.loadTexts:
    ciscoRFIssuStateNotifRev1.setStatus(
        "current"
    )


# Notifications groups

ciscoRFNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 3)
)
ciscoRFNotifGroup.setObjects(
      *(("CISCO-RF-MIB", "ciscoRFSwactNotif"),
        ("CISCO-RF-MIB", "ciscoRFProgressionNotif"))
)
if mibBuilder.loadTexts:
    ciscoRFNotifGroup.setStatus(
        "current"
    )

ciscoRFIssuStateNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 9)
)
ciscoRFIssuStateNotifGroup.setObjects(
    ("CISCO-RF-MIB", "ciscoRFIssuStateNotif")
)
if mibBuilder.loadTexts:
    ciscoRFIssuStateNotifGroup.setStatus(
        "deprecated"
    )

ciscoRFIssuStateNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 2, 10)
)
ciscoRFIssuStateNotifGroupRev1.setObjects(
    ("CISCO-RF-MIB", "ciscoRFIssuStateNotifRev1")
)
if mibBuilder.loadTexts:
    ciscoRFIssuStateNotifGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoRFMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1, 1)
)
ciscoRFMIBCompliance.setObjects(
      *(("CISCO-RF-MIB", "ciscoRFStatusGroup"),
        ("CISCO-RF-MIB", "ciscoRFConfigGroup"),
        ("CISCO-RF-MIB", "ciscoRFNotifGroup"))
)
if mibBuilder.loadTexts:
    ciscoRFMIBCompliance.setStatus(
        "deprecated"
    )

ciscoRFMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1, 2)
)
ciscoRFMIBComplianceRev1.setObjects(
      *(("CISCO-RF-MIB", "ciscoRFStatusGroup"),
        ("CISCO-RF-MIB", "ciscoRFConfigGroupRev1"),
        ("CISCO-RF-MIB", "ciscoRFNotifGroup"))
)
if mibBuilder.loadTexts:
    ciscoRFMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoRFMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1, 3)
)
ciscoRFMIBComplianceRev2.setObjects(
      *(("CISCO-RF-MIB", "ciscoRFStatusGroupRev1"),
        ("CISCO-RF-MIB", "ciscoRFConfigGroupRev1"),
        ("CISCO-RF-MIB", "ciscoRFNotifGroup"),
        ("CISCO-RF-MIB", "ciscoRFHistoryGroup"))
)
if mibBuilder.loadTexts:
    ciscoRFMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoRFMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1, 4)
)
ciscoRFMIBComplianceRev3.setObjects(
      *(("CISCO-RF-MIB", "ciscoRFStatusGroupRev1"),
        ("CISCO-RF-MIB", "ciscoRFConfigGroupRev1"),
        ("CISCO-RF-MIB", "ciscoRFNotifGroup"),
        ("CISCO-RF-MIB", "ciscoRFHistoryGroup"),
        ("CISCO-RF-MIB", "ciscoRFConfigRFOperModeGroup"),
        ("CISCO-RF-MIB", "ciscoRFStatusRFModeCapsGroup"),
        ("CISCO-RF-MIB", "ciscoRFIssuStateNotifGroup"),
        ("CISCO-RF-MIB", "ciscoRFIssuStateObjGroup"))
)
if mibBuilder.loadTexts:
    ciscoRFMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoRFMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1, 5)
)
ciscoRFMIBComplianceRev4.setObjects(
      *(("CISCO-RF-MIB", "ciscoRFStatusGroupRev1"),
        ("CISCO-RF-MIB", "ciscoRFConfigGroupRev1"),
        ("CISCO-RF-MIB", "ciscoRFNotifGroup"),
        ("CISCO-RF-MIB", "ciscoRFHistoryGroup"),
        ("CISCO-RF-MIB", "ciscoRFConfigRFOperModeGroup"),
        ("CISCO-RF-MIB", "ciscoRFStatusRFModeCapsGroup"),
        ("CISCO-RF-MIB", "ciscoRFIssuStateNotifGroupRev1"),
        ("CISCO-RF-MIB", "ciscoRFIssuStateObjGroupRev1"))
)
if mibBuilder.loadTexts:
    ciscoRFMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoRFMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 176, 3, 1, 6)
)
ciscoRFMIBComplianceRev5.setObjects(
      *(("CISCO-RF-MIB", "ciscoRFStatusGroupRev1"),
        ("CISCO-RF-MIB", "ciscoRFConfigGroupRev1"),
        ("CISCO-RF-MIB", "ciscoRFNotifGroup"),
        ("CISCO-RF-MIB", "ciscoRFHistoryGroup"),
        ("CISCO-RF-MIB", "ciscoRFConfigRFOperModeGroup"),
        ("CISCO-RF-MIB", "ciscoRFStatusRFModeCapsGroup"),
        ("CISCO-RF-MIB", "ciscoRFIssuStateNotifGroupRev1"),
        ("CISCO-RF-MIB", "ciscoRFIssuStateObjGroupRev1"),
        ("CISCO-RF-MIB", "ciscoRFStatusClientGroup"))
)
if mibBuilder.loadTexts:
    ciscoRFMIBComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RF-MIB",
    **{"RFState": RFState,
       "RFMode": RFMode,
       "RFAction": RFAction,
       "RFSwactReasonType": RFSwactReasonType,
       "RFUnitIdentifier": RFUnitIdentifier,
       "RFIssuState": RFIssuState,
       "RFIssuStateRev1": RFIssuStateRev1,
       "RFClientStatus": RFClientStatus,
       "ciscoRFMIB": ciscoRFMIB,
       "ciscoRFMIBObjects": ciscoRFMIBObjects,
       "cRFStatus": cRFStatus,
       "cRFStatusUnitId": cRFStatusUnitId,
       "cRFStatusUnitState": cRFStatusUnitState,
       "cRFStatusPeerUnitId": cRFStatusPeerUnitId,
       "cRFStatusPeerUnitState": cRFStatusPeerUnitState,
       "cRFStatusPrimaryMode": cRFStatusPrimaryMode,
       "cRFStatusDuplexMode": cRFStatusDuplexMode,
       "cRFStatusManualSwactInhibit": cRFStatusManualSwactInhibit,
       "cRFStatusLastSwactReasonCode": cRFStatusLastSwactReasonCode,
       "cRFStatusFailoverTime": cRFStatusFailoverTime,
       "cRFStatusPeerStandByEntryTime": cRFStatusPeerStandByEntryTime,
       "cRFStatusRFModeCapsTable": cRFStatusRFModeCapsTable,
       "cRFStatusRFModeCapsEntry": cRFStatusRFModeCapsEntry,
       "cRFStatusRFModeCapsMode": cRFStatusRFModeCapsMode,
       "cRFStatusRFModeCapsModeDescr": cRFStatusRFModeCapsModeDescr,
       "cRFStatusIssuState": cRFStatusIssuState,
       "cRFStatusIssuStateRev1": cRFStatusIssuStateRev1,
       "cRFStatusIssuFromVersion": cRFStatusIssuFromVersion,
       "cRFStatusIssuToVersion": cRFStatusIssuToVersion,
       "cRFCfg": cRFCfg,
       "cRFCfgSplitMode": cRFCfgSplitMode,
       "cRFCfgKeepaliveThresh": cRFCfgKeepaliveThresh,
       "cRFCfgKeepaliveThreshMin": cRFCfgKeepaliveThreshMin,
       "cRFCfgKeepaliveThreshMax": cRFCfgKeepaliveThreshMax,
       "cRFCfgKeepaliveTimer": cRFCfgKeepaliveTimer,
       "cRFCfgKeepaliveTimerMin": cRFCfgKeepaliveTimerMin,
       "cRFCfgKeepaliveTimerMax": cRFCfgKeepaliveTimerMax,
       "cRFCfgNotifTimer": cRFCfgNotifTimer,
       "cRFCfgNotifTimerMin": cRFCfgNotifTimerMin,
       "cRFCfgNotifTimerMax": cRFCfgNotifTimerMax,
       "cRFCfgAdminAction": cRFCfgAdminAction,
       "cRFCfgNotifsEnabled": cRFCfgNotifsEnabled,
       "cRFCfgMaintenanceMode": cRFCfgMaintenanceMode,
       "cRFCfgRedundancyMode": cRFCfgRedundancyMode,
       "cRFCfgRedundancyModeDescr": cRFCfgRedundancyModeDescr,
       "cRFCfgRedundancyOperMode": cRFCfgRedundancyOperMode,
       "cRFHistory": cRFHistory,
       "cRFHistoryTableMaxLength": cRFHistoryTableMaxLength,
       "cRFHistorySwitchOverTable": cRFHistorySwitchOverTable,
       "cRFHistorySwitchOverEntry": cRFHistorySwitchOverEntry,
       "cRFHistorySwitchOverIndex": cRFHistorySwitchOverIndex,
       "cRFHistoryPrevActiveUnitId": cRFHistoryPrevActiveUnitId,
       "cRFHistoryCurrActiveUnitId": cRFHistoryCurrActiveUnitId,
       "cRFHistorySwitchOverReason": cRFHistorySwitchOverReason,
       "cRFHistorySwactTime": cRFHistorySwactTime,
       "cRFHistoryColdStarts": cRFHistoryColdStarts,
       "cRFHistoryStandByAvailTime": cRFHistoryStandByAvailTime,
       "cRFClient": cRFClient,
       "cRFStatusRFClientTable": cRFStatusRFClientTable,
       "cRFStatusRFClientEntry": cRFStatusRFClientEntry,
       "cRFStatusRFClientID": cRFStatusRFClientID,
       "cRFStatusRFClientDescr": cRFStatusRFClientDescr,
       "cRFStatusRFClientSeq": cRFStatusRFClientSeq,
       "cRFStatusRFClientRedTime": cRFStatusRFClientRedTime,
       "cRFStatusRFClientStatus": cRFStatusRFClientStatus,
       "ciscoRFMIBNotificationsPrefix": ciscoRFMIBNotificationsPrefix,
       "ciscoRFMIBNotifications": ciscoRFMIBNotifications,
       "ciscoRFSwactNotif": ciscoRFSwactNotif,
       "ciscoRFProgressionNotif": ciscoRFProgressionNotif,
       "ciscoRFIssuStateNotif": ciscoRFIssuStateNotif,
       "ciscoRFIssuStateNotifRev1": ciscoRFIssuStateNotifRev1,
       "ciscoRFMIBConformance": ciscoRFMIBConformance,
       "ciscoRFMIBCompliances": ciscoRFMIBCompliances,
       "ciscoRFMIBCompliance": ciscoRFMIBCompliance,
       "ciscoRFMIBComplianceRev1": ciscoRFMIBComplianceRev1,
       "ciscoRFMIBComplianceRev2": ciscoRFMIBComplianceRev2,
       "ciscoRFMIBComplianceRev3": ciscoRFMIBComplianceRev3,
       "ciscoRFMIBComplianceRev4": ciscoRFMIBComplianceRev4,
       "ciscoRFMIBComplianceRev5": ciscoRFMIBComplianceRev5,
       "ciscoRFMIBGroups": ciscoRFMIBGroups,
       "ciscoRFStatusGroup": ciscoRFStatusGroup,
       "ciscoRFConfigGroup": ciscoRFConfigGroup,
       "ciscoRFNotifGroup": ciscoRFNotifGroup,
       "ciscoRFConfigGroupRev1": ciscoRFConfigGroupRev1,
       "ciscoRFStatusGroupRev1": ciscoRFStatusGroupRev1,
       "ciscoRFHistoryGroup": ciscoRFHistoryGroup,
       "ciscoRFConfigRFOperModeGroup": ciscoRFConfigRFOperModeGroup,
       "ciscoRFStatusRFModeCapsGroup": ciscoRFStatusRFModeCapsGroup,
       "ciscoRFIssuStateNotifGroup": ciscoRFIssuStateNotifGroup,
       "ciscoRFIssuStateNotifGroupRev1": ciscoRFIssuStateNotifGroupRev1,
       "ciscoRFIssuStateObjGroup": ciscoRFIssuStateObjGroup,
       "ciscoRFIssuStateObjGroupRev1": ciscoRFIssuStateObjGroupRev1,
       "ciscoRFStatusClientGroup": ciscoRFStatusClientGroup}
)
