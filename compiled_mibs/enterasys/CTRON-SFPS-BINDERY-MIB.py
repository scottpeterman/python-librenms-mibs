# SNMP MIB module (CTRON-SFPS-BINDERY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-SFPS-BINDERY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:41:22 2025
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

(sfpsAgentConfig,) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsAgentConfig")

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


# Types definitions



class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsAgentBinderyConfigTable_Object = MibTable
sfpsAgentBinderyConfigTable = _SfpsAgentBinderyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    sfpsAgentBinderyConfigTable.setStatus("mandatory")
_SfpsAgentBinderyConfigEntry_Object = MibTableRow
sfpsAgentBinderyConfigEntry = _SfpsAgentBinderyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1)
)
sfpsAgentBinderyConfigEntry.setIndexNames(
    (0, "CTRON-SFPS-BINDERY-MIB", "sfpsAgentBinderyConfigHashLeaf"),
    (0, "CTRON-SFPS-BINDERY-MIB", "sfpsAgentBinderyConfigHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsAgentBinderyConfigEntry.setStatus("mandatory")
_SfpsAgentBinderyConfigHashLeaf_Type = HexInteger
_SfpsAgentBinderyConfigHashLeaf_Object = MibTableColumn
sfpsAgentBinderyConfigHashLeaf = _SfpsAgentBinderyConfigHashLeaf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 1),
    _SfpsAgentBinderyConfigHashLeaf_Type()
)
sfpsAgentBinderyConfigHashLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAgentBinderyConfigHashLeaf.setStatus("mandatory")
_SfpsAgentBinderyConfigHashIndex_Type = Integer32
_SfpsAgentBinderyConfigHashIndex_Object = MibTableColumn
sfpsAgentBinderyConfigHashIndex = _SfpsAgentBinderyConfigHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 2),
    _SfpsAgentBinderyConfigHashIndex_Type()
)
sfpsAgentBinderyConfigHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAgentBinderyConfigHashIndex.setStatus("mandatory")
_SfpsAgentBinderyConfigName_Type = DisplayString
_SfpsAgentBinderyConfigName_Object = MibTableColumn
sfpsAgentBinderyConfigName = _SfpsAgentBinderyConfigName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 3),
    _SfpsAgentBinderyConfigName_Type()
)
sfpsAgentBinderyConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAgentBinderyConfigName.setStatus("mandatory")
_SfpsAgentBinderyConfigType_Type = DisplayString
_SfpsAgentBinderyConfigType_Object = MibTableColumn
sfpsAgentBinderyConfigType = _SfpsAgentBinderyConfigType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 4),
    _SfpsAgentBinderyConfigType_Type()
)
sfpsAgentBinderyConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAgentBinderyConfigType.setStatus("mandatory")


class _SfpsAgentBinderyConfigOperStatus_Type(Integer32):
    """Custom type sfpsAgentBinderyConfigOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("kStatusRunning", 1),
          ("kStatusHalted", 2),
          ("kStatusPending", 3),
          ("kStatusFaulted", 4),
          ("kStatusNotStarted", 5))
    )


_SfpsAgentBinderyConfigOperStatus_Type.__name__ = "Integer32"
_SfpsAgentBinderyConfigOperStatus_Object = MibTableColumn
sfpsAgentBinderyConfigOperStatus = _SfpsAgentBinderyConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 5),
    _SfpsAgentBinderyConfigOperStatus_Type()
)
sfpsAgentBinderyConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAgentBinderyConfigOperStatus.setStatus("mandatory")


class _SfpsAgentBinderyConfigAdminStatus_Type(Integer32):
    """Custom type sfpsAgentBinderyConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disable", 2),
          ("enable", 3))
    )


_SfpsAgentBinderyConfigAdminStatus_Type.__name__ = "Integer32"
_SfpsAgentBinderyConfigAdminStatus_Object = MibTableColumn
sfpsAgentBinderyConfigAdminStatus = _SfpsAgentBinderyConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 6),
    _SfpsAgentBinderyConfigAdminStatus_Type()
)
sfpsAgentBinderyConfigAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAgentBinderyConfigAdminStatus.setStatus("mandatory")
_SfpsAgentBinderyConfigStatusTime_Type = TimeTicks
_SfpsAgentBinderyConfigStatusTime_Object = MibTableColumn
sfpsAgentBinderyConfigStatusTime = _SfpsAgentBinderyConfigStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 7),
    _SfpsAgentBinderyConfigStatusTime_Type()
)
sfpsAgentBinderyConfigStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAgentBinderyConfigStatusTime.setStatus("mandatory")


class _SfpsAgentBinderyConfigNVStatus_Type(Integer32):
    """Custom type sfpsAgentBinderyConfigNVStatus based on Integer32"""
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
        *(("other", 1),
          ("disable", 2),
          ("enable", 3),
          ("unset", 4))
    )


_SfpsAgentBinderyConfigNVStatus_Type.__name__ = "Integer32"
_SfpsAgentBinderyConfigNVStatus_Object = MibTableColumn
sfpsAgentBinderyConfigNVStatus = _SfpsAgentBinderyConfigNVStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 8),
    _SfpsAgentBinderyConfigNVStatus_Type()
)
sfpsAgentBinderyConfigNVStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAgentBinderyConfigNVStatus.setStatus("mandatory")
_SfpsAgentBinderyAPI_ObjectIdentity = ObjectIdentity
sfpsAgentBinderyAPI = _SfpsAgentBinderyAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2)
)


class _SfpsAgentBinderyAPIVerb_Type(Integer32):
    """Custom type sfpsAgentBinderyAPIVerb based on Integer32"""
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
        *(("getStatus", 1),
          ("nextElem", 2),
          ("disable", 3),
          ("disableInNvram", 4),
          ("enable", 5),
          ("enableInNvram", 6),
          ("clear", 7),
          ("clearAll", 8))
    )


_SfpsAgentBinderyAPIVerb_Type.__name__ = "Integer32"
_SfpsAgentBinderyAPIVerb_Object = MibScalar
sfpsAgentBinderyAPIVerb = _SfpsAgentBinderyAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 1),
    _SfpsAgentBinderyAPIVerb_Type()
)
sfpsAgentBinderyAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAgentBinderyAPIVerb.setStatus("mandatory")
_SfpsAgentBinderyAPIElementName_Type = DisplayString
_SfpsAgentBinderyAPIElementName_Object = MibScalar
sfpsAgentBinderyAPIElementName = _SfpsAgentBinderyAPIElementName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 2),
    _SfpsAgentBinderyAPIElementName_Type()
)
sfpsAgentBinderyAPIElementName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAgentBinderyAPIElementName.setStatus("mandatory")


class _SfpsAgentBinderyAPINVStatus_Type(Integer32):
    """Custom type sfpsAgentBinderyAPINVStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disable", 2),
          ("enable", 3),
          ("unset", 4),
          ("invalid", 5))
    )


_SfpsAgentBinderyAPINVStatus_Type.__name__ = "Integer32"
_SfpsAgentBinderyAPINVStatus_Object = MibScalar
sfpsAgentBinderyAPINVStatus = _SfpsAgentBinderyAPINVStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 3),
    _SfpsAgentBinderyAPINVStatus_Type()
)
sfpsAgentBinderyAPINVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAgentBinderyAPINVStatus.setStatus("mandatory")


class _SfpsAgentBinderyAPIAdminStatus_Type(Integer32):
    """Custom type sfpsAgentBinderyAPIAdminStatus based on Integer32"""
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
        *(("other", 1),
          ("disable", 2),
          ("enable", 3),
          ("invalid", 4))
    )


_SfpsAgentBinderyAPIAdminStatus_Type.__name__ = "Integer32"
_SfpsAgentBinderyAPIAdminStatus_Object = MibScalar
sfpsAgentBinderyAPIAdminStatus = _SfpsAgentBinderyAPIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 4),
    _SfpsAgentBinderyAPIAdminStatus_Type()
)
sfpsAgentBinderyAPIAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAgentBinderyAPIAdminStatus.setStatus("mandatory")


class _SfpsAgentBinderyAPIOperStatus_Type(Integer32):
    """Custom type sfpsAgentBinderyAPIOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("halted", 2),
          ("pending", 3),
          ("faulted", 4),
          ("notStarted", 5),
          ("invalid", 6))
    )


_SfpsAgentBinderyAPIOperStatus_Type.__name__ = "Integer32"
_SfpsAgentBinderyAPIOperStatus_Object = MibScalar
sfpsAgentBinderyAPIOperStatus = _SfpsAgentBinderyAPIOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 5),
    _SfpsAgentBinderyAPIOperStatus_Type()
)
sfpsAgentBinderyAPIOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAgentBinderyAPIOperStatus.setStatus("mandatory")
_SfpsAgentBinderyAPINvSet_Type = Integer32
_SfpsAgentBinderyAPINvSet_Object = MibScalar
sfpsAgentBinderyAPINvSet = _SfpsAgentBinderyAPINvSet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 6),
    _SfpsAgentBinderyAPINvSet_Type()
)
sfpsAgentBinderyAPINvSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAgentBinderyAPINvSet.setStatus("mandatory")
_SfpsAgentBinderyAPINvTotal_Type = Integer32
_SfpsAgentBinderyAPINvTotal_Object = MibScalar
sfpsAgentBinderyAPINvTotal = _SfpsAgentBinderyAPINvTotal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 7),
    _SfpsAgentBinderyAPINvTotal_Type()
)
sfpsAgentBinderyAPINvTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAgentBinderyAPINvTotal.setStatus("mandatory")


class _SfpsAgentBinderyAPIDefaultStatus_Type(Integer32):
    """Custom type sfpsAgentBinderyAPIDefaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disable", 2),
          ("enable", 3),
          ("unset", 4),
          ("invalid", 5))
    )


_SfpsAgentBinderyAPIDefaultStatus_Type.__name__ = "Integer32"
_SfpsAgentBinderyAPIDefaultStatus_Object = MibScalar
sfpsAgentBinderyAPIDefaultStatus = _SfpsAgentBinderyAPIDefaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 8),
    _SfpsAgentBinderyAPIDefaultStatus_Type()
)
sfpsAgentBinderyAPIDefaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAgentBinderyAPIDefaultStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-BINDERY-MIB",
    **{"HexInteger": HexInteger,
       "sfpsAgentBinderyConfigTable": sfpsAgentBinderyConfigTable,
       "sfpsAgentBinderyConfigEntry": sfpsAgentBinderyConfigEntry,
       "sfpsAgentBinderyConfigHashLeaf": sfpsAgentBinderyConfigHashLeaf,
       "sfpsAgentBinderyConfigHashIndex": sfpsAgentBinderyConfigHashIndex,
       "sfpsAgentBinderyConfigName": sfpsAgentBinderyConfigName,
       "sfpsAgentBinderyConfigType": sfpsAgentBinderyConfigType,
       "sfpsAgentBinderyConfigOperStatus": sfpsAgentBinderyConfigOperStatus,
       "sfpsAgentBinderyConfigAdminStatus": sfpsAgentBinderyConfigAdminStatus,
       "sfpsAgentBinderyConfigStatusTime": sfpsAgentBinderyConfigStatusTime,
       "sfpsAgentBinderyConfigNVStatus": sfpsAgentBinderyConfigNVStatus,
       "sfpsAgentBinderyAPI": sfpsAgentBinderyAPI,
       "sfpsAgentBinderyAPIVerb": sfpsAgentBinderyAPIVerb,
       "sfpsAgentBinderyAPIElementName": sfpsAgentBinderyAPIElementName,
       "sfpsAgentBinderyAPINVStatus": sfpsAgentBinderyAPINVStatus,
       "sfpsAgentBinderyAPIAdminStatus": sfpsAgentBinderyAPIAdminStatus,
       "sfpsAgentBinderyAPIOperStatus": sfpsAgentBinderyAPIOperStatus,
       "sfpsAgentBinderyAPINvSet": sfpsAgentBinderyAPINvSet,
       "sfpsAgentBinderyAPINvTotal": sfpsAgentBinderyAPINvTotal,
       "sfpsAgentBinderyAPIDefaultStatus": sfpsAgentBinderyAPIDefaultStatus}
)
