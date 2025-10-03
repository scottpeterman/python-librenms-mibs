# SNMP MIB module (ARRIS-C3-POST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\ARRIS-C3-POST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:05 2025
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

(cmtsC3,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "cmtsC3")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cmtsC3POSTMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcxPOSTObjects_ObjectIdentity = ObjectIdentity
dcxPOSTObjects = _DcxPOSTObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1)
)
_DcxCPUWANPOSTGroup_ObjectIdentity = ObjectIdentity
dcxCPUWANPOSTGroup = _DcxCPUWANPOSTGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 1)
)
_DcxCPUWANPOSTTable_Object = MibTable
dcxCPUWANPOSTTable = _DcxCPUWANPOSTTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dcxCPUWANPOSTTable.setStatus("current")
_DcxCPUWANPOSTEntry_Object = MibTableRow
dcxCPUWANPOSTEntry = _DcxCPUWANPOSTEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 1, 1, 1)
)
dcxCPUWANPOSTEntry.setIndexNames(
    (0, "ARRIS-C3-POST-MIB", "dcxCPUWANPOSTType"),
)
if mibBuilder.loadTexts:
    dcxCPUWANPOSTEntry.setStatus("current")


class _DcxCPUWANPOSTType_Type(Integer32):
    """Custom type dcxCPUWANPOSTType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DcxCPUWANPOSTType_Type.__name__ = "Integer32"
_DcxCPUWANPOSTType_Object = MibTableColumn
dcxCPUWANPOSTType = _DcxCPUWANPOSTType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 1, 1, 1, 1),
    _DcxCPUWANPOSTType_Type()
)
dcxCPUWANPOSTType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxCPUWANPOSTType.setStatus("current")


class _DcxCPUWANPOSTDescr_Type(DisplayString):
    """Custom type dcxCPUWANPOSTDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DcxCPUWANPOSTDescr_Type.__name__ = "DisplayString"
_DcxCPUWANPOSTDescr_Object = MibTableColumn
dcxCPUWANPOSTDescr = _DcxCPUWANPOSTDescr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 1, 1, 1, 2),
    _DcxCPUWANPOSTDescr_Type()
)
dcxCPUWANPOSTDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCPUWANPOSTDescr.setStatus("current")


class _DcxCPUWANPOSTResult_Type(Integer32):
    """Custom type dcxCPUWANPOSTResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passed", 0),
          ("skipped", 1),
          ("failed", 2))
    )


_DcxCPUWANPOSTResult_Type.__name__ = "Integer32"
_DcxCPUWANPOSTResult_Object = MibTableColumn
dcxCPUWANPOSTResult = _DcxCPUWANPOSTResult_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 1, 1, 1, 3),
    _DcxCPUWANPOSTResult_Type()
)
dcxCPUWANPOSTResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCPUWANPOSTResult.setStatus("current")
_Dcx3212POSTGroup_ObjectIdentity = ObjectIdentity
dcx3212POSTGroup = _Dcx3212POSTGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 2)
)
_Dcx3212POSTTable_Object = MibTable
dcx3212POSTTable = _Dcx3212POSTTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dcx3212POSTTable.setStatus("current")
_Dcx3212POSTEntry_Object = MibTableRow
dcx3212POSTEntry = _Dcx3212POSTEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 2, 1, 1)
)
dcx3212POSTEntry.setIndexNames(
    (0, "ARRIS-C3-POST-MIB", "dcx3212POSTType"),
)
if mibBuilder.loadTexts:
    dcx3212POSTEntry.setStatus("current")


class _Dcx3212POSTType_Type(Integer32):
    """Custom type dcx3212POSTType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Dcx3212POSTType_Type.__name__ = "Integer32"
_Dcx3212POSTType_Object = MibTableColumn
dcx3212POSTType = _Dcx3212POSTType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 2, 1, 1, 1),
    _Dcx3212POSTType_Type()
)
dcx3212POSTType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcx3212POSTType.setStatus("current")


class _Dcx3212POSTDescr_Type(DisplayString):
    """Custom type dcx3212POSTDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Dcx3212POSTDescr_Type.__name__ = "DisplayString"
_Dcx3212POSTDescr_Object = MibTableColumn
dcx3212POSTDescr = _Dcx3212POSTDescr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 2, 1, 1, 2),
    _Dcx3212POSTDescr_Type()
)
dcx3212POSTDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcx3212POSTDescr.setStatus("current")


class _Dcx3212POSTResult_Type(Integer32):
    """Custom type dcx3212POSTResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passed", 0),
          ("failed", 1),
          ("skipped", 2))
    )


_Dcx3212POSTResult_Type.__name__ = "Integer32"
_Dcx3212POSTResult_Object = MibTableColumn
dcx3212POSTResult = _Dcx3212POSTResult_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 13, 1, 2, 1, 1, 3),
    _Dcx3212POSTResult_Type()
)
dcx3212POSTResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcx3212POSTResult.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-C3-POST-MIB",
    **{"cmtsC3POSTMIB": cmtsC3POSTMIB,
       "dcxPOSTObjects": dcxPOSTObjects,
       "dcxCPUWANPOSTGroup": dcxCPUWANPOSTGroup,
       "dcxCPUWANPOSTTable": dcxCPUWANPOSTTable,
       "dcxCPUWANPOSTEntry": dcxCPUWANPOSTEntry,
       "dcxCPUWANPOSTType": dcxCPUWANPOSTType,
       "dcxCPUWANPOSTDescr": dcxCPUWANPOSTDescr,
       "dcxCPUWANPOSTResult": dcxCPUWANPOSTResult,
       "dcx3212POSTGroup": dcx3212POSTGroup,
       "dcx3212POSTTable": dcx3212POSTTable,
       "dcx3212POSTEntry": dcx3212POSTEntry,
       "dcx3212POSTType": dcx3212POSTType,
       "dcx3212POSTDescr": dcx3212POSTDescr,
       "dcx3212POSTResult": dcx3212POSTResult}
)
