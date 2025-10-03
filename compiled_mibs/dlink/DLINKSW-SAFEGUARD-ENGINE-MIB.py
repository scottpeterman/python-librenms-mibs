# SNMP MIB module (DLINKSW-SAFEGUARD-ENGINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-SAFEGUARD-ENGINE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:49 2025
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

(dCpuProtectMIBObjects,) = mibBuilder.importSymbols(
    "DLINKSW-CPU-PROTECT-MIB",
    "dCpuProtectMIBObjects")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwSafeguardEngineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1)
)
if mibBuilder.loadTexts:
    dlinkSwSafeguardEngineMIB.setRevisions(
        ("2012-06-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DSafeguardEngineMIBNotif_ObjectIdentity = ObjectIdentity
dSafeguardEngineMIBNotif = _DSafeguardEngineMIBNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 0)
)
_DSafeguardEngineMIBObjects_ObjectIdentity = ObjectIdentity
dSafeguardEngineMIBObjects = _DSafeguardEngineMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1)
)


class _DSafeguardEngineState_Type(Integer32):
    """Custom type dSafeguardEngineState based on Integer32"""
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


_DSafeguardEngineState_Type.__name__ = "Integer32"
_DSafeguardEngineState_Object = MibScalar
dSafeguardEngineState = _DSafeguardEngineState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 1),
    _DSafeguardEngineState_Type()
)
dSafeguardEngineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSafeguardEngineState.setStatus("current")


class _DSafeguardEngineRiseThresh_Type(Integer32):
    """Custom type dSafeguardEngineRiseThresh based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_DSafeguardEngineRiseThresh_Type.__name__ = "Integer32"
_DSafeguardEngineRiseThresh_Object = MibScalar
dSafeguardEngineRiseThresh = _DSafeguardEngineRiseThresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 2),
    _DSafeguardEngineRiseThresh_Type()
)
dSafeguardEngineRiseThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSafeguardEngineRiseThresh.setStatus("current")
if mibBuilder.loadTexts:
    dSafeguardEngineRiseThresh.setUnits("%")


class _DSafeguardEngineFallThresh_Type(Integer32):
    """Custom type dSafeguardEngineFallThresh based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_DSafeguardEngineFallThresh_Type.__name__ = "Integer32"
_DSafeguardEngineFallThresh_Object = MibScalar
dSafeguardEngineFallThresh = _DSafeguardEngineFallThresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 3),
    _DSafeguardEngineFallThresh_Type()
)
dSafeguardEngineFallThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSafeguardEngineFallThresh.setStatus("current")
if mibBuilder.loadTexts:
    dSafeguardEngineFallThresh.setUnits("%")


class _DSafeguardEngineCurrentMode_Type(Integer32):
    """Custom type dSafeguardEngineCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("exhausted", 2))
    )


_DSafeguardEngineCurrentMode_Type.__name__ = "Integer32"
_DSafeguardEngineCurrentMode_Object = MibScalar
dSafeguardEngineCurrentMode = _DSafeguardEngineCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 4),
    _DSafeguardEngineCurrentMode_Type()
)
dSafeguardEngineCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSafeguardEngineCurrentMode.setStatus("current")


class _DSafeguardEngineNotifEnable_Type(TruthValue):
    """Custom type dSafeguardEngineNotifEnable based on TruthValue"""
    defaultValue = 2


_DSafeguardEngineNotifEnable_Type.__name__ = "TruthValue"
_DSafeguardEngineNotifEnable_Object = MibScalar
dSafeguardEngineNotifEnable = _DSafeguardEngineNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 5),
    _DSafeguardEngineNotifEnable_Type()
)
dSafeguardEngineNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSafeguardEngineNotifEnable.setStatus("current")
_DSafeguardEngineMIBConformance_ObjectIdentity = ObjectIdentity
dSafeguardEngineMIBConformance = _DSafeguardEngineMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2)
)
_DSafeguardEngineCompliances_ObjectIdentity = ObjectIdentity
dSafeguardEngineCompliances = _DSafeguardEngineCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 1)
)
_DSafeguardEngineGroups_ObjectIdentity = ObjectIdentity
dSafeguardEngineGroups = _DSafeguardEngineGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2)
)

# Managed Objects groups

dSafeguardEngineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2, 1)
)
dSafeguardEngineGroup.setObjects(
      *(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineState"),
        ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineRiseThresh"),
        ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineFallThresh"),
        ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineCurrentMode"))
)
if mibBuilder.loadTexts:
    dSafeguardEngineGroup.setStatus("current")

dSafeguardEngNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2, 2)
)
dSafeguardEngNotifEnableGroup.setObjects(
    ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineNotifEnable")
)
if mibBuilder.loadTexts:
    dSafeguardEngNotifEnableGroup.setStatus("current")


# Notification objects

dSafeguardChgToExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 0, 1)
)
dSafeguardChgToExhausted.setObjects(
    ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineCurrentMode")
)
if mibBuilder.loadTexts:
    dSafeguardChgToExhausted.setStatus(
        "current"
    )

dSafeguardChgToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 0, 2)
)
dSafeguardChgToNormal.setObjects(
    ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineCurrentMode")
)
if mibBuilder.loadTexts:
    dSafeguardChgToNormal.setStatus(
        "current"
    )


# Notifications groups

dSafeguardEngineNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2, 3)
)
dSafeguardEngineNotifGroup.setObjects(
      *(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardChgToExhausted"),
        ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardChgToNormal"))
)
if mibBuilder.loadTexts:
    dSafeguardEngineNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dSafeguardEngineCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 1, 1)
)
dSafeguardEngineCompliance.setObjects(
      *(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineGroup"),
        ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngNotifEnableGroup"),
        ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineNotifGroup"))
)
if mibBuilder.loadTexts:
    dSafeguardEngineCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-SAFEGUARD-ENGINE-MIB",
    **{"dlinkSwSafeguardEngineMIB": dlinkSwSafeguardEngineMIB,
       "dSafeguardEngineMIBNotif": dSafeguardEngineMIBNotif,
       "dSafeguardChgToExhausted": dSafeguardChgToExhausted,
       "dSafeguardChgToNormal": dSafeguardChgToNormal,
       "dSafeguardEngineMIBObjects": dSafeguardEngineMIBObjects,
       "dSafeguardEngineState": dSafeguardEngineState,
       "dSafeguardEngineRiseThresh": dSafeguardEngineRiseThresh,
       "dSafeguardEngineFallThresh": dSafeguardEngineFallThresh,
       "dSafeguardEngineCurrentMode": dSafeguardEngineCurrentMode,
       "dSafeguardEngineNotifEnable": dSafeguardEngineNotifEnable,
       "dSafeguardEngineMIBConformance": dSafeguardEngineMIBConformance,
       "dSafeguardEngineCompliances": dSafeguardEngineCompliances,
       "dSafeguardEngineCompliance": dSafeguardEngineCompliance,
       "dSafeguardEngineGroups": dSafeguardEngineGroups,
       "dSafeguardEngineGroup": dSafeguardEngineGroup,
       "dSafeguardEngNotifEnableGroup": dSafeguardEngNotifEnableGroup,
       "dSafeguardEngineNotifGroup": dSafeguardEngineNotifGroup}
)
