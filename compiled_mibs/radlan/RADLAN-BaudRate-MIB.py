# SNMP MIB module (RADLAN-BaudRate-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\radlan\RADLAN-BaudRate-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:22:12 2025
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

rlRs232 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 104)
)
if mibBuilder.loadTexts:
    rlRs232.setRevisions(
        ("2005-04-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlRs232MibVersion_Type = Integer32
_RlRs232MibVersion_Object = MibScalar
rlRs232MibVersion = _RlRs232MibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 104, 1),
    _RlRs232MibVersion_Type()
)
rlRs232MibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRs232MibVersion.setStatus("current")


class _RlRs232AutoBaudRateStatus_Type(Integer32):
    """Custom type rlRs232AutoBaudRateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlRs232AutoBaudRateStatus_Type.__name__ = "Integer32"
_RlRs232AutoBaudRateStatus_Object = MibScalar
rlRs232AutoBaudRateStatus = _RlRs232AutoBaudRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 104, 2),
    _RlRs232AutoBaudRateStatus_Type()
)
rlRs232AutoBaudRateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRs232AutoBaudRateStatus.setStatus("current")


class _RlRs232AutoBaudRateStatusAfterReset_Type(Integer32):
    """Custom type rlRs232AutoBaudRateStatusAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlRs232AutoBaudRateStatusAfterReset_Type.__name__ = "Integer32"
_RlRs232AutoBaudRateStatusAfterReset_Object = MibScalar
rlRs232AutoBaudRateStatusAfterReset = _RlRs232AutoBaudRateStatusAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 104, 3),
    _RlRs232AutoBaudRateStatusAfterReset_Type()
)
rlRs232AutoBaudRateStatusAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRs232AutoBaudRateStatusAfterReset.setStatus("current")


class _RlRs232BaudRate_Type(Integer32):
    """Custom type rlRs232BaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("baud2400", 1),
          ("baud4800", 2),
          ("baud9600", 3),
          ("baud19200", 4),
          ("baud38400", 5),
          ("baud57600", 6),
          ("baud115200", 7))
    )


_RlRs232BaudRate_Type.__name__ = "Integer32"
_RlRs232BaudRate_Object = MibScalar
rlRs232BaudRate = _RlRs232BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 104, 4),
    _RlRs232BaudRate_Type()
)
rlRs232BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRs232BaudRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-BaudRate-MIB",
    **{"rlRs232": rlRs232,
       "rlRs232MibVersion": rlRs232MibVersion,
       "rlRs232AutoBaudRateStatus": rlRs232AutoBaudRateStatus,
       "rlRs232AutoBaudRateStatusAfterReset": rlRs232AutoBaudRateStatusAfterReset,
       "rlRs232BaudRate": rlRs232BaudRate}
)
