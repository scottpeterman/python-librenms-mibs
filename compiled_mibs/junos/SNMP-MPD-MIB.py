# SNMP MIB module (SNMP-MPD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\SNMP-MPD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:05:23 2025
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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

snmpMPDMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 11)
)
if mibBuilder.loadTexts:
    snmpMPDMIB.setRevisions(
        ("2002-10-14 00:00",
         "1999-05-04 16:36",
         "1997-09-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpMPDAdmin_ObjectIdentity = ObjectIdentity
snmpMPDAdmin = _SnmpMPDAdmin_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 1)
)
_SnmpMPDMIBObjects_ObjectIdentity = ObjectIdentity
snmpMPDMIBObjects = _SnmpMPDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 2)
)
_SnmpMPDStats_ObjectIdentity = ObjectIdentity
snmpMPDStats = _SnmpMPDStats_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 2, 1)
)
_SnmpUnknownSecurityModels_Type = Counter32
_SnmpUnknownSecurityModels_Object = MibScalar
snmpUnknownSecurityModels = _SnmpUnknownSecurityModels_Object(
    (1, 3, 6, 1, 6, 3, 11, 2, 1, 1),
    _SnmpUnknownSecurityModels_Type()
)
snmpUnknownSecurityModels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUnknownSecurityModels.setStatus("current")
_SnmpInvalidMsgs_Type = Counter32
_SnmpInvalidMsgs_Object = MibScalar
snmpInvalidMsgs = _SnmpInvalidMsgs_Object(
    (1, 3, 6, 1, 6, 3, 11, 2, 1, 2),
    _SnmpInvalidMsgs_Type()
)
snmpInvalidMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInvalidMsgs.setStatus("current")
_SnmpUnknownPDUHandlers_Type = Counter32
_SnmpUnknownPDUHandlers_Object = MibScalar
snmpUnknownPDUHandlers = _SnmpUnknownPDUHandlers_Object(
    (1, 3, 6, 1, 6, 3, 11, 2, 1, 3),
    _SnmpUnknownPDUHandlers_Type()
)
snmpUnknownPDUHandlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUnknownPDUHandlers.setStatus("current")
_SnmpMPDMIBConformance_ObjectIdentity = ObjectIdentity
snmpMPDMIBConformance = _SnmpMPDMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 3)
)
_SnmpMPDMIBCompliances_ObjectIdentity = ObjectIdentity
snmpMPDMIBCompliances = _SnmpMPDMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 3, 1)
)
_SnmpMPDMIBGroups_ObjectIdentity = ObjectIdentity
snmpMPDMIBGroups = _SnmpMPDMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 11, 3, 2)
)

# Managed Objects groups

snmpMPDGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 11, 3, 2, 1)
)
snmpMPDGroup.setObjects(
      *(("SNMP-MPD-MIB", "snmpUnknownSecurityModels"),
        ("SNMP-MPD-MIB", "snmpInvalidMsgs"),
        ("SNMP-MPD-MIB", "snmpUnknownPDUHandlers"))
)
if mibBuilder.loadTexts:
    snmpMPDGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

snmpMPDCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 11, 3, 1, 1)
)
snmpMPDCompliance.setObjects(
    ("SNMP-MPD-MIB", "snmpMPDGroup")
)
if mibBuilder.loadTexts:
    snmpMPDCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-MPD-MIB",
    **{"snmpMPDMIB": snmpMPDMIB,
       "snmpMPDAdmin": snmpMPDAdmin,
       "snmpMPDMIBObjects": snmpMPDMIBObjects,
       "snmpMPDStats": snmpMPDStats,
       "snmpUnknownSecurityModels": snmpUnknownSecurityModels,
       "snmpInvalidMsgs": snmpInvalidMsgs,
       "snmpUnknownPDUHandlers": snmpUnknownPDUHandlers,
       "snmpMPDMIBConformance": snmpMPDMIBConformance,
       "snmpMPDMIBCompliances": snmpMPDMIBCompliances,
       "snmpMPDCompliance": snmpMPDCompliance,
       "snmpMPDMIBGroups": snmpMPDMIBGroups,
       "snmpMPDGroup": snmpMPDGroup}
)
