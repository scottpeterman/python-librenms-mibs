# SNMP MIB module (RADLAN-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\radlan\RADLAN-SNMP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:22:38 2025
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

rlSNMP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 98)
)
if mibBuilder.loadTexts:
    rlSNMP.setRevisions(
        ("1904-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlSnmpUDPMridAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d.1d.1d.1d/2d/2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



# MIB Managed Objects in the order of their OIDs

_RlSNMPv3_ObjectIdentity = ObjectIdentity
rlSNMPv3 = _RlSNMPv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 98, 1)
)


class _RlTargetParamsTestingLevel_Type(Integer32):
    """Custom type rlTargetParamsTestingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_RlTargetParamsTestingLevel_Type.__name__ = "Integer32"
_RlTargetParamsTestingLevel_Object = MibScalar
rlTargetParamsTestingLevel = _RlTargetParamsTestingLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 1),
    _RlTargetParamsTestingLevel_Type()
)
rlTargetParamsTestingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTargetParamsTestingLevel.setStatus("current")


class _RlNotifyFilterTestingLevel_Type(Integer32):
    """Custom type rlNotifyFilterTestingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_RlNotifyFilterTestingLevel_Type.__name__ = "Integer32"
_RlNotifyFilterTestingLevel_Object = MibScalar
rlNotifyFilterTestingLevel = _RlNotifyFilterTestingLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 2),
    _RlNotifyFilterTestingLevel_Type()
)
rlNotifyFilterTestingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNotifyFilterTestingLevel.setStatus("current")


class _RlSnmpEngineID_Type(OctetString):
    """Custom type rlSnmpEngineID based on OctetString"""
    defaultHexValue = "0000000001"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_RlSnmpEngineID_Type.__name__ = "OctetString"
_RlSnmpEngineID_Object = MibScalar
rlSnmpEngineID = _RlSnmpEngineID_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 1, 3),
    _RlSnmpEngineID_Type()
)
rlSnmpEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSnmpEngineID.setStatus("current")
_RlSNMPDomains_ObjectIdentity = ObjectIdentity
rlSNMPDomains = _RlSNMPDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 98, 2)
)
_RlSnmpUDPMridDomain_ObjectIdentity = ObjectIdentity
rlSnmpUDPMridDomain = _RlSnmpUDPMridDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 98, 2, 1)
)
if mibBuilder.loadTexts:
    rlSnmpUDPMridDomain.setStatus("current")
_RlSnmpRequestMridTable_Object = MibTable
rlSnmpRequestMridTable = _RlSnmpRequestMridTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 3)
)
if mibBuilder.loadTexts:
    rlSnmpRequestMridTable.setStatus("current")
_RlSnmpRequestMridEntry_Object = MibTableRow
rlSnmpRequestMridEntry = _RlSnmpRequestMridEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 3, 1)
)
rlSnmpRequestMridEntry.setIndexNames(
    (0, "RADLAN-SNMP-MIB", "rlSnmpRequestManagedMrid"),
)
if mibBuilder.loadTexts:
    rlSnmpRequestMridEntry.setStatus("current")
_RlSnmpRequestManagedMrid_Type = Integer32
_RlSnmpRequestManagedMrid_Object = MibTableColumn
rlSnmpRequestManagedMrid = _RlSnmpRequestManagedMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 3, 1, 1),
    _RlSnmpRequestManagedMrid_Type()
)
rlSnmpRequestManagedMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSnmpRequestManagedMrid.setStatus("current")


class _RlSnmpRequestMridStatus_Type(Integer32):
    """Custom type rlSnmpRequestMridStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_RlSnmpRequestMridStatus_Type.__name__ = "Integer32"
_RlSnmpRequestMridStatus_Object = MibTableColumn
rlSnmpRequestMridStatus = _RlSnmpRequestMridStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 98, 3, 1, 2),
    _RlSnmpRequestMridStatus_Type()
)
rlSnmpRequestMridStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSnmpRequestMridStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-SNMP-MIB",
    **{"RlSnmpUDPMridAddress": RlSnmpUDPMridAddress,
       "rlSNMP": rlSNMP,
       "rlSNMPv3": rlSNMPv3,
       "rlTargetParamsTestingLevel": rlTargetParamsTestingLevel,
       "rlNotifyFilterTestingLevel": rlNotifyFilterTestingLevel,
       "rlSnmpEngineID": rlSnmpEngineID,
       "rlSNMPDomains": rlSNMPDomains,
       "rlSnmpUDPMridDomain": rlSnmpUDPMridDomain,
       "rlSnmpRequestMridTable": rlSnmpRequestMridTable,
       "rlSnmpRequestMridEntry": rlSnmpRequestMridEntry,
       "rlSnmpRequestManagedMrid": rlSnmpRequestManagedMrid,
       "rlSnmpRequestMridStatus": rlSnmpRequestMridStatus}
)
