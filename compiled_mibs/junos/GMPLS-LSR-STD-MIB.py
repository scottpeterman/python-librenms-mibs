# SNMP MIB module (GMPLS-LSR-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\GMPLS-LSR-STD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:02:32 2025
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

(GmplsSegmentDirectionTC,) = mibBuilder.importSymbols(
    "GMPLS-TC-STD-MIB",
    "GmplsSegmentDirectionTC")

(ifCounterDiscontinuityGroup,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifCounterDiscontinuityGroup",
    "ifGeneralInformationGroup")

(mplsInSegmentGroup,
 mplsInSegmentIndex,
 mplsInterfaceGroup,
 mplsInterfaceIndex,
 mplsLsrNotificationGroup,
 mplsOutSegmentGroup,
 mplsOutSegmentIndex,
 mplsPerfGroup,
 mplsXCGroup) = mibBuilder.importSymbols(
    "MPLS-LSR-STD-MIB",
    "mplsInSegmentGroup",
    "mplsInSegmentIndex",
    "mplsInterfaceGroup",
    "mplsInterfaceIndex",
    "mplsLsrNotificationGroup",
    "mplsOutSegmentGroup",
    "mplsOutSegmentIndex",
    "mplsPerfGroup",
    "mplsXCGroup")

(mplsStdMIB,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "mplsStdMIB")

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
 zeroDotZero) = mibBuilder.importSymbols(
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
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

gmplsLsrStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 15)
)
if mibBuilder.loadTexts:
    gmplsLsrStdMIB.setRevisions(
        ("2007-02-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GmplsLsrObjects_ObjectIdentity = ObjectIdentity
gmplsLsrObjects = _GmplsLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1)
)
_GmplsInterfaceTable_Object = MibTable
gmplsInterfaceTable = _GmplsInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 1)
)
if mibBuilder.loadTexts:
    gmplsInterfaceTable.setStatus("current")
_GmplsInterfaceEntry_Object = MibTableRow
gmplsInterfaceEntry = _GmplsInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 1, 1)
)
gmplsInterfaceEntry.setIndexNames(
    (0, "MPLS-LSR-STD-MIB", "mplsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    gmplsInterfaceEntry.setStatus("current")


class _GmplsInterfaceSignalingCaps_Type(Bits):
    """Custom type gmplsInterfaceSignalingCaps based on Bits"""
    defaultBinValue = "01"

    namedValues = NamedValues(
        *(("unknown", 0),
          ("rsvpGmpls", 1),
          ("crldpGmpls", 2),
          ("otherGmpls", 3))
    )

_GmplsInterfaceSignalingCaps_Type.__name__ = "Bits"
_GmplsInterfaceSignalingCaps_Object = MibTableColumn
gmplsInterfaceSignalingCaps = _GmplsInterfaceSignalingCaps_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 1, 1, 1),
    _GmplsInterfaceSignalingCaps_Type()
)
gmplsInterfaceSignalingCaps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsInterfaceSignalingCaps.setStatus("current")


class _GmplsInterfaceRsvpHelloPeriod_Type(Unsigned32):
    """Custom type gmplsInterfaceRsvpHelloPeriod based on Unsigned32"""
    defaultValue = 3000


_GmplsInterfaceRsvpHelloPeriod_Type.__name__ = "Unsigned32"
_GmplsInterfaceRsvpHelloPeriod_Object = MibTableColumn
gmplsInterfaceRsvpHelloPeriod = _GmplsInterfaceRsvpHelloPeriod_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 1, 1, 2),
    _GmplsInterfaceRsvpHelloPeriod_Type()
)
gmplsInterfaceRsvpHelloPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsInterfaceRsvpHelloPeriod.setStatus("current")
if mibBuilder.loadTexts:
    gmplsInterfaceRsvpHelloPeriod.setUnits("milliseconds")
_GmplsInSegmentTable_Object = MibTable
gmplsInSegmentTable = _GmplsInSegmentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 2)
)
if mibBuilder.loadTexts:
    gmplsInSegmentTable.setStatus("current")
_GmplsInSegmentEntry_Object = MibTableRow
gmplsInSegmentEntry = _GmplsInSegmentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 2, 1)
)
gmplsInSegmentEntry.setIndexNames(
    (0, "MPLS-LSR-STD-MIB", "mplsInSegmentIndex"),
)
if mibBuilder.loadTexts:
    gmplsInSegmentEntry.setStatus("current")


class _GmplsInSegmentDirection_Type(GmplsSegmentDirectionTC):
    """Custom type gmplsInSegmentDirection based on GmplsSegmentDirectionTC"""
    defaultValue = 1


_GmplsInSegmentDirection_Type.__name__ = "GmplsSegmentDirectionTC"
_GmplsInSegmentDirection_Object = MibTableColumn
gmplsInSegmentDirection = _GmplsInSegmentDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 2, 1, 1),
    _GmplsInSegmentDirection_Type()
)
gmplsInSegmentDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsInSegmentDirection.setStatus("current")


class _GmplsInSegmentExtraParamsPtr_Type(RowPointer):
    """Custom type gmplsInSegmentExtraParamsPtr based on RowPointer"""
    defaultValue = (0, 0)


_GmplsInSegmentExtraParamsPtr_Type.__name__ = "RowPointer"
_GmplsInSegmentExtraParamsPtr_Object = MibTableColumn
gmplsInSegmentExtraParamsPtr = _GmplsInSegmentExtraParamsPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 2, 1, 2),
    _GmplsInSegmentExtraParamsPtr_Type()
)
gmplsInSegmentExtraParamsPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsInSegmentExtraParamsPtr.setStatus("current")
_GmplsOutSegmentTable_Object = MibTable
gmplsOutSegmentTable = _GmplsOutSegmentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3)
)
if mibBuilder.loadTexts:
    gmplsOutSegmentTable.setStatus("current")
_GmplsOutSegmentEntry_Object = MibTableRow
gmplsOutSegmentEntry = _GmplsOutSegmentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3, 1)
)
gmplsOutSegmentEntry.setIndexNames(
    (0, "MPLS-LSR-STD-MIB", "mplsOutSegmentIndex"),
)
if mibBuilder.loadTexts:
    gmplsOutSegmentEntry.setStatus("current")


class _GmplsOutSegmentDirection_Type(GmplsSegmentDirectionTC):
    """Custom type gmplsOutSegmentDirection based on GmplsSegmentDirectionTC"""
    defaultValue = 1


_GmplsOutSegmentDirection_Type.__name__ = "GmplsSegmentDirectionTC"
_GmplsOutSegmentDirection_Object = MibTableColumn
gmplsOutSegmentDirection = _GmplsOutSegmentDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3, 1, 1),
    _GmplsOutSegmentDirection_Type()
)
gmplsOutSegmentDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsOutSegmentDirection.setStatus("current")


class _GmplsOutSegmentTTLDecrement_Type(Unsigned32):
    """Custom type gmplsOutSegmentTTLDecrement based on Unsigned32"""
    defaultValue = 0


_GmplsOutSegmentTTLDecrement_Type.__name__ = "Unsigned32"
_GmplsOutSegmentTTLDecrement_Object = MibTableColumn
gmplsOutSegmentTTLDecrement = _GmplsOutSegmentTTLDecrement_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3, 1, 2),
    _GmplsOutSegmentTTLDecrement_Type()
)
gmplsOutSegmentTTLDecrement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsOutSegmentTTLDecrement.setStatus("current")


class _GmplsOutSegmentExtraParamsPtr_Type(RowPointer):
    """Custom type gmplsOutSegmentExtraParamsPtr based on RowPointer"""
    defaultValue = (0, 0)


_GmplsOutSegmentExtraParamsPtr_Type.__name__ = "RowPointer"
_GmplsOutSegmentExtraParamsPtr_Object = MibTableColumn
gmplsOutSegmentExtraParamsPtr = _GmplsOutSegmentExtraParamsPtr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 1, 3, 1, 3),
    _GmplsOutSegmentExtraParamsPtr_Type()
)
gmplsOutSegmentExtraParamsPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsOutSegmentExtraParamsPtr.setStatus("current")
_GmplsLsrConformance_ObjectIdentity = ObjectIdentity
gmplsLsrConformance = _GmplsLsrConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 2)
)
_GmplsLsrGroups_ObjectIdentity = ObjectIdentity
gmplsLsrGroups = _GmplsLsrGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 1)
)
_GmplsLsrCompliances_ObjectIdentity = ObjectIdentity
gmplsLsrCompliances = _GmplsLsrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 2)
)

# Managed Objects groups

gmplsInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 1, 1)
)
gmplsInterfaceGroup.setObjects(
      *(("GMPLS-LSR-STD-MIB", "gmplsInterfaceSignalingCaps"),
        ("GMPLS-LSR-STD-MIB", "gmplsInterfaceRsvpHelloPeriod"))
)
if mibBuilder.loadTexts:
    gmplsInterfaceGroup.setStatus("current")

gmplsInSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 1, 2)
)
gmplsInSegmentGroup.setObjects(
      *(("GMPLS-LSR-STD-MIB", "gmplsInSegmentDirection"),
        ("GMPLS-LSR-STD-MIB", "gmplsInSegmentExtraParamsPtr"))
)
if mibBuilder.loadTexts:
    gmplsInSegmentGroup.setStatus("current")

gmplsOutSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 1, 3)
)
gmplsOutSegmentGroup.setObjects(
      *(("GMPLS-LSR-STD-MIB", "gmplsOutSegmentDirection"),
        ("GMPLS-LSR-STD-MIB", "gmplsOutSegmentTTLDecrement"),
        ("GMPLS-LSR-STD-MIB", "gmplsOutSegmentExtraParamsPtr"))
)
if mibBuilder.loadTexts:
    gmplsOutSegmentGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gmplsLsrModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 2, 1)
)
gmplsLsrModuleFullCompliance.setObjects(
      *(("IF-MIB", "ifGeneralInformationGroup"),
        ("IF-MIB", "ifCounterDiscontinuityGroup"),
        ("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"),
        ("MPLS-LSR-STD-MIB", "mplsXCGroup"),
        ("MPLS-LSR-STD-MIB", "mplsPerfGroup"),
        ("MPLS-LSR-STD-MIB", "mplsLsrNotificationGroup"),
        ("GMPLS-LSR-STD-MIB", "gmplsInterfaceGroup"),
        ("GMPLS-LSR-STD-MIB", "gmplsInSegmentGroup"),
        ("GMPLS-LSR-STD-MIB", "gmplsOutSegmentGroup"))
)
if mibBuilder.loadTexts:
    gmplsLsrModuleFullCompliance.setStatus(
        "current"
    )

gmplsLsrModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 15, 2, 2, 2)
)
gmplsLsrModuleReadOnlyCompliance.setObjects(
      *(("IF-MIB", "ifGeneralInformationGroup"),
        ("IF-MIB", "ifCounterDiscontinuityGroup"),
        ("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"),
        ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"),
        ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"),
        ("MPLS-LSR-STD-MIB", "mplsXCGroup"),
        ("MPLS-LSR-STD-MIB", "mplsPerfGroup"),
        ("GMPLS-LSR-STD-MIB", "gmplsInterfaceGroup"),
        ("GMPLS-LSR-STD-MIB", "gmplsInSegmentGroup"),
        ("GMPLS-LSR-STD-MIB", "gmplsOutSegmentGroup"))
)
if mibBuilder.loadTexts:
    gmplsLsrModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GMPLS-LSR-STD-MIB",
    **{"gmplsLsrStdMIB": gmplsLsrStdMIB,
       "gmplsLsrObjects": gmplsLsrObjects,
       "gmplsInterfaceTable": gmplsInterfaceTable,
       "gmplsInterfaceEntry": gmplsInterfaceEntry,
       "gmplsInterfaceSignalingCaps": gmplsInterfaceSignalingCaps,
       "gmplsInterfaceRsvpHelloPeriod": gmplsInterfaceRsvpHelloPeriod,
       "gmplsInSegmentTable": gmplsInSegmentTable,
       "gmplsInSegmentEntry": gmplsInSegmentEntry,
       "gmplsInSegmentDirection": gmplsInSegmentDirection,
       "gmplsInSegmentExtraParamsPtr": gmplsInSegmentExtraParamsPtr,
       "gmplsOutSegmentTable": gmplsOutSegmentTable,
       "gmplsOutSegmentEntry": gmplsOutSegmentEntry,
       "gmplsOutSegmentDirection": gmplsOutSegmentDirection,
       "gmplsOutSegmentTTLDecrement": gmplsOutSegmentTTLDecrement,
       "gmplsOutSegmentExtraParamsPtr": gmplsOutSegmentExtraParamsPtr,
       "gmplsLsrConformance": gmplsLsrConformance,
       "gmplsLsrGroups": gmplsLsrGroups,
       "gmplsInterfaceGroup": gmplsInterfaceGroup,
       "gmplsInSegmentGroup": gmplsInSegmentGroup,
       "gmplsOutSegmentGroup": gmplsOutSegmentGroup,
       "gmplsLsrCompliances": gmplsLsrCompliances,
       "gmplsLsrModuleFullCompliance": gmplsLsrModuleFullCompliance,
       "gmplsLsrModuleReadOnlyCompliance": gmplsLsrModuleReadOnlyCompliance}
)
