# SNMP MIB module (CTRON-FRONTPANEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-FRONTPANEL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:40:59 2025
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

(ctFpRedundancy,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctFpRedundancy")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtFpRedund_ObjectIdentity = ObjectIdentity
ctFpRedund = _CtFpRedund_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1)
)


class _CtFpRedundReset_Type(Integer32):
    """Custom type ctFpRedundReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_CtFpRedundReset_Type.__name__ = "Integer32"
_CtFpRedundReset_Object = MibScalar
ctFpRedundReset = _CtFpRedundReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 1),
    _CtFpRedundReset_Type()
)
ctFpRedundReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFpRedundReset.setStatus("mandatory")
_CtFpRedundPollInterval_Type = Integer32
_CtFpRedundPollInterval_Object = MibScalar
ctFpRedundPollInterval = _CtFpRedundPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 2),
    _CtFpRedundPollInterval_Type()
)
ctFpRedundPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFpRedundPollInterval.setStatus("mandatory")
_CtFpRedundRetrys_Type = Integer32
_CtFpRedundRetrys_Object = MibScalar
ctFpRedundRetrys = _CtFpRedundRetrys_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 3),
    _CtFpRedundRetrys_Type()
)
ctFpRedundRetrys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFpRedundRetrys.setStatus("mandatory")
_CtFpRedundNumAddr_Type = Integer32
_CtFpRedundNumAddr_Object = MibScalar
ctFpRedundNumAddr = _CtFpRedundNumAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 4),
    _CtFpRedundNumAddr_Type()
)
ctFpRedundNumAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFpRedundNumAddr.setStatus("mandatory")
_CtFpRedundAddAddr_Type = IpAddress
_CtFpRedundAddAddr_Object = MibScalar
ctFpRedundAddAddr = _CtFpRedundAddAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 5),
    _CtFpRedundAddAddr_Type()
)
ctFpRedundAddAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFpRedundAddAddr.setStatus("mandatory")
_CtFpRedundDelAddr_Type = IpAddress
_CtFpRedundDelAddr_Object = MibScalar
ctFpRedundDelAddr = _CtFpRedundDelAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 6),
    _CtFpRedundDelAddr_Type()
)
ctFpRedundDelAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFpRedundDelAddr.setStatus("mandatory")
_CtFpRedundActivePort_Type = Integer32
_CtFpRedundActivePort_Object = MibScalar
ctFpRedundActivePort = _CtFpRedundActivePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 7),
    _CtFpRedundActivePort_Type()
)
ctFpRedundActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFpRedundActivePort.setStatus("mandatory")


class _CtFpRedundEnable_Type(Integer32):
    """Custom type ctFpRedundEnable based on Integer32"""
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


_CtFpRedundEnable_Type.__name__ = "Integer32"
_CtFpRedundEnable_Object = MibScalar
ctFpRedundEnable = _CtFpRedundEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 8),
    _CtFpRedundEnable_Type()
)
ctFpRedundEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctFpRedundEnable.setStatus("mandatory")
_CtFpRedundAddrTable_Object = MibTable
ctFpRedundAddrTable = _CtFpRedundAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 9)
)
if mibBuilder.loadTexts:
    ctFpRedundAddrTable.setStatus("mandatory")
_CtFpRedundAddrEntry_Object = MibTableRow
ctFpRedundAddrEntry = _CtFpRedundAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 9, 1)
)
ctFpRedundAddrEntry.setIndexNames(
    (0, "CTRON-FRONTPANEL-MIB", "ctFpRedundAddrId"),
)
if mibBuilder.loadTexts:
    ctFpRedundAddrEntry.setStatus("mandatory")


class _CtFpRedundAddrId_Type(Integer32):
    """Custom type ctFpRedundAddrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtFpRedundAddrId_Type.__name__ = "Integer32"
_CtFpRedundAddrId_Object = MibTableColumn
ctFpRedundAddrId = _CtFpRedundAddrId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 9, 1, 1),
    _CtFpRedundAddrId_Type()
)
ctFpRedundAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFpRedundAddrId.setStatus("mandatory")
_CtFpRedundAddrIPAddr_Type = IpAddress
_CtFpRedundAddrIPAddr_Object = MibTableColumn
ctFpRedundAddrIPAddr = _CtFpRedundAddrIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5, 1, 9, 1, 2),
    _CtFpRedundAddrIPAddr_Type()
)
ctFpRedundAddrIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctFpRedundAddrIPAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-FRONTPANEL-MIB",
    **{"ctFpRedund": ctFpRedund,
       "ctFpRedundReset": ctFpRedundReset,
       "ctFpRedundPollInterval": ctFpRedundPollInterval,
       "ctFpRedundRetrys": ctFpRedundRetrys,
       "ctFpRedundNumAddr": ctFpRedundNumAddr,
       "ctFpRedundAddAddr": ctFpRedundAddAddr,
       "ctFpRedundDelAddr": ctFpRedundDelAddr,
       "ctFpRedundActivePort": ctFpRedundActivePort,
       "ctFpRedundEnable": ctFpRedundEnable,
       "ctFpRedundAddrTable": ctFpRedundAddrTable,
       "ctFpRedundAddrEntry": ctFpRedundAddrEntry,
       "ctFpRedundAddrId": ctFpRedundAddrId,
       "ctFpRedundAddrIPAddr": ctFpRedundAddrIPAddr}
)
