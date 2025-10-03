# SNMP MIB module (CISCOSB-LBD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-LBD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:28:58 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlLbd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127)
)
if mibBuilder.loadTexts:
    rlLbd.setRevisions(
        ("2007-11-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlLbdEnable_Type = TruthValue
_RlLbdEnable_Object = MibScalar
rlLbdEnable = _RlLbdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 1),
    _RlLbdEnable_Type()
)
rlLbdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLbdEnable.setStatus("current")


class _RlLbdDetectionInterval_Type(Integer32):
    """Custom type rlLbdDetectionInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_RlLbdDetectionInterval_Type.__name__ = "Integer32"
_RlLbdDetectionInterval_Object = MibScalar
rlLbdDetectionInterval = _RlLbdDetectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 2),
    _RlLbdDetectionInterval_Type()
)
rlLbdDetectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLbdDetectionInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlLbdDetectionInterval.setUnits("seconds")


class _RlLbdMode_Type(Integer32):
    """Custom type rlLbdMode based on Integer32"""
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
        *(("source-mac-addr", 1),
          ("base-mac-addr", 2),
          ("broadcast-mac-addr", 3),
          ("predefined-multicast-mac-addr", 4),
          ("user-defined-mac-addr", 5))
    )


_RlLbdMode_Type.__name__ = "Integer32"
_RlLbdMode_Object = MibScalar
rlLbdMode = _RlLbdMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 3),
    _RlLbdMode_Type()
)
rlLbdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLbdMode.setStatus("current")
_RlLbdPortTable_Object = MibTable
rlLbdPortTable = _RlLbdPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4)
)
if mibBuilder.loadTexts:
    rlLbdPortTable.setStatus("current")
_RlLbdPortEntry_Object = MibTableRow
rlLbdPortEntry = _RlLbdPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4, 1)
)
rlLbdPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlLbdPortEntry.setStatus("current")


class _RlLbdPortAdminStatus_Type(Integer32):
    """Custom type rlLbdPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RlLbdPortAdminStatus_Type.__name__ = "Integer32"
_RlLbdPortAdminStatus_Object = MibTableColumn
rlLbdPortAdminStatus = _RlLbdPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4, 1, 1),
    _RlLbdPortAdminStatus_Type()
)
rlLbdPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLbdPortAdminStatus.setStatus("current")


class _RlLbdPortOperStatus_Type(Integer32):
    """Custom type rlLbdPortOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2),
          ("loopDetected", 3))
    )


_RlLbdPortOperStatus_Type.__name__ = "Integer32"
_RlLbdPortOperStatus_Object = MibTableColumn
rlLbdPortOperStatus = _RlLbdPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127, 4, 1, 2),
    _RlLbdPortOperStatus_Type()
)
rlLbdPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLbdPortOperStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-LBD-MIB",
    **{"rlLbd": rlLbd,
       "rlLbdEnable": rlLbdEnable,
       "rlLbdDetectionInterval": rlLbdDetectionInterval,
       "rlLbdMode": rlLbdMode,
       "rlLbdPortTable": rlLbdPortTable,
       "rlLbdPortEntry": rlLbdPortEntry,
       "rlLbdPortAdminStatus": rlLbdPortAdminStatus,
       "rlLbdPortOperStatus": rlLbdPortOperStatus}
)
