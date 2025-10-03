# SNMP MIB module (WESTERMO-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\westermo\WESTERMO-INTERFACE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:04 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

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

(common,) = mibBuilder.importSymbols(
    "WESTERMO-OID-MIB",
    "common")


# MODULE-IDENTITY

wmoInterface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4)
)
if mibBuilder.loadTexts:
    wmoInterface.setRevisions(
        ("2019-08-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IfaceRefIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )



# MIB Managed Objects in the order of their OIDs

_WmoInterfaceObjects_ObjectIdentity = ObjectIdentity
wmoInterfaceObjects = _WmoInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4, 1)
)
_IfRefTable_Object = MibTable
ifRefTable = _IfRefTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ifRefTable.setStatus("current")
_IfRefEntry_Object = MibTableRow
ifRefEntry = _IfRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1, 1)
)
ifRefEntry.setIndexNames(
    (0, "WESTERMO-INTERFACE-MIB", "ifRefIndex"),
)
if mibBuilder.loadTexts:
    ifRefEntry.setStatus("current")
_IfRefIndex_Type = IfaceRefIndex
_IfRefIndex_Object = MibTableColumn
ifRefIndex = _IfRefIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1, 1, 1),
    _IfRefIndex_Type()
)
ifRefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifRefIndex.setStatus("current")
_IfRefifIndex_Type = InterfaceIndex
_IfRefifIndex_Object = MibTableColumn
ifRefifIndex = _IfRefifIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1, 1, 2),
    _IfRefifIndex_Type()
)
ifRefifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRefifIndex.setStatus("current")


class _IfRefifName_Type(DisplayString):
    """Custom type ifRefifName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfRefifName_Type.__name__ = "DisplayString"
_IfRefifName_Object = MibTableColumn
ifRefifName = _IfRefifName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1, 1, 3),
    _IfRefifName_Type()
)
ifRefifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRefifName.setStatus("current")


class _IfRefifDescr_Type(DisplayString):
    """Custom type ifRefifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfRefifDescr_Type.__name__ = "DisplayString"
_IfRefifDescr_Object = MibTableColumn
ifRefifDescr = _IfRefifDescr_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1, 1, 4),
    _IfRefifDescr_Type()
)
ifRefifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRefifDescr.setStatus("current")
_IfRefifType_Type = IANAifType
_IfRefifType_Object = MibTableColumn
ifRefifType = _IfRefifType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4, 1, 1, 1, 5),
    _IfRefifType_Type()
)
ifRefifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRefifType.setStatus("current")
_WmoInterfaceConformance_ObjectIdentity = ObjectIdentity
wmoInterfaceConformance = _WmoInterfaceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4, 2)
)
_WmoInterfaceGroups_ObjectIdentity = ObjectIdentity
wmoInterfaceGroups = _WmoInterfaceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4, 2, 1)
)
_WmoInterfaceCompliances_ObjectIdentity = ObjectIdentity
wmoInterfaceCompliances = _WmoInterfaceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4, 2, 2)
)

# Managed Objects groups

wmoInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4, 2, 1, 1)
)
wmoInterfaceGroup.setObjects(
      *(("WESTERMO-INTERFACE-MIB", "ifRefifIndex"),
        ("WESTERMO-INTERFACE-MIB", "ifRefifName"),
        ("WESTERMO-INTERFACE-MIB", "ifRefifDescr"),
        ("WESTERMO-INTERFACE-MIB", "ifRefifType"))
)
if mibBuilder.loadTexts:
    wmoInterfaceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wmoInterfaceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 16177, 2, 4, 2, 2, 1)
)
wmoInterfaceCompliance.setObjects(
    ("WESTERMO-INTERFACE-MIB", "wmoInterfaceGroup")
)
if mibBuilder.loadTexts:
    wmoInterfaceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-INTERFACE-MIB",
    **{"IfaceRefIndex": IfaceRefIndex,
       "wmoInterface": wmoInterface,
       "wmoInterfaceObjects": wmoInterfaceObjects,
       "ifRefTable": ifRefTable,
       "ifRefEntry": ifRefEntry,
       "ifRefIndex": ifRefIndex,
       "ifRefifIndex": ifRefifIndex,
       "ifRefifName": ifRefifName,
       "ifRefifDescr": ifRefifDescr,
       "ifRefifType": ifRefifType,
       "wmoInterfaceConformance": wmoInterfaceConformance,
       "wmoInterfaceGroups": wmoInterfaceGroups,
       "wmoInterfaceGroup": wmoInterfaceGroup,
       "wmoInterfaceCompliances": wmoInterfaceCompliances,
       "wmoInterfaceCompliance": wmoInterfaceCompliance}
)
