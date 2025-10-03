# SNMP MIB module (CTRON-SFPS-CONN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-SFPS-CONN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:41:25 2025
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

(sfpsServiceCenter,) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsServiceCenter")

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

_SfpsServiceCenterConnectTable_Object = MibTable
sfpsServiceCenterConnectTable = _SfpsServiceCenterConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    sfpsServiceCenterConnectTable.setStatus("mandatory")
_SfpsServiceCenterConnectEntry_Object = MibTableRow
sfpsServiceCenterConnectEntry = _SfpsServiceCenterConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1)
)
sfpsServiceCenterConnectEntry.setIndexNames(
    (0, "CTRON-SFPS-CONN-MIB", "sfpsServiceCenterConnectAddress"),
)
if mibBuilder.loadTexts:
    sfpsServiceCenterConnectEntry.setStatus("mandatory")
_SfpsServiceCenterConnectAddress_Type = HexInteger
_SfpsServiceCenterConnectAddress_Object = MibTableColumn
sfpsServiceCenterConnectAddress = _SfpsServiceCenterConnectAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 1),
    _SfpsServiceCenterConnectAddress_Type()
)
sfpsServiceCenterConnectAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterConnectAddress.setStatus("mandatory")
_SfpsServiceCenterConnectMetric_Type = Integer32
_SfpsServiceCenterConnectMetric_Object = MibTableColumn
sfpsServiceCenterConnectMetric = _SfpsServiceCenterConnectMetric_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 2),
    _SfpsServiceCenterConnectMetric_Type()
)
sfpsServiceCenterConnectMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterConnectMetric.setStatus("mandatory")
_SfpsServiceCenterConnectName_Type = DisplayString
_SfpsServiceCenterConnectName_Object = MibTableColumn
sfpsServiceCenterConnectName = _SfpsServiceCenterConnectName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 3),
    _SfpsServiceCenterConnectName_Type()
)
sfpsServiceCenterConnectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterConnectName.setStatus("mandatory")


class _SfpsServiceCenterConnectOperStatus_Type(Integer32):
    """Custom type sfpsServiceCenterConnectOperStatus based on Integer32"""
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


_SfpsServiceCenterConnectOperStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterConnectOperStatus_Object = MibTableColumn
sfpsServiceCenterConnectOperStatus = _SfpsServiceCenterConnectOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 4),
    _SfpsServiceCenterConnectOperStatus_Type()
)
sfpsServiceCenterConnectOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterConnectOperStatus.setStatus("mandatory")


class _SfpsServiceCenterConnectAdminStatus_Type(Integer32):
    """Custom type sfpsServiceCenterConnectAdminStatus based on Integer32"""
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


_SfpsServiceCenterConnectAdminStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterConnectAdminStatus_Object = MibTableColumn
sfpsServiceCenterConnectAdminStatus = _SfpsServiceCenterConnectAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 5),
    _SfpsServiceCenterConnectAdminStatus_Type()
)
sfpsServiceCenterConnectAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsServiceCenterConnectAdminStatus.setStatus("mandatory")
_SfpsServiceCenterConnectStatusTime_Type = TimeTicks
_SfpsServiceCenterConnectStatusTime_Object = MibTableColumn
sfpsServiceCenterConnectStatusTime = _SfpsServiceCenterConnectStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 6),
    _SfpsServiceCenterConnectStatusTime_Type()
)
sfpsServiceCenterConnectStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterConnectStatusTime.setStatus("mandatory")
_SfpsServiceCenterConnectRequests_Type = Integer32
_SfpsServiceCenterConnectRequests_Object = MibTableColumn
sfpsServiceCenterConnectRequests = _SfpsServiceCenterConnectRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 7),
    _SfpsServiceCenterConnectRequests_Type()
)
sfpsServiceCenterConnectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterConnectRequests.setStatus("mandatory")
_SfpsServiceCenterConnectResponses_Type = Integer32
_SfpsServiceCenterConnectResponses_Object = MibTableColumn
sfpsServiceCenterConnectResponses = _SfpsServiceCenterConnectResponses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 8),
    _SfpsServiceCenterConnectResponses_Type()
)
sfpsServiceCenterConnectResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterConnectResponses.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-CONN-MIB",
    **{"HexInteger": HexInteger,
       "sfpsServiceCenterConnectTable": sfpsServiceCenterConnectTable,
       "sfpsServiceCenterConnectEntry": sfpsServiceCenterConnectEntry,
       "sfpsServiceCenterConnectAddress": sfpsServiceCenterConnectAddress,
       "sfpsServiceCenterConnectMetric": sfpsServiceCenterConnectMetric,
       "sfpsServiceCenterConnectName": sfpsServiceCenterConnectName,
       "sfpsServiceCenterConnectOperStatus": sfpsServiceCenterConnectOperStatus,
       "sfpsServiceCenterConnectAdminStatus": sfpsServiceCenterConnectAdminStatus,
       "sfpsServiceCenterConnectStatusTime": sfpsServiceCenterConnectStatusTime,
       "sfpsServiceCenterConnectRequests": sfpsServiceCenterConnectRequests,
       "sfpsServiceCenterConnectResponses": sfpsServiceCenterConnectResponses}
)
