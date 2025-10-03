# SNMP MIB module (ALCATEL-IND1-LBD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-LBD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:39 2025
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

(alaLbdTraps,
 softentIND1Lbd) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "alaLbdTraps",
    "softentIND1Lbd")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1LBDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LBDMIB.setRevisions(
        ("2008-12-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaLbdPortConfigLbdOperStatus(TextualConvention, Integer32):
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
        *(("inactive", 0),
          ("normal", 1),
          ("shutdown", 2))
    )



class AlaLbdCurrentStateCVAorAR(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("normal", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1LBDMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1LBDMIBObjects = _AlcatelIND1LBDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LBDMIBObjects.setStatus("current")


class _AlaLbdGlobalConfigStatus_Type(Integer32):
    """Custom type alaLbdGlobalConfigStatus based on Integer32"""
    defaultValue = 2

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


_AlaLbdGlobalConfigStatus_Type.__name__ = "Integer32"
_AlaLbdGlobalConfigStatus_Object = MibScalar
alaLbdGlobalConfigStatus = _AlaLbdGlobalConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 1),
    _AlaLbdGlobalConfigStatus_Type()
)
alaLbdGlobalConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdGlobalConfigStatus.setStatus("current")


class _AlaLbdGlobalConfigTransmissionTimer_Type(Unsigned32):
    """Custom type alaLbdGlobalConfigTransmissionTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_AlaLbdGlobalConfigTransmissionTimer_Type.__name__ = "Unsigned32"
_AlaLbdGlobalConfigTransmissionTimer_Object = MibScalar
alaLbdGlobalConfigTransmissionTimer = _AlaLbdGlobalConfigTransmissionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 2),
    _AlaLbdGlobalConfigTransmissionTimer_Type()
)
alaLbdGlobalConfigTransmissionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdGlobalConfigTransmissionTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaLbdGlobalConfigTransmissionTimer.setUnits("seconds")


class _AlaLbdGlobalClearPortStat_Type(Integer32):
    """Custom type alaLbdGlobalClearPortStat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaLbdGlobalClearPortStat_Type.__name__ = "Integer32"
_AlaLbdGlobalClearPortStat_Object = MibScalar
alaLbdGlobalClearPortStat = _AlaLbdGlobalClearPortStat_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 3),
    _AlaLbdGlobalClearPortStat_Type()
)
alaLbdGlobalClearPortStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdGlobalClearPortStat.setStatus("current")


class _AlaLbdGlobalConfigAutorecoveryTimer_Type(Unsigned32):
    """Custom type alaLbdGlobalConfigAutorecoveryTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_AlaLbdGlobalConfigAutorecoveryTimer_Type.__name__ = "Unsigned32"
_AlaLbdGlobalConfigAutorecoveryTimer_Object = MibScalar
alaLbdGlobalConfigAutorecoveryTimer = _AlaLbdGlobalConfigAutorecoveryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 4),
    _AlaLbdGlobalConfigAutorecoveryTimer_Type()
)
alaLbdGlobalConfigAutorecoveryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdGlobalConfigAutorecoveryTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaLbdGlobalConfigAutorecoveryTimer.setUnits("seconds")
_AlaLbdPortConfig_ObjectIdentity = ObjectIdentity
alaLbdPortConfig = _AlaLbdPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 5)
)
_AlaLbdPortConfigTable_Object = MibTable
alaLbdPortConfigTable = _AlaLbdPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alaLbdPortConfigTable.setStatus("current")
_AlaLbdPortConfigEntry_Object = MibTableRow
alaLbdPortConfigEntry = _AlaLbdPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 5, 1, 1)
)
alaLbdPortConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-LBD-MIB", "alaLbdPortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    alaLbdPortConfigEntry.setStatus("current")
_AlaLbdPortConfigIfIndex_Type = InterfaceIndex
_AlaLbdPortConfigIfIndex_Object = MibTableColumn
alaLbdPortConfigIfIndex = _AlaLbdPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 5, 1, 1, 1),
    _AlaLbdPortConfigIfIndex_Type()
)
alaLbdPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaLbdPortConfigIfIndex.setStatus("current")


class _AlaLbdPortConfigLbdAdminStatus_Type(Integer32):
    """Custom type alaLbdPortConfigLbdAdminStatus based on Integer32"""
    defaultValue = 2

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


_AlaLbdPortConfigLbdAdminStatus_Type.__name__ = "Integer32"
_AlaLbdPortConfigLbdAdminStatus_Object = MibTableColumn
alaLbdPortConfigLbdAdminStatus = _AlaLbdPortConfigLbdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 5, 1, 1, 2),
    _AlaLbdPortConfigLbdAdminStatus_Type()
)
alaLbdPortConfigLbdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdPortConfigLbdAdminStatus.setStatus("current")
_AlaLbdPortConfigLbdOperStatus_Type = AlaLbdPortConfigLbdOperStatus
_AlaLbdPortConfigLbdOperStatus_Object = MibTableColumn
alaLbdPortConfigLbdOperStatus = _AlaLbdPortConfigLbdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 5, 1, 1, 3),
    _AlaLbdPortConfigLbdOperStatus_Type()
)
alaLbdPortConfigLbdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLbdPortConfigLbdOperStatus.setStatus("current")
_AlaLbdPortStat_ObjectIdentity = ObjectIdentity
alaLbdPortStat = _AlaLbdPortStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 6)
)
_AlaLbdPortStatsTable_Object = MibTable
alaLbdPortStatsTable = _AlaLbdPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    alaLbdPortStatsTable.setStatus("current")
_AlaLbdPortStatsEntry_Object = MibTableRow
alaLbdPortStatsEntry = _AlaLbdPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 6, 1, 1)
)
alaLbdPortStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-LBD-MIB", "alaLbdPortStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaLbdPortStatsEntry.setStatus("current")
_AlaLbdPortStatsIfIndex_Type = InterfaceIndex
_AlaLbdPortStatsIfIndex_Object = MibTableColumn
alaLbdPortStatsIfIndex = _AlaLbdPortStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 6, 1, 1, 1),
    _AlaLbdPortStatsIfIndex_Type()
)
alaLbdPortStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaLbdPortStatsIfIndex.setStatus("current")
_AlaLbdPortNumLbdInvalidRcvd_Type = Counter32
_AlaLbdPortNumLbdInvalidRcvd_Object = MibTableColumn
alaLbdPortNumLbdInvalidRcvd = _AlaLbdPortNumLbdInvalidRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 6, 1, 1, 2),
    _AlaLbdPortNumLbdInvalidRcvd_Type()
)
alaLbdPortNumLbdInvalidRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLbdPortNumLbdInvalidRcvd.setStatus("current")
_AlaLbdPortLbdSent_Type = Counter32
_AlaLbdPortLbdSent_Object = MibTableColumn
alaLbdPortLbdSent = _AlaLbdPortLbdSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 6, 1, 1, 3),
    _AlaLbdPortLbdSent_Type()
)
alaLbdPortLbdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLbdPortLbdSent.setStatus("current")


class _AlaLbdPortStatsClear_Type(Integer32):
    """Custom type alaLbdPortStatsClear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaLbdPortStatsClear_Type.__name__ = "Integer32"
_AlaLbdPortStatsClear_Object = MibTableColumn
alaLbdPortStatsClear = _AlaLbdPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 1, 6, 1, 1, 4),
    _AlaLbdPortStatsClear_Type()
)
alaLbdPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdPortStatsClear.setStatus("current")
_AlcatelIND1LBDMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1LBDMIBConformance = _AlcatelIND1LBDMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1LBDMIBConformance.setStatus("current")
_AlcatelIND1LBDMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1LBDMIBGroups = _AlcatelIND1LBDMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LBDMIBGroups.setStatus("current")
_AlcatelIND1LBDMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1LBDMIBCompliances = _AlcatelIND1LBDMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1LBDMIBCompliances.setStatus("current")
_AlaLbdTrapsDesc_ObjectIdentity = ObjectIdentity
alaLbdTrapsDesc = _AlaLbdTrapsDesc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 22, 1)
)
_AlaLbdTrapsRoot_ObjectIdentity = ObjectIdentity
alaLbdTrapsRoot = _AlaLbdTrapsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 22, 1, 0)
)
_AlaLbdTrapsObj_ObjectIdentity = ObjectIdentity
alaLbdTrapsObj = _AlaLbdTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 22, 2)
)
_AlaLbdPortIfIndex_Type = InterfaceIndex
_AlaLbdPortIfIndex_Object = MibScalar
alaLbdPortIfIndex = _AlaLbdPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 22, 2, 1),
    _AlaLbdPortIfIndex_Type()
)
alaLbdPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdPortIfIndex.setStatus("current")


class _AlaLbdPreviousState_Type(Integer32):
    """Custom type alaLbdPreviousState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("normal", 1)
    )


_AlaLbdPreviousState_Type.__name__ = "Integer32"
_AlaLbdPreviousState_Object = MibScalar
alaLbdPreviousState = _AlaLbdPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 22, 2, 2),
    _AlaLbdPreviousState_Type()
)
alaLbdPreviousState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdPreviousState.setStatus("current")


class _AlaLbdCurrentState_Type(Integer32):
    """Custom type alaLbdCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("shutdown", 1)
    )


_AlaLbdCurrentState_Type.__name__ = "Integer32"
_AlaLbdCurrentState_Object = MibScalar
alaLbdCurrentState = _AlaLbdCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 22, 2, 3),
    _AlaLbdCurrentState_Type()
)
alaLbdCurrentState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdCurrentState.setStatus("current")


class _AlaLbdPreviousStateClearViolationAll_Type(Integer32):
    """Custom type alaLbdPreviousStateClearViolationAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("shutdown", 1)
    )


_AlaLbdPreviousStateClearViolationAll_Type.__name__ = "Integer32"
_AlaLbdPreviousStateClearViolationAll_Object = MibScalar
alaLbdPreviousStateClearViolationAll = _AlaLbdPreviousStateClearViolationAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 22, 2, 4),
    _AlaLbdPreviousStateClearViolationAll_Type()
)
alaLbdPreviousStateClearViolationAll.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdPreviousStateClearViolationAll.setStatus("current")
_AlaLbdCurrentStateClearViolationAll_Type = AlaLbdCurrentStateCVAorAR
_AlaLbdCurrentStateClearViolationAll_Object = MibScalar
alaLbdCurrentStateClearViolationAll = _AlaLbdCurrentStateClearViolationAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 22, 2, 5),
    _AlaLbdCurrentStateClearViolationAll_Type()
)
alaLbdCurrentStateClearViolationAll.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdCurrentStateClearViolationAll.setStatus("current")


class _AlaLbdPreviousStateAutoRecovery_Type(Integer32):
    """Custom type alaLbdPreviousStateAutoRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("shutdown", 1)
    )


_AlaLbdPreviousStateAutoRecovery_Type.__name__ = "Integer32"
_AlaLbdPreviousStateAutoRecovery_Object = MibScalar
alaLbdPreviousStateAutoRecovery = _AlaLbdPreviousStateAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 22, 2, 6),
    _AlaLbdPreviousStateAutoRecovery_Type()
)
alaLbdPreviousStateAutoRecovery.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdPreviousStateAutoRecovery.setStatus("current")
_AlaLbdCurrentStateAutoRecovery_Type = AlaLbdCurrentStateCVAorAR
_AlaLbdCurrentStateAutoRecovery_Object = MibScalar
alaLbdCurrentStateAutoRecovery = _AlaLbdCurrentStateAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 22, 2, 7),
    _AlaLbdCurrentStateAutoRecovery_Type()
)
alaLbdCurrentStateAutoRecovery.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdCurrentStateAutoRecovery.setStatus("current")

# Managed Objects groups

alaLbdGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 2, 1, 1)
)
alaLbdGlobalConfigGroup.setObjects(
      *(("ALCATEL-IND1-LBD-MIB", "alaLbdGlobalConfigStatus"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdGlobalConfigTransmissionTimer"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdGlobalClearPortStat"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdGlobalConfigAutorecoveryTimer"))
)
if mibBuilder.loadTexts:
    alaLbdGlobalConfigGroup.setStatus("current")

alaLbdIntfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 2, 1, 2)
)
alaLbdIntfConfigGroup.setObjects(
      *(("ALCATEL-IND1-LBD-MIB", "alaLbdPortConfigLbdAdminStatus"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdPortConfigLbdOperStatus"))
)
if mibBuilder.loadTexts:
    alaLbdIntfConfigGroup.setStatus("current")

alaLbdPortStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 2, 1, 3)
)
alaLbdPortStatusGroup.setObjects(
      *(("ALCATEL-IND1-LBD-MIB", "alaLbdPortNumLbdInvalidRcvd"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdPortLbdSent"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdPortStatsClear"))
)
if mibBuilder.loadTexts:
    alaLbdPortStatusGroup.setStatus("current")

alaLbdStateTrapToShutdownGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 2, 1, 4)
)
alaLbdStateTrapToShutdownGroup.setObjects(
      *(("ALCATEL-IND1-LBD-MIB", "alaLbdPreviousState"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdCurrentState"))
)
if mibBuilder.loadTexts:
    alaLbdStateTrapToShutdownGroup.setStatus("current")

alaLbdStateTrapForClearViolationAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 2, 1, 5)
)
alaLbdStateTrapForClearViolationAllGroup.setObjects(
      *(("ALCATEL-IND1-LBD-MIB", "alaLbdPreviousStateClearViolationAll"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdCurrentStateClearViolationAll"))
)
if mibBuilder.loadTexts:
    alaLbdStateTrapForClearViolationAllGroup.setStatus("current")

alaLbdStateTrapForAutoRecoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 2, 1, 6)
)
alaLbdStateTrapForAutoRecoveryGroup.setObjects(
      *(("ALCATEL-IND1-LBD-MIB", "alaLbdPreviousStateAutoRecovery"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdCurrentStateAutoRecovery"))
)
if mibBuilder.loadTexts:
    alaLbdStateTrapForAutoRecoveryGroup.setStatus("current")


# Notification objects

alaLbdStateChangeToShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 22, 1, 0, 1)
)
alaLbdStateChangeToShutdown.setObjects(
      *(("ALCATEL-IND1-LBD-MIB", "alaLbdPortIfIndex"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdPreviousState"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdCurrentState"))
)
if mibBuilder.loadTexts:
    alaLbdStateChangeToShutdown.setStatus(
        "current"
    )

alaLbdStateChangeForClearViolationAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 22, 1, 0, 2)
)
alaLbdStateChangeForClearViolationAll.setObjects(
      *(("ALCATEL-IND1-LBD-MIB", "alaLbdPortIfIndex"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdPreviousStateClearViolationAll"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdCurrentStateClearViolationAll"))
)
if mibBuilder.loadTexts:
    alaLbdStateChangeForClearViolationAll.setStatus(
        "current"
    )

alaLbdStateChangeForAutoRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 22, 1, 0, 3)
)
alaLbdStateChangeForAutoRecovery.setObjects(
      *(("ALCATEL-IND1-LBD-MIB", "alaLbdPortIfIndex"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdPreviousStateAutoRecovery"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdCurrentStateAutoRecovery"))
)
if mibBuilder.loadTexts:
    alaLbdStateChangeForAutoRecovery.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1LBDMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 56, 1, 2, 2, 1)
)
alcatelIND1LBDMIBCompliance.setObjects(
      *(("ALCATEL-IND1-LBD-MIB", "alaLbdGlobalConfigGroup"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdIntfConfigGroup"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdPortStatusGroup"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdStateTrapToShutdownGroup"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdStateTrapForClearViolationAllGroup"),
        ("ALCATEL-IND1-LBD-MIB", "alaLbdStateTrapForAutoRecoveryGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1LBDMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-LBD-MIB",
    **{"AlaLbdPortConfigLbdOperStatus": AlaLbdPortConfigLbdOperStatus,
       "AlaLbdCurrentStateCVAorAR": AlaLbdCurrentStateCVAorAR,
       "alcatelIND1LBDMIB": alcatelIND1LBDMIB,
       "alcatelIND1LBDMIBObjects": alcatelIND1LBDMIBObjects,
       "alaLbdGlobalConfigStatus": alaLbdGlobalConfigStatus,
       "alaLbdGlobalConfigTransmissionTimer": alaLbdGlobalConfigTransmissionTimer,
       "alaLbdGlobalClearPortStat": alaLbdGlobalClearPortStat,
       "alaLbdGlobalConfigAutorecoveryTimer": alaLbdGlobalConfigAutorecoveryTimer,
       "alaLbdPortConfig": alaLbdPortConfig,
       "alaLbdPortConfigTable": alaLbdPortConfigTable,
       "alaLbdPortConfigEntry": alaLbdPortConfigEntry,
       "alaLbdPortConfigIfIndex": alaLbdPortConfigIfIndex,
       "alaLbdPortConfigLbdAdminStatus": alaLbdPortConfigLbdAdminStatus,
       "alaLbdPortConfigLbdOperStatus": alaLbdPortConfigLbdOperStatus,
       "alaLbdPortStat": alaLbdPortStat,
       "alaLbdPortStatsTable": alaLbdPortStatsTable,
       "alaLbdPortStatsEntry": alaLbdPortStatsEntry,
       "alaLbdPortStatsIfIndex": alaLbdPortStatsIfIndex,
       "alaLbdPortNumLbdInvalidRcvd": alaLbdPortNumLbdInvalidRcvd,
       "alaLbdPortLbdSent": alaLbdPortLbdSent,
       "alaLbdPortStatsClear": alaLbdPortStatsClear,
       "alcatelIND1LBDMIBConformance": alcatelIND1LBDMIBConformance,
       "alcatelIND1LBDMIBGroups": alcatelIND1LBDMIBGroups,
       "alaLbdGlobalConfigGroup": alaLbdGlobalConfigGroup,
       "alaLbdIntfConfigGroup": alaLbdIntfConfigGroup,
       "alaLbdPortStatusGroup": alaLbdPortStatusGroup,
       "alaLbdStateTrapToShutdownGroup": alaLbdStateTrapToShutdownGroup,
       "alaLbdStateTrapForClearViolationAllGroup": alaLbdStateTrapForClearViolationAllGroup,
       "alaLbdStateTrapForAutoRecoveryGroup": alaLbdStateTrapForAutoRecoveryGroup,
       "alcatelIND1LBDMIBCompliances": alcatelIND1LBDMIBCompliances,
       "alcatelIND1LBDMIBCompliance": alcatelIND1LBDMIBCompliance,
       "alaLbdTrapsDesc": alaLbdTrapsDesc,
       "alaLbdTrapsRoot": alaLbdTrapsRoot,
       "alaLbdStateChangeToShutdown": alaLbdStateChangeToShutdown,
       "alaLbdStateChangeForClearViolationAll": alaLbdStateChangeForClearViolationAll,
       "alaLbdStateChangeForAutoRecovery": alaLbdStateChangeForAutoRecovery,
       "alaLbdTrapsObj": alaLbdTrapsObj,
       "alaLbdPortIfIndex": alaLbdPortIfIndex,
       "alaLbdPreviousState": alaLbdPreviousState,
       "alaLbdCurrentState": alaLbdCurrentState,
       "alaLbdPreviousStateClearViolationAll": alaLbdPreviousStateClearViolationAll,
       "alaLbdCurrentStateClearViolationAll": alaLbdCurrentStateClearViolationAll,
       "alaLbdPreviousStateAutoRecovery": alaLbdPreviousStateAutoRecovery,
       "alaLbdCurrentStateAutoRecovery": alaLbdCurrentStateAutoRecovery}
)
