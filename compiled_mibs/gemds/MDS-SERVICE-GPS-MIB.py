# SNMP MIB module (MDS-SERVICE-GPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gemds\MDS-SERVICE-GPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:35 2025
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

(mdsServices,) = mibBuilder.importSymbols(
    "MDS-ORBIT-SMI-MIB",
    "mdsServices")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mdsGpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12)
)
if mibBuilder.loadTexts:
    mdsGpsMIB.setRevisions(
        ("2018-05-16 00:00",
         "2016-06-06 00:00",
         "2015-01-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MGpsMIBObjects_ObjectIdentity = ObjectIdentity
mGpsMIBObjects = _MGpsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1)
)
_MGpsConfig_ObjectIdentity = ObjectIdentity
mGpsConfig = _MGpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 1)
)
_MGpsStatus_ObjectIdentity = ObjectIdentity
mGpsStatus = _MGpsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2)
)


class _MGpsStatusFixMode_Type(Integer32):
    """Custom type mGpsStatusFixMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nofix", 0),
          ("a2dfix", 1),
          ("a3dfix", 2))
    )


_MGpsStatusFixMode_Type.__name__ = "Integer32"
_MGpsStatusFixMode_Object = MibScalar
mGpsStatusFixMode = _MGpsStatusFixMode_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 1),
    _MGpsStatusFixMode_Type()
)
mGpsStatusFixMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsStatusFixMode.setStatus("current")
_MGpsStatusTime_Type = OctetString
_MGpsStatusTime_Object = MibScalar
mGpsStatusTime = _MGpsStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 2),
    _MGpsStatusTime_Type()
)
mGpsStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsStatusTime.setStatus("current")
_MGpsStatusLatitude_Type = OctetString
_MGpsStatusLatitude_Object = MibScalar
mGpsStatusLatitude = _MGpsStatusLatitude_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 3),
    _MGpsStatusLatitude_Type()
)
mGpsStatusLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsStatusLatitude.setStatus("current")
_MGpsStatusLongitude_Type = OctetString
_MGpsStatusLongitude_Object = MibScalar
mGpsStatusLongitude = _MGpsStatusLongitude_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 4),
    _MGpsStatusLongitude_Type()
)
mGpsStatusLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsStatusLongitude.setStatus("current")
_MGpsStatusAltitude_Type = OctetString
_MGpsStatusAltitude_Object = MibScalar
mGpsStatusAltitude = _MGpsStatusAltitude_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 5),
    _MGpsStatusAltitude_Type()
)
mGpsStatusAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsStatusAltitude.setStatus("current")
_MGpsStatusSpeed_Type = OctetString
_MGpsStatusSpeed_Object = MibScalar
mGpsStatusSpeed = _MGpsStatusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 6),
    _MGpsStatusSpeed_Type()
)
mGpsStatusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsStatusSpeed.setStatus("current")
_MGpsStatusHeading_Type = OctetString
_MGpsStatusHeading_Object = MibScalar
mGpsStatusHeading = _MGpsStatusHeading_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 7),
    _MGpsStatusHeading_Type()
)
mGpsStatusHeading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsStatusHeading.setStatus("current")


class _MGpsStatusSatellitesVisible_Type(Unsigned32):
    """Custom type mGpsStatusSatellitesVisible based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MGpsStatusSatellitesVisible_Type.__name__ = "Unsigned32"
_MGpsStatusSatellitesVisible_Object = MibScalar
mGpsStatusSatellitesVisible = _MGpsStatusSatellitesVisible_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 8),
    _MGpsStatusSatellitesVisible_Type()
)
mGpsStatusSatellitesVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsStatusSatellitesVisible.setStatus("current")


class _MGpsStatusSatellitesUsed_Type(Unsigned32):
    """Custom type mGpsStatusSatellitesUsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MGpsStatusSatellitesUsed_Type.__name__ = "Unsigned32"
_MGpsStatusSatellitesUsed_Object = MibScalar
mGpsStatusSatellitesUsed = _MGpsStatusSatellitesUsed_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 9),
    _MGpsStatusSatellitesUsed_Type()
)
mGpsStatusSatellitesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsStatusSatellitesUsed.setStatus("current")
_MGpsSatellitesTable_Object = MibTable
mGpsSatellitesTable = _MGpsSatellitesTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10)
)
if mibBuilder.loadTexts:
    mGpsSatellitesTable.setStatus("current")
_MGpsSatellitesEntry_Object = MibTableRow
mGpsSatellitesEntry = _MGpsSatellitesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1)
)
mGpsSatellitesEntry.setIndexNames(
    (0, "MDS-SERVICE-GPS-MIB", "mGpsSatellitesPrn"),
)
if mibBuilder.loadTexts:
    mGpsSatellitesEntry.setStatus("current")


class _MGpsSatellitesPrn_Type(Unsigned32):
    """Custom type mGpsSatellitesPrn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MGpsSatellitesPrn_Type.__name__ = "Unsigned32"
_MGpsSatellitesPrn_Object = MibTableColumn
mGpsSatellitesPrn = _MGpsSatellitesPrn_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 1),
    _MGpsSatellitesPrn_Type()
)
mGpsSatellitesPrn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGpsSatellitesPrn.setStatus("current")
_MGpsSatellitesUsed_Type = TruthValue
_MGpsSatellitesUsed_Object = MibTableColumn
mGpsSatellitesUsed = _MGpsSatellitesUsed_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 2),
    _MGpsSatellitesUsed_Type()
)
mGpsSatellitesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsSatellitesUsed.setStatus("current")


class _MGpsSatellitesElevation_Type(Unsigned32):
    """Custom type mGpsSatellitesElevation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MGpsSatellitesElevation_Type.__name__ = "Unsigned32"
_MGpsSatellitesElevation_Object = MibTableColumn
mGpsSatellitesElevation = _MGpsSatellitesElevation_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 3),
    _MGpsSatellitesElevation_Type()
)
mGpsSatellitesElevation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsSatellitesElevation.setStatus("current")


class _MGpsSatellitesAzimuth_Type(Unsigned32):
    """Custom type mGpsSatellitesAzimuth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MGpsSatellitesAzimuth_Type.__name__ = "Unsigned32"
_MGpsSatellitesAzimuth_Object = MibTableColumn
mGpsSatellitesAzimuth = _MGpsSatellitesAzimuth_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 4),
    _MGpsSatellitesAzimuth_Type()
)
mGpsSatellitesAzimuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsSatellitesAzimuth.setStatus("current")


class _MGpsSatellitesSnr_Type(Unsigned32):
    """Custom type mGpsSatellitesSnr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MGpsSatellitesSnr_Type.__name__ = "Unsigned32"
_MGpsSatellitesSnr_Object = MibTableColumn
mGpsSatellitesSnr = _MGpsSatellitesSnr_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 5),
    _MGpsSatellitesSnr_Type()
)
mGpsSatellitesSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsSatellitesSnr.setStatus("current")
_MGpsSourcesTable_Object = MibTable
mGpsSourcesTable = _MGpsSourcesTable_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 3)
)
if mibBuilder.loadTexts:
    mGpsSourcesTable.setStatus("current")
_MGpsSourcesEntry_Object = MibTableRow
mGpsSourcesEntry = _MGpsSourcesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 3, 1)
)
mGpsSourcesEntry.setIndexNames(
    (0, "MDS-SERVICE-GPS-MIB", "mGpsSourceName"),
)
if mibBuilder.loadTexts:
    mGpsSourcesEntry.setStatus("current")
_MGpsSourceName_Type = DisplayString
_MGpsSourceName_Object = MibTableColumn
mGpsSourceName = _MGpsSourceName_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 3, 1, 1),
    _MGpsSourceName_Type()
)
mGpsSourceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mGpsSourceName.setStatus("current")
_MGpsSourceDevice_Type = OctetString
_MGpsSourceDevice_Object = MibTableColumn
mGpsSourceDevice = _MGpsSourceDevice_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 3, 1, 2),
    _MGpsSourceDevice_Type()
)
mGpsSourceDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGpsSourceDevice.setStatus("current")
_MdsGpsMIBConformance_ObjectIdentity = ObjectIdentity
mdsGpsMIBConformance = _MdsGpsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3)
)
_MdsGpsMIBCompliances_ObjectIdentity = ObjectIdentity
mdsGpsMIBCompliances = _MdsGpsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 1)
)
_MdsGpsMIBGroups_ObjectIdentity = ObjectIdentity
mdsGpsMIBGroups = _MdsGpsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 2)
)

# Managed Objects groups

mGpsStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 2, 1)
)
mGpsStatusGroup.setObjects(
      *(("MDS-SERVICE-GPS-MIB", "mGpsStatusFixMode"),
        ("MDS-SERVICE-GPS-MIB", "mGpsStatusTime"),
        ("MDS-SERVICE-GPS-MIB", "mGpsStatusLatitude"),
        ("MDS-SERVICE-GPS-MIB", "mGpsStatusLongitude"),
        ("MDS-SERVICE-GPS-MIB", "mGpsStatusAltitude"),
        ("MDS-SERVICE-GPS-MIB", "mGpsStatusSpeed"),
        ("MDS-SERVICE-GPS-MIB", "mGpsStatusHeading"),
        ("MDS-SERVICE-GPS-MIB", "mGpsStatusSatellitesVisible"),
        ("MDS-SERVICE-GPS-MIB", "mGpsStatusSatellitesUsed"),
        ("MDS-SERVICE-GPS-MIB", "mGpsSatellitesUsed"),
        ("MDS-SERVICE-GPS-MIB", "mGpsSatellitesElevation"),
        ("MDS-SERVICE-GPS-MIB", "mGpsSatellitesAzimuth"),
        ("MDS-SERVICE-GPS-MIB", "mGpsSatellitesSnr"))
)
if mibBuilder.loadTexts:
    mGpsStatusGroup.setStatus("current")

mGpsSourcesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 2, 2)
)
mGpsSourcesGroup.setObjects(
    ("MDS-SERVICE-GPS-MIB", "mGpsSourceDevice")
)
if mibBuilder.loadTexts:
    mGpsSourcesGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mGpsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 1, 1)
)
mGpsCompliance.setObjects(
      *(("MDS-SERVICE-GPS-MIB", "mGpsStatusGroup"),
        ("MDS-SERVICE-GPS-MIB", "mGpsSourcesGroup"))
)
if mibBuilder.loadTexts:
    mGpsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MDS-SERVICE-GPS-MIB",
    **{"mdsGpsMIB": mdsGpsMIB,
       "mGpsMIBObjects": mGpsMIBObjects,
       "mGpsConfig": mGpsConfig,
       "mGpsStatus": mGpsStatus,
       "mGpsStatusFixMode": mGpsStatusFixMode,
       "mGpsStatusTime": mGpsStatusTime,
       "mGpsStatusLatitude": mGpsStatusLatitude,
       "mGpsStatusLongitude": mGpsStatusLongitude,
       "mGpsStatusAltitude": mGpsStatusAltitude,
       "mGpsStatusSpeed": mGpsStatusSpeed,
       "mGpsStatusHeading": mGpsStatusHeading,
       "mGpsStatusSatellitesVisible": mGpsStatusSatellitesVisible,
       "mGpsStatusSatellitesUsed": mGpsStatusSatellitesUsed,
       "mGpsSatellitesTable": mGpsSatellitesTable,
       "mGpsSatellitesEntry": mGpsSatellitesEntry,
       "mGpsSatellitesPrn": mGpsSatellitesPrn,
       "mGpsSatellitesUsed": mGpsSatellitesUsed,
       "mGpsSatellitesElevation": mGpsSatellitesElevation,
       "mGpsSatellitesAzimuth": mGpsSatellitesAzimuth,
       "mGpsSatellitesSnr": mGpsSatellitesSnr,
       "mGpsSourcesTable": mGpsSourcesTable,
       "mGpsSourcesEntry": mGpsSourcesEntry,
       "mGpsSourceName": mGpsSourceName,
       "mGpsSourceDevice": mGpsSourceDevice,
       "mdsGpsMIBConformance": mdsGpsMIBConformance,
       "mdsGpsMIBCompliances": mdsGpsMIBCompliances,
       "mGpsCompliance": mGpsCompliance,
       "mdsGpsMIBGroups": mdsGpsMIBGroups,
       "mGpsStatusGroup": mGpsStatusGroup,
       "mGpsSourcesGroup": mGpsSourcesGroup}
)
