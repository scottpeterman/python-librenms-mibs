# SNMP MIB module (CISCOSB-JUMBOFRAMES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-JUMBOFRAMES-MIB
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

rlJumboFrames = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 91)
)
if mibBuilder.loadTexts:
    rlJumboFrames.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlJumboFramesCurrentStatus_Type(Integer32):
    """Custom type rlJumboFramesCurrentStatus based on Integer32"""
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


_RlJumboFramesCurrentStatus_Type.__name__ = "Integer32"
_RlJumboFramesCurrentStatus_Object = MibScalar
rlJumboFramesCurrentStatus = _RlJumboFramesCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 91, 1),
    _RlJumboFramesCurrentStatus_Type()
)
rlJumboFramesCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlJumboFramesCurrentStatus.setStatus("current")


class _RlJumboFramesStatusAfterReset_Type(Integer32):
    """Custom type rlJumboFramesStatusAfterReset based on Integer32"""
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


_RlJumboFramesStatusAfterReset_Type.__name__ = "Integer32"
_RlJumboFramesStatusAfterReset_Object = MibScalar
rlJumboFramesStatusAfterReset = _RlJumboFramesStatusAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 91, 2),
    _RlJumboFramesStatusAfterReset_Type()
)
rlJumboFramesStatusAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlJumboFramesStatusAfterReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-JUMBOFRAMES-MIB",
    **{"rlJumboFrames": rlJumboFrames,
       "rlJumboFramesCurrentStatus": rlJumboFramesCurrentStatus,
       "rlJumboFramesStatusAfterReset": rlJumboFramesStatusAfterReset}
)
