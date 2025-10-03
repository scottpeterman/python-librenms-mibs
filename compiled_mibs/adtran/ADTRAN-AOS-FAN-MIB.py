# SNMP MIB module (ADTRAN-AOS-FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adtran\ADTRAN-AOS-FAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:14:18 2025
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

(adGenAOSCommon,
 adGenAOSConformance) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSCommon",
    "adGenAOSConformance")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

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

adGenAOSFanMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 8)
)
if mibBuilder.loadTexts:
    adGenAOSFanMib.setRevisions(
        ("2013-10-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSFan_ObjectIdentity = ObjectIdentity
adGenAOSFan = _AdGenAOSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8)
)
_AdGenAOSFanTrap_ObjectIdentity = ObjectIdentity
adGenAOSFanTrap = _AdGenAOSFanTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 0)
)
_AdGenAOSFanTrapControl_ObjectIdentity = ObjectIdentity
adGenAOSFanTrapControl = _AdGenAOSFanTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 1)
)


class _AdGenAOSFanTrapEnable_Type(Integer32):
    """Custom type adGenAOSFanTrapEnable based on Integer32"""
    defaultValue = 2

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


_AdGenAOSFanTrapEnable_Type.__name__ = "Integer32"
_AdGenAOSFanTrapEnable_Object = MibScalar
adGenAOSFanTrapEnable = _AdGenAOSFanTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 1, 1),
    _AdGenAOSFanTrapEnable_Type()
)
adGenAOSFanTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSFanTrapEnable.setStatus("current")
_AdGenAOSFanInfo_ObjectIdentity = ObjectIdentity
adGenAOSFanInfo = _AdGenAOSFanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 2)
)
_AdGenAOSFanNumber_Type = Integer32
_AdGenAOSFanNumber_Object = MibScalar
adGenAOSFanNumber = _AdGenAOSFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 2, 1),
    _AdGenAOSFanNumber_Type()
)
adGenAOSFanNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adGenAOSFanNumber.setStatus("current")
_AdGenAOSFanConformance_ObjectIdentity = ObjectIdentity
adGenAOSFanConformance = _AdGenAOSFanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17)
)
_AdGenAOSFanGroups_ObjectIdentity = ObjectIdentity
adGenAOSFanGroups = _AdGenAOSFanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1)
)
_AdGenAOSFanCompliances_ObjectIdentity = ObjectIdentity
adGenAOSFanCompliances = _AdGenAOSFanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 2)
)

# Managed Objects groups

adGenAOSFanTrapCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1, 1)
)
adGenAOSFanTrapCfgGroup.setObjects(
    ("ADTRAN-AOS-FAN-MIB", "adGenAOSFanTrapEnable")
)
if mibBuilder.loadTexts:
    adGenAOSFanTrapCfgGroup.setStatus("current")

adGenAOSFanTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1, 2)
)
adGenAOSFanTrapGroup.setObjects(
    ("ADTRAN-AOS-FAN-MIB", "adGenAOSFanNumber")
)
if mibBuilder.loadTexts:
    adGenAOSFanTrapGroup.setStatus("current")


# Notification objects

adGenAOSFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 0, 1)
)
adGenAOSFanFailure.setObjects(
    ("ADTRAN-AOS-FAN-MIB", "adGenAOSFanNumber")
)
if mibBuilder.loadTexts:
    adGenAOSFanFailure.setStatus(
        "current"
    )


# Notifications groups

adGenAOSFanNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1, 3)
)
adGenAOSFanNotificationGroup.setObjects(
    ("ADTRAN-AOS-FAN-MIB", "adGenAOSFanFailure")
)
if mibBuilder.loadTexts:
    adGenAOSFanNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adGenAOSFanFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 2, 1)
)
adGenAOSFanFullCompliance.setObjects(
      *(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanTrapCfgGroup"),
        ("ADTRAN-AOS-FAN-MIB", "adGenAOSFanTrapGroup"),
        ("ADTRAN-AOS-FAN-MIB", "adGenAOSFanNotificationGroup"))
)
if mibBuilder.loadTexts:
    adGenAOSFanFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-FAN-MIB",
    **{"adGenAOSFan": adGenAOSFan,
       "adGenAOSFanTrap": adGenAOSFanTrap,
       "adGenAOSFanFailure": adGenAOSFanFailure,
       "adGenAOSFanTrapControl": adGenAOSFanTrapControl,
       "adGenAOSFanTrapEnable": adGenAOSFanTrapEnable,
       "adGenAOSFanInfo": adGenAOSFanInfo,
       "adGenAOSFanNumber": adGenAOSFanNumber,
       "adGenAOSFanConformance": adGenAOSFanConformance,
       "adGenAOSFanGroups": adGenAOSFanGroups,
       "adGenAOSFanTrapCfgGroup": adGenAOSFanTrapCfgGroup,
       "adGenAOSFanTrapGroup": adGenAOSFanTrapGroup,
       "adGenAOSFanNotificationGroup": adGenAOSFanNotificationGroup,
       "adGenAOSFanCompliances": adGenAOSFanCompliances,
       "adGenAOSFanFullCompliance": adGenAOSFanFullCompliance,
       "adGenAOSFanMib": adGenAOSFanMib}
)
