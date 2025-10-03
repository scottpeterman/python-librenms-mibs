# SNMP MIB module (HH3C-FCOE-MODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-FCOE-MODE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:39 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cFcoeMode = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 135)
)
if mibBuilder.loadTexts:
    hh3cFcoeMode.setRevisions(
        ("2013-03-08 11:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cFcoeModeMibObjects_ObjectIdentity = ObjectIdentity
hh3cFcoeModeMibObjects = _Hh3cFcoeModeMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 135, 1)
)
_Hh3cFcoeModeCfgMode_Type = Integer32
_Hh3cFcoeModeCfgMode_Object = MibScalar
hh3cFcoeModeCfgMode = _Hh3cFcoeModeCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 135, 1, 1),
    _Hh3cFcoeModeCfgMode_Type()
)
hh3cFcoeModeCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcoeModeCfgMode.setStatus("current")


class _Hh3cFcoeModeCfgLastResult_Type(Integer32):
    """Custom type hh3cFcoeModeCfgLastResult based on Integer32"""
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
        *(("success", 1),
          ("noLicence", 2),
          ("needReset", 3),
          ("unknownFault", 4))
    )


_Hh3cFcoeModeCfgLastResult_Type.__name__ = "Integer32"
_Hh3cFcoeModeCfgLastResult_Object = MibScalar
hh3cFcoeModeCfgLastResult = _Hh3cFcoeModeCfgLastResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 135, 1, 2),
    _Hh3cFcoeModeCfgLastResult_Type()
)
hh3cFcoeModeCfgLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcoeModeCfgLastResult.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FCOE-MODE-MIB",
    **{"hh3cFcoeMode": hh3cFcoeMode,
       "hh3cFcoeModeMibObjects": hh3cFcoeModeMibObjects,
       "hh3cFcoeModeCfgMode": hh3cFcoeModeCfgMode,
       "hh3cFcoeModeCfgLastResult": hh3cFcoeModeCfgLastResult}
)
