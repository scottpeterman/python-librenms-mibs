# SNMP MIB module (SIAE-HC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-HC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:56 2025
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

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

headerCompression = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 79)
)
if mibBuilder.loadTexts:
    headerCompression.setRevisions(
        ("2014-10-07 00:00",
         "2014-03-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HeaderCompressionMibVersion_Type = Integer32
_HeaderCompressionMibVersion_Object = MibScalar
headerCompressionMibVersion = _HeaderCompressionMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 79, 1),
    _HeaderCompressionMibVersion_Type()
)
headerCompressionMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    headerCompressionMibVersion.setStatus("current")
_HeaderCompressionTable_Object = MibTable
headerCompressionTable = _HeaderCompressionTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2)
)
if mibBuilder.loadTexts:
    headerCompressionTable.setStatus("current")
_HeaderCompressionEntry_Object = MibTableRow
headerCompressionEntry = _HeaderCompressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1)
)
headerCompressionEntry.setIndexNames(
    (0, "SIAE-HC-MIB", "headerCompressionIndex"),
)
if mibBuilder.loadTexts:
    headerCompressionEntry.setStatus("current")
_HeaderCompressionIndex_Type = Integer32
_HeaderCompressionIndex_Object = MibTableColumn
headerCompressionIndex = _HeaderCompressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 1),
    _HeaderCompressionIndex_Type()
)
headerCompressionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    headerCompressionIndex.setStatus("current")


class _HeaderCompressionAdminStatus_Type(Integer32):
    """Custom type headerCompressionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_HeaderCompressionAdminStatus_Type.__name__ = "Integer32"
_HeaderCompressionAdminStatus_Object = MibTableColumn
headerCompressionAdminStatus = _HeaderCompressionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 2),
    _HeaderCompressionAdminStatus_Type()
)
headerCompressionAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    headerCompressionAdminStatus.setStatus("current")


class _HeaderCompressionContextDepth_Type(Integer32):
    """Custom type headerCompressionContextDepth based on Integer32"""
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
        *(("ctx16bytes", 1),
          ("ctx32bytes", 2),
          ("ctx64byets", 3),
          ("ctx128bytes", 4))
    )


_HeaderCompressionContextDepth_Type.__name__ = "Integer32"
_HeaderCompressionContextDepth_Object = MibTableColumn
headerCompressionContextDepth = _HeaderCompressionContextDepth_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 3),
    _HeaderCompressionContextDepth_Type()
)
headerCompressionContextDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    headerCompressionContextDepth.setStatus("current")


class _HeaderCompressionParsingMode_Type(Integer32):
    """Custom type headerCompressionParsingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("semiMpls", 2),
          ("semiIPv4IPv6", 3))
    )


_HeaderCompressionParsingMode_Type.__name__ = "Integer32"
_HeaderCompressionParsingMode_Object = MibTableColumn
headerCompressionParsingMode = _HeaderCompressionParsingMode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 4),
    _HeaderCompressionParsingMode_Type()
)
headerCompressionParsingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    headerCompressionParsingMode.setStatus("current")


class _HeaderCompressionTagEnable_Type(Integer32):
    """Custom type headerCompressionTagEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HeaderCompressionTagEnable_Type.__name__ = "Integer32"
_HeaderCompressionTagEnable_Object = MibTableColumn
headerCompressionTagEnable = _HeaderCompressionTagEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 5),
    _HeaderCompressionTagEnable_Type()
)
headerCompressionTagEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    headerCompressionTagEnable.setStatus("current")
_HeaderCompressionRowStatus_Type = RowStatus
_HeaderCompressionRowStatus_Object = MibTableColumn
headerCompressionRowStatus = _HeaderCompressionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 6),
    _HeaderCompressionRowStatus_Type()
)
headerCompressionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    headerCompressionRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-HC-MIB",
    **{"headerCompression": headerCompression,
       "headerCompressionMibVersion": headerCompressionMibVersion,
       "headerCompressionTable": headerCompressionTable,
       "headerCompressionEntry": headerCompressionEntry,
       "headerCompressionIndex": headerCompressionIndex,
       "headerCompressionAdminStatus": headerCompressionAdminStatus,
       "headerCompressionContextDepth": headerCompressionContextDepth,
       "headerCompressionParsingMode": headerCompressionParsingMode,
       "headerCompressionTagEnable": headerCompressionTagEnable,
       "headerCompressionRowStatus": headerCompressionRowStatus}
)
