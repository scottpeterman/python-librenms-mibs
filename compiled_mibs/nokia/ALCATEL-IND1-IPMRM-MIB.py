# SNMP MIB module (ALCATEL-IND1-IPMRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-IPMRM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:31 2025
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

(routingIND1Ipmrm,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Ipmrm")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

alcatelIND1IPMRMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1IPMRMMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IPMRMMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IPMRMMIBObjects = _AlcatelIND1IPMRMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 1)
)
_AlaIpmrmDebugConfig_ObjectIdentity = ObjectIdentity
alaIpmrmDebugConfig = _AlaIpmrmDebugConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 1, 1)
)


class _AlaIpmrmDebugLevel_Type(Integer32):
    """Custom type alaIpmrmDebugLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaIpmrmDebugLevel_Type.__name__ = "Integer32"
_AlaIpmrmDebugLevel_Object = MibScalar
alaIpmrmDebugLevel = _AlaIpmrmDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 1, 1, 1),
    _AlaIpmrmDebugLevel_Type()
)
alaIpmrmDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmrmDebugLevel.setStatus("deprecated")


class _AlaIpmrmDebugError_Type(Integer32):
    """Custom type alaIpmrmDebugError based on Integer32"""
    defaultValue = 2

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


_AlaIpmrmDebugError_Type.__name__ = "Integer32"
_AlaIpmrmDebugError_Object = MibScalar
alaIpmrmDebugError = _AlaIpmrmDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 1, 1, 2),
    _AlaIpmrmDebugError_Type()
)
alaIpmrmDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmrmDebugError.setStatus("deprecated")


class _AlaIpmrmDebugFib_Type(Integer32):
    """Custom type alaIpmrmDebugFib based on Integer32"""
    defaultValue = 2

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


_AlaIpmrmDebugFib_Type.__name__ = "Integer32"
_AlaIpmrmDebugFib_Object = MibScalar
alaIpmrmDebugFib = _AlaIpmrmDebugFib_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 1, 1, 3),
    _AlaIpmrmDebugFib_Type()
)
alaIpmrmDebugFib.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmrmDebugFib.setStatus("deprecated")


class _AlaIpmrmDebugAging_Type(Integer32):
    """Custom type alaIpmrmDebugAging based on Integer32"""
    defaultValue = 2

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


_AlaIpmrmDebugAging_Type.__name__ = "Integer32"
_AlaIpmrmDebugAging_Object = MibScalar
alaIpmrmDebugAging = _AlaIpmrmDebugAging_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 1, 1, 4),
    _AlaIpmrmDebugAging_Type()
)
alaIpmrmDebugAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmrmDebugAging.setStatus("deprecated")


class _AlaIpmrmDebugProtos_Type(Integer32):
    """Custom type alaIpmrmDebugProtos based on Integer32"""
    defaultValue = 2

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


_AlaIpmrmDebugProtos_Type.__name__ = "Integer32"
_AlaIpmrmDebugProtos_Object = MibScalar
alaIpmrmDebugProtos = _AlaIpmrmDebugProtos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 1, 1, 5),
    _AlaIpmrmDebugProtos_Type()
)
alaIpmrmDebugProtos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmrmDebugProtos.setStatus("deprecated")


class _AlaIpmrmDebugIpms_Type(Integer32):
    """Custom type alaIpmrmDebugIpms based on Integer32"""
    defaultValue = 2

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


_AlaIpmrmDebugIpms_Type.__name__ = "Integer32"
_AlaIpmrmDebugIpms_Object = MibScalar
alaIpmrmDebugIpms = _AlaIpmrmDebugIpms_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 1, 1, 6),
    _AlaIpmrmDebugIpms_Type()
)
alaIpmrmDebugIpms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmrmDebugIpms.setStatus("deprecated")


class _AlaIpmrmDebugMip_Type(Integer32):
    """Custom type alaIpmrmDebugMip based on Integer32"""
    defaultValue = 2

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


_AlaIpmrmDebugMip_Type.__name__ = "Integer32"
_AlaIpmrmDebugMip_Object = MibScalar
alaIpmrmDebugMip = _AlaIpmrmDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 1, 1, 7),
    _AlaIpmrmDebugMip_Type()
)
alaIpmrmDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmrmDebugMip.setStatus("deprecated")


class _AlaIpmrmDebugInit_Type(Integer32):
    """Custom type alaIpmrmDebugInit based on Integer32"""
    defaultValue = 2

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


_AlaIpmrmDebugInit_Type.__name__ = "Integer32"
_AlaIpmrmDebugInit_Object = MibScalar
alaIpmrmDebugInit = _AlaIpmrmDebugInit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 1, 1, 8),
    _AlaIpmrmDebugInit_Type()
)
alaIpmrmDebugInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmrmDebugInit.setStatus("deprecated")


class _AlaIpmrmDebugTm_Type(Integer32):
    """Custom type alaIpmrmDebugTm based on Integer32"""
    defaultValue = 2

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


_AlaIpmrmDebugTm_Type.__name__ = "Integer32"
_AlaIpmrmDebugTm_Object = MibScalar
alaIpmrmDebugTm = _AlaIpmrmDebugTm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 1, 1, 9),
    _AlaIpmrmDebugTm_Type()
)
alaIpmrmDebugTm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmrmDebugTm.setStatus("deprecated")


class _AlaIpmrmDebugMisc_Type(Integer32):
    """Custom type alaIpmrmDebugMisc based on Integer32"""
    defaultValue = 2

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


_AlaIpmrmDebugMisc_Type.__name__ = "Integer32"
_AlaIpmrmDebugMisc_Object = MibScalar
alaIpmrmDebugMisc = _AlaIpmrmDebugMisc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 1, 1, 10),
    _AlaIpmrmDebugMisc_Type()
)
alaIpmrmDebugMisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmrmDebugMisc.setStatus("deprecated")


class _AlaIpmrmDebugAll_Type(Integer32):
    """Custom type alaIpmrmDebugAll based on Integer32"""
    defaultValue = 2

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


_AlaIpmrmDebugAll_Type.__name__ = "Integer32"
_AlaIpmrmDebugAll_Object = MibScalar
alaIpmrmDebugAll = _AlaIpmrmDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 1, 1, 11),
    _AlaIpmrmDebugAll_Type()
)
alaIpmrmDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmrmDebugAll.setStatus("deprecated")
_AlcatelIND1IPMRMMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IPMRMMIBConformance = _AlcatelIND1IPMRMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 2)
)
_AlcatelIND1IPMRMMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IPMRMMIBCompliances = _AlcatelIND1IPMRMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 2, 1)
)
_AlcatelIND1IPMRMMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IPMRMMIBGroups = _AlcatelIND1IPMRMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 2, 2)
)

# Managed Objects groups

alaIpmrmDebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 2, 2, 2)
)
alaIpmrmDebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmDebugLevel"),
        ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmDebugError"),
        ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmDebugFib"),
        ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmDebugAging"),
        ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmDebugProtos"),
        ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmDebugIpms"),
        ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmDebugMip"),
        ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmDebugInit"),
        ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmDebugTm"),
        ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmDebugMisc"),
        ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmDebugAll"))
)
if mibBuilder.loadTexts:
    alaIpmrmDebugMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaIpmrmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 10, 1, 2, 1, 1)
)
alaIpmrmCompliance.setObjects(
    ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmDebugMIBGroup")
)
if mibBuilder.loadTexts:
    alaIpmrmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-IPMRM-MIB",
    **{"alcatelIND1IPMRMMIB": alcatelIND1IPMRMMIB,
       "alcatelIND1IPMRMMIBObjects": alcatelIND1IPMRMMIBObjects,
       "alaIpmrmDebugConfig": alaIpmrmDebugConfig,
       "alaIpmrmDebugLevel": alaIpmrmDebugLevel,
       "alaIpmrmDebugError": alaIpmrmDebugError,
       "alaIpmrmDebugFib": alaIpmrmDebugFib,
       "alaIpmrmDebugAging": alaIpmrmDebugAging,
       "alaIpmrmDebugProtos": alaIpmrmDebugProtos,
       "alaIpmrmDebugIpms": alaIpmrmDebugIpms,
       "alaIpmrmDebugMip": alaIpmrmDebugMip,
       "alaIpmrmDebugInit": alaIpmrmDebugInit,
       "alaIpmrmDebugTm": alaIpmrmDebugTm,
       "alaIpmrmDebugMisc": alaIpmrmDebugMisc,
       "alaIpmrmDebugAll": alaIpmrmDebugAll,
       "alcatelIND1IPMRMMIBConformance": alcatelIND1IPMRMMIBConformance,
       "alcatelIND1IPMRMMIBCompliances": alcatelIND1IPMRMMIBCompliances,
       "alaIpmrmCompliance": alaIpmrmCompliance,
       "alcatelIND1IPMRMMIBGroups": alcatelIND1IPMRMMIBGroups,
       "alaIpmrmDebugMIBGroup": alaIpmrmDebugMIBGroup}
)
