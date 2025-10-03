# SNMP MIB module (ALCATEL-IND1-VIRTUALROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-VIRTUALROUTER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:24 2025
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

(routingIND1Vrf,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Vrf")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1VirtualRouterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VirtualRouterMIB.setRevisions(
        ("2008-03-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1VirtualRouterMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1VirtualRouterMIBObjects = _AlcatelIND1VirtualRouterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1)
)
_AlaVirtualRouterConfig_ObjectIdentity = ObjectIdentity
alaVirtualRouterConfig = _AlaVirtualRouterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1)
)
_AlaVirtualRouterNameTable_Object = MibTable
alaVirtualRouterNameTable = _AlaVirtualRouterNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaVirtualRouterNameTable.setStatus("current")
_AlaVirtualRouterNameEntry_Object = MibTableRow
alaVirtualRouterNameEntry = _AlaVirtualRouterNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1)
)
alaVirtualRouterNameEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterName"),
)
if mibBuilder.loadTexts:
    alaVirtualRouterNameEntry.setStatus("current")


class _AlaVirtualRouterName_Type(DisplayString):
    """Custom type alaVirtualRouterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AlaVirtualRouterName_Type.__name__ = "DisplayString"
_AlaVirtualRouterName_Object = MibTableColumn
alaVirtualRouterName = _AlaVirtualRouterName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 1),
    _AlaVirtualRouterName_Type()
)
alaVirtualRouterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVirtualRouterName.setStatus("current")
_AlaVirtualRouterNameIndex_Type = Unsigned32
_AlaVirtualRouterNameIndex_Object = MibTableColumn
alaVirtualRouterNameIndex = _AlaVirtualRouterNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 2),
    _AlaVirtualRouterNameIndex_Type()
)
alaVirtualRouterNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVirtualRouterNameIndex.setStatus("current")
_AlaVirtualRouterNameRowStatus_Type = RowStatus
_AlaVirtualRouterNameRowStatus_Object = MibTableColumn
alaVirtualRouterNameRowStatus = _AlaVirtualRouterNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 3),
    _AlaVirtualRouterNameRowStatus_Type()
)
alaVirtualRouterNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVirtualRouterNameRowStatus.setStatus("current")
_AlcatelIND1VirtualRouterMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1VirtualRouterMIBConformance = _AlcatelIND1VirtualRouterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2)
)
_AlcatelIND1VirtualRouterMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1VirtualRouterMIBCompliances = _AlcatelIND1VirtualRouterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 1)
)
_AlcatelIND1VirtualRouterMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1VirtualRouterMIBGroups = _AlcatelIND1VirtualRouterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 2)
)

# Managed Objects groups

alaVirtualRouterConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 2, 1)
)
alaVirtualRouterConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameIndex"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameRowStatus"))
)
if mibBuilder.loadTexts:
    alaVirtualRouterConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaVirtualRouterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 1, 1)
)
alaVirtualRouterCompliance.setObjects(
    ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterConfigMIBGroup")
)
if mibBuilder.loadTexts:
    alaVirtualRouterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-VIRTUALROUTER-MIB",
    **{"alcatelIND1VirtualRouterMIB": alcatelIND1VirtualRouterMIB,
       "alcatelIND1VirtualRouterMIBObjects": alcatelIND1VirtualRouterMIBObjects,
       "alaVirtualRouterConfig": alaVirtualRouterConfig,
       "alaVirtualRouterNameTable": alaVirtualRouterNameTable,
       "alaVirtualRouterNameEntry": alaVirtualRouterNameEntry,
       "alaVirtualRouterName": alaVirtualRouterName,
       "alaVirtualRouterNameIndex": alaVirtualRouterNameIndex,
       "alaVirtualRouterNameRowStatus": alaVirtualRouterNameRowStatus,
       "alcatelIND1VirtualRouterMIBConformance": alcatelIND1VirtualRouterMIBConformance,
       "alcatelIND1VirtualRouterMIBCompliances": alcatelIND1VirtualRouterMIBCompliances,
       "alaVirtualRouterCompliance": alaVirtualRouterCompliance,
       "alcatelIND1VirtualRouterMIBGroups": alcatelIND1VirtualRouterMIBGroups,
       "alaVirtualRouterConfigMIBGroup": alaVirtualRouterConfigMIBGroup}
)
