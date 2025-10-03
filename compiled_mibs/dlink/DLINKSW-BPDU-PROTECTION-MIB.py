# SNMP MIB module (DLINKSW-BPDU-PROTECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-BPDU-PROTECTION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:42 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwBpduProtectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 47)
)
if mibBuilder.loadTexts:
    dlinkSwBpduProtectionMIB.setRevisions(
        ("2013-02-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DBpduProtectionNotifications_ObjectIdentity = ObjectIdentity
dBpduProtectionNotifications = _DBpduProtectionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 0)
)
_DBpduProtectionObjects_ObjectIdentity = ObjectIdentity
dBpduProtectionObjects = _DBpduProtectionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 1)
)
_DBpduProtectionGlobalEnabled_Type = TruthValue
_DBpduProtectionGlobalEnabled_Object = MibScalar
dBpduProtectionGlobalEnabled = _DBpduProtectionGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 1),
    _DBpduProtectionGlobalEnabled_Type()
)
dBpduProtectionGlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBpduProtectionGlobalEnabled.setStatus("current")
_DBpduProtectionNotifyEnabled_Type = TruthValue
_DBpduProtectionNotifyEnabled_Object = MibScalar
dBpduProtectionNotifyEnabled = _DBpduProtectionNotifyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 2),
    _DBpduProtectionNotifyEnabled_Type()
)
dBpduProtectionNotifyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBpduProtectionNotifyEnabled.setStatus("current")
_DBpduProtectionIfTable_Object = MibTable
dBpduProtectionIfTable = _DBpduProtectionIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 3)
)
if mibBuilder.loadTexts:
    dBpduProtectionIfTable.setStatus("current")
_DBpduProtectionIfEntry_Object = MibTableRow
dBpduProtectionIfEntry = _DBpduProtectionIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 3, 1)
)
dBpduProtectionIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dBpduProtectionIfEntry.setStatus("current")


class _DBpduProtectionIfCfgMode_Type(Integer32):
    """Custom type dBpduProtectionIfCfgMode based on Integer32"""
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
        *(("disabled", 1),
          ("drop", 2),
          ("block", 3),
          ("shutdown", 4))
    )


_DBpduProtectionIfCfgMode_Type.__name__ = "Integer32"
_DBpduProtectionIfCfgMode_Object = MibTableColumn
dBpduProtectionIfCfgMode = _DBpduProtectionIfCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 3, 1, 1),
    _DBpduProtectionIfCfgMode_Type()
)
dBpduProtectionIfCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBpduProtectionIfCfgMode.setStatus("current")


class _DBpduProtectionIfAttackStatus_Type(Integer32):
    """Custom type dBpduProtectionIfAttackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("underAttack", 2))
    )


_DBpduProtectionIfAttackStatus_Type.__name__ = "Integer32"
_DBpduProtectionIfAttackStatus_Object = MibTableColumn
dBpduProtectionIfAttackStatus = _DBpduProtectionIfAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 1, 3, 1, 2),
    _DBpduProtectionIfAttackStatus_Type()
)
dBpduProtectionIfAttackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dBpduProtectionIfAttackStatus.setStatus("current")
_DBpduProtectionConformance_ObjectIdentity = ObjectIdentity
dBpduProtectionConformance = _DBpduProtectionConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 2)
)
_DBpduProtectionMIBCompliances_ObjectIdentity = ObjectIdentity
dBpduProtectionMIBCompliances = _DBpduProtectionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 1)
)
_DBpduProtectionMIBGroups_ObjectIdentity = ObjectIdentity
dBpduProtectionMIBGroups = _DBpduProtectionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 2)
)

# Managed Objects groups

dBpduProtectionCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 2, 1)
)
dBpduProtectionCfgGroup.setObjects(
      *(("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionGlobalEnabled"),
        ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionNotifyEnabled"))
)
if mibBuilder.loadTexts:
    dBpduProtectionCfgGroup.setStatus("current")

dBpduProtectionIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 2, 2)
)
dBpduProtectionIfGroup.setObjects(
      *(("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionIfCfgMode"),
        ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionIfAttackStatus"))
)
if mibBuilder.loadTexts:
    dBpduProtectionIfGroup.setStatus("current")


# Notification objects

dBpduProtectionAttackOccur = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 0, 1)
)
dBpduProtectionAttackOccur.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionIfCfgMode"))
)
if mibBuilder.loadTexts:
    dBpduProtectionAttackOccur.setStatus(
        "current"
    )

dBpduProtectionAttackRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 0, 2)
)
dBpduProtectionAttackRecover.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    dBpduProtectionAttackRecover.setStatus(
        "current"
    )


# Notifications groups

dBpduProtectionNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 2, 3)
)
dBpduProtectionNotifyGroup.setObjects(
      *(("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionAttackOccur"),
        ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionAttackRecover"))
)
if mibBuilder.loadTexts:
    dBpduProtectionNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dBpduProtectionMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 47, 2, 1, 1)
)
dBpduProtectionMIBCompliance.setObjects(
      *(("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionCfgGroup"),
        ("DLINKSW-BPDU-PROTECTION-MIB", "dBpduProtectionIfGroup"))
)
if mibBuilder.loadTexts:
    dBpduProtectionMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-BPDU-PROTECTION-MIB",
    **{"dlinkSwBpduProtectionMIB": dlinkSwBpduProtectionMIB,
       "dBpduProtectionNotifications": dBpduProtectionNotifications,
       "dBpduProtectionAttackOccur": dBpduProtectionAttackOccur,
       "dBpduProtectionAttackRecover": dBpduProtectionAttackRecover,
       "dBpduProtectionObjects": dBpduProtectionObjects,
       "dBpduProtectionGlobalEnabled": dBpduProtectionGlobalEnabled,
       "dBpduProtectionNotifyEnabled": dBpduProtectionNotifyEnabled,
       "dBpduProtectionIfTable": dBpduProtectionIfTable,
       "dBpduProtectionIfEntry": dBpduProtectionIfEntry,
       "dBpduProtectionIfCfgMode": dBpduProtectionIfCfgMode,
       "dBpduProtectionIfAttackStatus": dBpduProtectionIfAttackStatus,
       "dBpduProtectionConformance": dBpduProtectionConformance,
       "dBpduProtectionMIBCompliances": dBpduProtectionMIBCompliances,
       "dBpduProtectionMIBCompliance": dBpduProtectionMIBCompliance,
       "dBpduProtectionMIBGroups": dBpduProtectionMIBGroups,
       "dBpduProtectionCfgGroup": dBpduProtectionCfgGroup,
       "dBpduProtectionIfGroup": dBpduProtectionIfGroup,
       "dBpduProtectionNotifyGroup": dBpduProtectionNotifyGroup}
)
